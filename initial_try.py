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

def create_conditional_probability_table(data,network):
    '''this function creates conditional probability table based on data and the network of the data'''
    

def main():
    data=load_data("mystery_data2.csv")
    
    network=create_graph(data=data)

    print(network)
    
if __name__=="__main__":
    main()