"""
Test SpaceStation model using generated test data.
"""

from pydantic import ValidationError

from ex0.space_station import SpaceStation
from generated_data.space_stations import SPACE_STATIONS

from ex1.alien_contact import AlienContact
from generated_data.alien_contacts import ALIEN_CONTACTS

from ex2.space_crew import SpaceMission
from generated_data.space_missions import SPACE_MISSIONS


def test_space_stations():
    print("\nSpace Station Data Validation")
    print("========================================")

    for station_data in SPACE_STATIONS:
        try:
            station = SpaceStation(**station_data)

            print("Valid station created:")
            print("ID: ", station.station_id)
            print("Name: ", station.name)
            print("Crew: ", station.crew_size, " people")
            print("Power: ", station.power_level)
            print("Oxygen: ", station.oxygen_level)

            status = (
                "Operational"
                if station.is_operational
                else "Non-operational"
            )
            print("Status: ", status)
            print("========================================")

        except ValidationError as e:
            print("Expected validation error:")

            for error in e.errors():
                print(error["msg"])

            print("========================================")


def test_alien_contacts():
    print("\nAlien Contact Log Validation")
    print("======================================")

    for contact_data in ALIEN_CONTACTS:
        try:
            contact = AlienContact(**contact_data)

            print("Valid contact report:")
            print("ID: ", contact.contact_id)
            print("Type: ", contact.contact_type.value)
            print("Location: ", contact.location)
            print("Signal: ", contact.signal_strength, "/10")
            print("Duration: ", contact.duration_minutes, " minutes")
            print("Witnesses: ", contact.witness_count)
            print("Message: ", contact.message_received)

            print("======================================")

        except ValidationError as e:
            print("Expected validation error:")

            for error in e.errors():
                print(
                    error["msg"].removeprefix("Value error, ")
                )

            print("======================================")


def test_space_missions():
    print("\nSpace Mission Crew Validation")
    print("=========================================")

    for mission_data in SPACE_MISSIONS:
        try:
            mission = SpaceMission(**mission_data)

            print("Valid mission created:")
            print("Mission: ", mission.mission_name)
            print("ID: ", mission.mission_id)
            print("Destination: ", mission.destination)
            print("Duration: ", mission.duration_days, " days")
            print("Budget: $", mission.budget_millions, "M")
            print("Crew size: ", len(mission.crew))
            print("Crew members:")

            print("\n".join(
                f"- {mem.name} ({mem.rank.value}) - "
                f"{mem.specialization}"
                for mem in mission.crew
            ))

            print("=========================================")

        except ValidationError as e:
            print("Expected validation error:")

            for error in e.errors():
                print(
                    error["msg"].removeprefix("Value error, ")
                )

            print("=========================================")


if __name__ == "__main__":
    test_space_stations()
    test_alien_contacts()
    test_space_missions()
