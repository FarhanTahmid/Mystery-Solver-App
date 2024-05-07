import pandas as pd
import networkx as nx

def load_data(filename):
    '''this function loads all the data from dataset'''
    
    data=pd.read_csv(filename)
    
    return data

def create_graph(data):
    '''this function creates a directed acyclic graph to from the data to'''
    
    graph=nx.DiGraph()
    
    # the elements_in_myster value defines the element of the mystery. Location, knife etc
    elements_in_mystery=list(set(data["Variable"]))
    
    # Adding all variables as nodes in the graph
    graph.add_nodes_from(elements_in_mystery)
    
    # adding edges based on relationships
    potential_edges=[
        ("Weapon","Location"),("Location","Opportunity"),("Opportunity","Motive"),
    ]
    for edge in potential_edges:
        if all(var in elements_in_mystery for var in edge):
            graph.add_edge(*edge)
    return graph

def all_assignments(elements_in_mystery,data):
    if not elements_in_mystery:
        yield[]
    else:
        element=elements_in_mystery[0]
        for element in data[element].unique():
            for assignment in all_assignments(elements_in_mystery[1:],data=data):
                yield[element]+assignment
            

def create_conditional_probability_table(data,network):
    '''this function creates conditional probability table based on data and the network of the data'''
    cpts = {}
    for var in network.nodes:
        parent_vars = list(network.predecessors(var))
        cpts[var] = {}
        if not parent_vars:  # Handle variables without parents (root nodes)
            value_counts = data[var].value_counts(normalize=True)
            cpts[var] = dict(value_counts)
        else:
            columns = parent_vars + [var]
            joint_distribution = data[columns].groupby(parent_vars).apply(lambda df: df[var].value_counts(normalize=True)).unstack(fill_value=0)

            for parent_assignment, dist in joint_distribution.iteritems():
                cpts[var][parent_assignment if len(parent_vars) > 1 else parent_assignment[0]] = dist.to_dict()
    return cpts



def main():
    data=load_data("mystery_data2.csv")
    
    network=create_graph(data=data)

    print(network)
    
    conditional_probability_table=create_conditional_probability_table(data=data.copy(),network=network)
    
    print(conditional_probability_table)
    
if __name__=="__main__":
    main()