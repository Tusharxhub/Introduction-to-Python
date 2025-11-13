# Create a program that reads data from a JSON file containing user information, modifies a specific entry (e.g., changes a user's email), and saves the updated data back to a new JSON file.


import json

# Step 1: Read data from JSON file
with open("users.json", "r") as file:
    data = json.load(file)

# Step 2: Modify a specific entry (e.g., change email of user with id=2)
for user in data["users"]:
    if user["id"] == 2:
        user["email"] = "newemail@example.com"

# Step 3: Save updated data to a new JSON file
with open("updated_users.json", "w") as file:
    json.dump(data, file, indent=4)

print("User email updated successfully! ✅")
