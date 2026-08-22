from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Self


class Rank(Enum):
    cd = "cadet"
    of = "officer"
    lt = "lieutenant"
    cp = "captain"
    cm = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if not any(mem.rank in (Rank.cm, Rank.cp) for mem in self.crew):
            raise ValueError(
                'Mission must have at least one Commander or Captain')
        if self.duration_days > 365 and (
            sum(1 for mem in self.crew if mem.years_experience > 5)
            < len(self.crew) / 2
        ):
            raise ValueError('Long missions (> 365 days) need ',
                             '50/% /experienced crew (5+ years)')
        if not all(mem.is_active for mem in self.crew):
            raise ValueError('All crew members must be active')
        return self


def main() -> None:
    print('Space Mission Crew Validation')
    try:
        cm = CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank=Rank.cm,
            age=50,
            specialization='Mission Command',
            years_experience=30,
        )
        lt = CrewMember(
            member_id='002',
            name='John Smith',
            rank=Rank.lt,
            age=28,
            specialization='Navigation',
            years_experience=5
        )
        of = CrewMember(
            member_id='003',
            name='Alice Johnson',
            rank=Rank.of,
            age=30,
            specialization='Engineering',
            years_experience=6
        )
        mission1 = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date='20230812',
            duration_days=900,
            crew=[cm, lt, of],
            budget_millions=2500.0,
        )
        print("=========================================")
        print('Valid mission created:')
        print('Mission: ', mission1.mission_name)
        print('ID: ', mission1.mission_id)
        print('Destination: ', mission1.destination)
        print('Duration: ', mission1.duration_days, ' days')
        print('Budget: $', mission1.budget_millions, 'M')
        print('Crew size: ', len(mission1.crew))
        print('Crew members:')
        print("\n".join(
            f'- {mem.name} ({mem.rank.value}) - {mem.specialization}'
            for mem in mission1.crew
        ))
        print("=========================================")
        mission2 = SpaceMission(
            mission_id='M2028_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date='20270812',
            duration_days=100,
            crew=[lt, of],
            budget_millions=2500.0,
        )
        print('Mission: ', mission2.mission_name)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
