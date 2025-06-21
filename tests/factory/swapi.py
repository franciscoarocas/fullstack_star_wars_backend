
def build_fake_swapi_people_data():
    return [
        {"name": "Luke Skywalker", "height": "172", "mass": "77"},
        {"name": "Darth Vader", "height": "202", "mass": "136"},
        {"name": "Leia Organa", "height": "150", "mass": "49"},
        {"name": "Han Solo", "height": "180", "mass": "80"},
        {"name": "Chewbacca", "height": "228", "mass": "112"}
    ]


def build_fake_swapi_planets_data():
    return [
        {"name": "Tatooine", "climate": "arid", "terrain": "desert"},
        {"name": "Alderaan", "climate": "temperate", "terrain": "grasslands, mountains"},
        {"name": "Hoth", "climate": "frozen", "terrain": "tundra, ice caves, mountain ranges"},
        {"name": "Dagobah", "climate": "murky", "terrain": "swamp, jungles"},
        {"name": "Bespin", "climate": "temperate", "terrain": "gas giant"}
    ]
