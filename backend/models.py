from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Recording(Base):
    __tablename__ = "recordings"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    original_filename = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending, transcribing, diarizing, done, error
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    segments = relationship("Segment", back_populates="recording")


class Segment(Base):
    __tablename__ = "segments"

    id = Column(Integer, primary_key=True, index=True)
    recording_id = Column(Integer, ForeignKey("recordings.id"), nullable=False)
    speaker = Column(String, default="UNKNOWN")
    text = Column(Text, nullable=False)
    start_time = Column(Float, nullable=False)
    end_time = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    recording = relationship("Recording", back_populates="segments")
    arguments = relationship("Argument", back_populates="segment")


class Argument(Base):
    __tablename__ = "arguments"

    id = Column(Integer, primary_key=True, index=True)
    segment_id = Column(Integer, ForeignKey("segments.id"), nullable=False)
    arg_type = Column(String, nullable=True)      # CLAIM or PREMISE
    relation = Column(String, nullable=True)       # SUPPORT or ATTACK
    confidence = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    segment = relationship("Segment", back_populates="arguments")