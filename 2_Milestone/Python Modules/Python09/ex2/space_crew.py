from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum
import json


class CrewRank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        ranks = [member.rank for member in self.crew]
        if CrewRank.commander not in ranks and CrewRank.captain not in ranks:
            raise ValueError("Must have at least one Commander or Captain")
        experienced_crew = len([member for member in
                                self.crew if member.years_experience >= 5])
        if (self.duration_days > 365
                and experienced_crew < len(self.crew) * 0.5):
            raise ValueError("Long missions (> 365 days) need 50% experienced "
                             "crew (5+ years)")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Valid mission created:")
    with open("../data_generator/generated_data/space_missions.json") as f:
        missions_data = json.load(f)
    mission = SpaceMission(**missions_data[0])
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budged: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) "
              f"- {member.specialization}")

    print("\n========================================")
    print("Expected validation error:")
    try:
        for member in missions_data[0]["crew"]:
            member["rank"] = "cadet"
        invalid_mission = SpaceMission(**missions_data[0])
        print(invalid_mission)
    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("========================================")
    main()
