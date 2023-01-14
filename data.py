import pandas as pd

star_data = pd.read_csv("final1.csv")
star_rows = star_data[1:]

star_names = star_data["Star Name"]
star_distances = star_data["Distance (ly)"]
star_masses = star_data["Mass"]
star_radiuses = star_data["Radius"]
star_gravity = star_data["Surface Gravity"]

star_list = []
for index in range(len(star_rows) + 1):
    star_dictionary = {
        "Star Name" : star_names[index].replace('\xa0', ' '),
        "Distance" : star_distances[index],
        "Mass" : star_masses[index],
        "Radius" : star_radiuses[index],
        "Surface Gravity" : star_gravity[index]
    }
    star_list.append(star_dictionary)

print(star_list)
