from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RecordingResponse(BaseModel):
    id: int
    filename: str
    original_filename: str
    status: str
    error_message: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True