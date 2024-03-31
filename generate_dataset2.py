import random
import csv

# Define variables with their possible values and descriptions
variables = {
    "Weapon": {
        "Values": ["Knife", "Gun", "Poison", "Fists"],
        "Description": "Murder weapon"
    },
    "Location": {
        "Values": ["Living Room", "Kitchen", "Bedroom", "Garden"],
        "Description": "Location of the crime"
    },
    "Opportunity": {
        "Values": ["High", "Medium", "Low"],
        "Description": "Suspect's opportunity to commit the crime"
    },
    "Motive": {
        "Values": ["Jealousy", "Revenge", "Greed", "None"],
        "Description": "Suspect's motive for the crime"
    }
}

# Define suspects and possible solutions
suspects = ["John", "Mary", "Peter", "Alice"]
solutions = suspects.copy()  # All suspects are potential solutions

# Set the number of data points to generate
num_data_points = 1000

# Open CSV file for writing
with open("mystery_data2.csv", "w", newline="") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=[
      "Case ID", "Suspect", "Variable", "Value", "Description", "Solution"
  ])
  writer.writeheader()

  # Generate random data points
  for _ in range(num_data_points):
    data_point = {}

    # Generate unique Case ID
    data_point["Case ID"] = f"C{random.randint(1000, 9999)}"

    # Choose a random suspect
    data_point["Suspect"] = random.choice(suspects)

    # Choose a random variable and its value
    random_variable = random.choice(list(variables.keys()))
    data_point["Variable"] = random_variable
    data_point["Value"] = random.choice(variables[random_variable]["Values"])
    data_point["Description"] = variables[random_variable]["Description"]

    # Choose the solution (culprit) with a bias towards the chosen suspect (modify as needed)
    solution_probability = [1.0] * len(suspects)  # Initially equal probability
    solution_probability[suspects.index(data_point["Suspect"])] = 0.8  # Higher chance for chosen suspect
    data_point["Solution"] = random.choices(solutions, weights=solution_probability)[0]

    writer.writerow(data_point)

print(f"Generated {num_data_points} data points and saved to mystery_data2.csv")
