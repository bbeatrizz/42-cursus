from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 10, 30, 0),
        is_operational=True,
    )
    if station.is_operational:
        status = "Operational"
    else:
        status = "Non-operational"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")
    print(f"Last maintance: {station.last_maintenance}")
    print("\n========================================")
    print("Expected validation error:")
    try:
        station_2 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=49,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 10, 30, 0),
            is_operational=True,
        )
        print(station_2)
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    main()
