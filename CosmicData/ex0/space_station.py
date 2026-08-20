from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    # use Field() for additional configuration:
    # description, constraints, alias, etc.
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)  # ge: greater or equal
    power_level: float = Field(ge=0.0, le=100.0)  # le: less or equal
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    try:
        print("========================================")
        valid_eg = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            last_maintenance="2026-08-20T16:30:00"
        )
        print("Valid station created:")
        print("ID: ", valid_eg.station_id)
        print("Name: ", valid_eg.name)
        print("Crew: ", valid_eg.crew_size, " people")
        print("Power: ", valid_eg.power_level)
        print("Oxygen: ", valid_eg.oxygen_level)
        status = ("Operational" if valid_eg.is_operational
                  else "Non-operational")
        print("Status: ", status)
        print("========================================")
        invalid_eg = SpaceStation(
            station_id="abc",
            name="invalid",
            crew_size=21,
            power_level=10,
            oxygen_level=20,
            last_maintenance="2026-08-20T16:10:00"
        )
        print("ID: ", invalid_eg.station_id)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
