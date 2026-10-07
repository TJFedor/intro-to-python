# Ewok Data Tracker - Created by Tristan

ewok_data = {
    "name": "Tristan",
    "age": 16,
    "weapon": "spear",
    "rank": "warrior"
}

print("Ewok name:", ewok_data["name"])
print("Ewok age:", ewok_data["age"])
print("Ewok weapon:", ewok_data["weapon"])
print("Ewok rank:", ewok_data["rank"]) 

ewok_data["weapon"] = "bow and arrow"
ewok_data["rank"] = "chief"
ewok_data["homeland"] = "Earth"

print("\nUpdated Ewok Data:")
for key, value in ewok_data.items():
    print(f"{key}: {value}")

ewok_tribe = {
    "tristan": ewok_data,
    "Zane": {
        "name": "Zane",
        "age": 16,
        "weapon": "club",
        "rank": "warrior",
        "homeland": "Earth"
    }
}

print("\nEwok Tribe Data:")
for ewok_name, ewok_info in ewok_tribe.items():
    print(f"\nEwok: {ewok_name}")
    for key, value in ewok_info.items():
        print(f"{key}: {value}")