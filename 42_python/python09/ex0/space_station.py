from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """validate record of single space station status"""
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    """print h-r summary of valid station"""
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {'Operational' if station.is_operational else 'Offline'}")


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 10, 30, 0),
    )
    display_station(station)
    print("\n" + "=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="OVR001",
            name="Overcrowded Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance=datetime(2024, 1, 15, 10, 30, 0),
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
