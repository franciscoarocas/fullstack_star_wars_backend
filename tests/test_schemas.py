
from typing import Dict

from app.schemas.people import People
from app.schemas.planets import Planet


def build_fake_people_data() -> Dict[str, str]:
    return {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male"
    }


def test_people_schema():
    data = build_fake_people_data()

    people = People(**data)
    assert people.name == "Luke Skywalker"
    assert people.height == "172"
    assert people.mass == "77"
    assert people.hair_color == "blond"
    assert people.skin_color == "fair"
    assert people.eye_color == "blue"
    assert people.birth_year == "19BBY"
    assert people.gender == "male"