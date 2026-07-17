from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=200)
    is_verified: bool = False

    @model_validator(mode='after')
    def custom_validation(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should "
                             "include received messages")
        return self


def main() -> None:
    log_validation = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 15, 10, 30, 0),
        location="Area 51, Nevada",
        contact_type= ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="'Greetings from Zeta Reticuli'",
        is_verified=True
    )
    print("Valid contact report:")
    print(f"ID: {log_validation.contact_id}")
    print(f"Type: {log_validation.contact_type.value}")
    print(f"Location: {log_validation.location}")
    print(f"Signal: {log_validation.signal_strength}/10")
    print(f"Duration: {log_validation.duration_minutes} minutes")
    print(f"Witnesses: {log_validation.witness_count}")
    print(f"Message: {log_validation.message_received}")
    print("\n========================================")
    print("Expected validation error:")
    try:
        log_2 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 15, 10, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="'Greetings from Zeta Reticuli'",
            is_verified=True
        )
        print(log_2)
    except ValidationError as e:
        msg = e.errors()[0]["msg"]
        print(msg.replace("Value error, ", ""))


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("========================================")
    main()
