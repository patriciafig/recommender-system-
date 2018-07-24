#
# Patricia Figueroa
# CSCI 4800 : Networks and Informatics
# User to User Recommender System using the Facebook dataset
#


import networkx as nx
import matplotlib.pyplot as plt

'''
import glob

edge_list = []
edge_files = glob.glob("facebook/*.edges")
for edge_file_name in edge_files:
    file = open(edge_file_name, "r")
    for line in file:
        edge_list.append(line.split())
    file.close()

graph = nx.Graph(edge_list)

'''


graph = nx.read_edgelist('facebook/facebook_combined.txt', create_using=nx.Graph(), nodetype=int)

# Print the info of the graph
print(nx.info(graph))


def recommend_friend(g, u_id, count=10):
    """
    Method to recommend friend for a given user
    :param g: Graph
    :param u_id: id of the person to get the recommendations for
    :param count: Number of friend recommendations
    :return: a list of friend recommendations

    """

    # find the neighbors of the given user
    neighbors = g.neighbors(n=u_id)
    friends = []
    processed = set()
    processed.add(u_id)
    queue = []
    # Add all the neighbors to the queue
    for n in neighbors:
        queue.append(n)
        # We cannot recommend the people who are already friends
        # So, add them to processed
        processed.add(n)
    # Now perform a BFS to find the neighbors of the neighbors
    while len(queue) != 0 and len(friends) < count:
        # Get the head of the queue
        current = queue[0]
        # Pop it
        queue.remove(current)

        # Get the neighbors and add to friends
        current_neighbors = g.neighbors(current)
        # For each neighbor of the current neighbor
        for current_neighbor in current_neighbors:
            # If this neighbor hasn't been processed yet
            if current_neighbor not in processed:
                # Add them to the recommended friends
                friends.append(current_neighbor)
                # And to the queue for further processing
                queue.append(current_neighbor)
                if len(friends) == count:
                    return friends
        # Add the current node to the set of processed nodes
        processed.add(current)

    if len(friends) > count:
        return friends[:count]

    return friends


# Print 10 recommendations for user 0
recommended = recommend_friend(graph, 0)
print(recommended)

# Plot the graph
sp = nx.spring_layout(graph)
plt.axis('off')
nx.draw_networkx(graph, sp, with_labels=False, node_size=35)
plt.show()


