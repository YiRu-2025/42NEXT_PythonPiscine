from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum
from typing import Optional, Self


# Enum: Base class for creating enumerated constants.
# They make code cleaner, more readable and prevent using invalid values.
# Each member of an Enum has a name and a value.
class ContactType(Enum):
    r = "radio"
    v = "visual"
    p = "physical"
    t = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType  # ContactType enum
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    # After validators: run after the whole model has been validated.
    # As such, they are defined as instance methods and can be seen
    # as post-initialization hooks.
    # Important note: the validated instance should be returned.
    @model_validator(mode='after')
    def validation_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if (self.contact_type == ContactType.p
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.t
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    try:
        print("======================================")
        valid_eg = AlienContact(
            contact_id="AC_2024_001",
            timestamp="20260820",
            contact_type=ContactType.r,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print("ID: ", valid_eg.contact_id)
        print("Type: ", valid_eg.contact_type.value)
        print("Location", valid_eg.location)
        print("Signal: ", valid_eg.signal_strength, "/10")
        print("Duration: ", valid_eg.duration_minutes, " minutes")
        print("Witnesses: ", valid_eg.witness_count)
        print("Message ", valid_eg.message_received)

        print("======================================")
        invalid_eg = AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-01-16T22:00:00",
            location="Paris",
            contact_type=ContactType.t,
            signal_strength=4.0,
            duration_minutes=10,
            witness_count=1,
            is_verified=False,
        )
        print("ID: ", invalid_eg.contact_id)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
