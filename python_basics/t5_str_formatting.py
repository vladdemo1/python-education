"""Task about string formatting"""
growth = 200    # in cm
weight = 82    # in kg
first_name = "Vlad"
# Output info characteristics
print(f"Info about {first_name}. With growth {growth} cm and weight {weight} kg:")
print("Normal index weight") if weight / (growth**2) < 28 else print("Big boy")
