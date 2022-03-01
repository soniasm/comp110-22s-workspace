"""Demonstrations of dictionary capabilities."""


# declaring type of dictionary
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# set key-value pairing in dictionsry
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else: 
    print("No key 'Duke' in schools")
# is_duke_present: bool = "Duke" in schools

# print(f"Duke is present: {is_duke_present}")

schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literalys

# Empty dictionary literal
schools = {}  # same as dict()

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")