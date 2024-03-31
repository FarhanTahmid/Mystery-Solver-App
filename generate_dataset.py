import random
import csv

# Define number of data points to generate
num_data_points = 1000

# List of suspects
suspects = ["John", "Mary", "Peter", "Alice"]

# Possible variables and their values
variables = {
  "Weapon": ["Knife", "Gun", "Poison", "Fists"],
  "Location": ["Living Room", "Kitchen", "Bedroom", "Garden"],
  "Opportunity": ["High", "Medium", "Low"],
  "Motive": ["Jealousy", "Revenge", "Financial Gain", "None"]
}

# Open CSV file for writing
with open("mystery_data.csv", "w", newline="") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=["Case ID", "Suspect", "Variable", "Value", "Solution"])
  writer.writeheader()

  # Generate random data points
  for _ in range(num_data_points):
    data_point = {}

    # Generate unique Case ID
    data_point["Case ID"] = f"C{random.randint(1000, 9999)}"

    # Randomly choose a suspect
    data_point["Suspect"] = random.choice(suspects)

    # Randomly choose a variable and its value
    data_point["Variable"] = random.choice(list(variables.keys()))
    data_point["Value"] = random.choice(variables[data_point["Variable"]])

    # Randomly choose a culprit (solution) - Can be modified to consider variable influence
    data_point["Solution"] = random.choice(suspects)

    writer.writerow(data_point)

print(f"Generated {num_data_points} data points and saved to mystery_data.csv")
