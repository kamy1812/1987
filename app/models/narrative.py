"""Narrative data models."""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID, uuid4


class NarrativeDetails(BaseModel):
    """Details for narrative generation."""

    person_description: str = Field(
        ..., description="Description of the person in the narrative"
    )
    car_features: str = Field(
        ..., description="Description of car features and modifications"
    )
    setting: str = Field(..., description="Description of the setting/environment")
    additional_context: Optional[str] = Field(
        None, description="Any additional context for the narrative"
    )


class NarrativeRequest(BaseModel):
    """Request model for narrative generation."""

    style: str = Field(
        default="tokyo_drift_80s", description="Style of narrative generation"
    )
    theme: str = Field(default="car_scene", description="Theme of the narrative")
    mood: str = Field(default="cinematic", description="Mood/tone of the narrative")
    details: NarrativeDetails = Field(..., description="Narrative details")
    language: str = Field(default="en", description="Output language")
    length: str = Field(
        default="medium",
        description="Length of narrative (short, medium, long)",
    )


class NarrativeResponse(BaseModel):
    """Response model for generated narrative."""

    id: UUID = Field(default_factory=uuid4, description="Unique identifier")
    narrative: str = Field(..., description="Generated narrative text")
    style: str = Field(..., description="Style used for generation")
    theme: str = Field(..., description="Theme of the narrative")
    mood: str = Field(..., description="Mood of the narrative")
    language: str = Field(..., description="Language of the narrative")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="Additional metadata"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "narrative": "A vivid description of a person standing...",
                "style": "tokyo_drift_80s",
                "theme": "car_scene",
                "mood": "cinematic",
                "language": "en",
                "created_at": "2026-05-20T12:00:00Z",
            }
        }
