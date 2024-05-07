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


def create_conditional_probability_table(data, network):
  '''this function creates a conditional probability table based on data and the network of the data'''
  conditional_probability_table = {}
  
  for node in network.nodes:
      parent_nodes = list(network.predecessors(node))
      conditional_probability_table[node] = {}
      print(node)
      if not parent_nodes:
          # Normalize value counts for nodes without parents
          node_value_counts = data[node].value_counts(normalize=True)
          conditional_probability_table[node] = dict(node_value_counts)
      else:
          # Iterate over all possible assignments of values to parent nodes
          for parent_assignment in all_assignments(parent_nodes, data):
              if len(parent_nodes) == 1:
                  # Filter data for a single parent node
                  filtered_data = data[data[parent_nodes[0]] == parent_assignment[0]]
              else:
                  # Generate conditions for filtering data based on parent assignments
                  conditions = (data[parent_nodes[i]] == parent_assignment[i] for i in range(len(parent_nodes)))
                  filtered_data = data[np.all(np.column_stack(conditions), axis=1)]
              
              # Normalize value counts for nodes with parents
              node_value_counts = filtered_data[node].value_counts(normalize=True)
              conditional_probability_table[node][tuple(parent_assignment)] = dict(node_value_counts)
              print(parent_assignment)
              
  return conditional_probability_table


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
  cpts = create_conditional_probability_table(data.copy(), network)

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
