#%%
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# NB! Don't use this code in production, as it's not optimized for large datasets
geolocator = Nominatim(user_agent="geoapiExercises")


def geolocate(place):
    try:
        location = geolocator.geocode(place)
        if location:
            return (location.latitude, location.longitude)
        else:
            return (None, None)
    except GeocoderTimedOut:
        return (None, None)



def find_coordinates(places):
    # Create a dictionary to hold place names and their coordinates
    place_coordinates = {}

    for place in places:
        if place not in place_coordinates:  # Avoid duplicating API calls for the same place
            coords = geolocate(place)
            place_coordinates[place] = coords
            print(f"{place}: {coords}")
        else:
            print(f"{place} (duplicate): {place_coordinates[place]}")

# %%


if __name__ == "__main__":

    places = """
    Norges
    Baahus
    Finland
    Finmarken
    Halland
    Nordsøen
    Norge
    Sverige
    Sverige
    Upsala
    """.strip().splitlines()

    print(find_coordinates(places))
