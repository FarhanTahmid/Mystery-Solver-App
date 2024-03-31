import pandas as pd
import networkx as nx


def load_data(filename):
  """
  Loads the mystery data from a CSV file
  """
  data = pd.read_csv(filename)
  return data


def create_dag(data):
  """
  Creates a directed acyclic graph (DAG) from the data
  """
  G = nx.DiGraph()
  variables = list(set(data["Variable"]))

  # Add all variables as nodes
  G.add_nodes_from(variables)

  # Add edges based on potential relationships (replace with domain knowledge)
  possible_edges = [
      ("weapon", "location"),  # Weapon might be found at the location
      ("location", "opportunity"),  # Location can influence opportunity
      ("opportunity", "motive"),  # Opportunity might create motive
  ]

  # Add valid edges based on variables present in the data
  for edge in possible_edges:
    if all(var in variables for var in edge):
      G.add_edge(*edge)

  return G


def create_cpts(data, network):
  """
  Creates conditional probability tables (CPTs) based on data and network structure
  """
  cpts = {}
  for var in network.nodes:
    parent_vars = list(network.predecessors(var))
    cpts[var] = {}
    if not parent_vars:  # Handle variables without parents (root nodes)
      value_counts = data[var].value_counts(normalize=True)
      cpts[var] = dict(value_counts)
    else:
      for parent_assignment in all_assignments(parent_vars):
        # filtered_data = data.loc[(data[parent_vars[0]] == parent_assignment[0]) & (data[parent_vars[1]] == parent_assignment[1]) if len(parent_vars) > 1 else (data[parent_vars[0]] == parent_assignment[0])]
        # value_counts = filtered_data[var].value_counts(normalize=True)
        # cpts[var][parent_assignment] = dict(value_counts)
        print(parent_assignment)
  return cpts


def all_assignments(variables):
  """
  Generates all possible assignments of values for a list of variables
  """
  if not variables:
    yield []
  else:
    variable = variables[0]
    for value in data[variable].unique():
      for assignment in all_assignments(variables[1:]):
        yield [value] + assignment


def main():
  # Load data from CSV file (replace 'data.csv' with your actual file path)
  data = load_data("mystery_data2.csv")

  # Create the Directed Acyclic Graph (DAG)
  network = create_dag(data)

  # Create Conditional Probability Tables (CPTs) from data
  cpts = create_cpts(data.copy(), network)

  # Example to calculate posterior probability for a scenario (modify as needed)
  evidence = {
      "weapon": "knife",
      "location": "library"
  }

  # Update probabilities based on evidence (replace with actual inference algorithm)
  for var, value in evidence.items():
    for parent in network.predecessors(var):
      del cpts[var][network.nodes[parent]["value"]]  # Remove previous CPT entry (assuming single parent for simplicity)
    parent_assignment = tuple(evidence[p] for p in network.predecessors(var))
    network.nodes[var]["probability"] = cpts[var][parent_assignment][value]

  # Print suspect probabilities (assuming 'Solution' variable holds suspect names)
  solution_probs = {s: network.nodes[s]["probability"] for s in data["Solution"].unique()}
  print("Suspect Probabilities:")
  for suspect, prob in solution_probs.items():
    print(f"\t- {suspect}: {prob:.2f}")


if __name__ == "__main__":
  main()
