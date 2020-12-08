import re
import networkx as nx

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

# print(lines)

directed_bag_graph = nx.DiGraph()

for line in lines:
    parent_node = "_".join(line.strip().split()[:2])
    if parent_node not in directed_bag_graph.nodes:
        directed_bag_graph.add_node(parent_node)
    parent_child = line.strip().split("bags contain")

    for each_child in parent_child[1:][0].split(","):
        if each_child.endswith("."):
            each_child = each_child[:-1]
        if each_child.split()[0] == "1":
            child_node = "_".join(each_child.split("bag")[0].split()[1:])
            if child_node not in directed_bag_graph.nodes:
                directed_bag_graph.add_node(child_node)
            directed_bag_graph.add_edge(child_node, parent_node, weight=1)
        if each_child.split()[0] != "no":
            child_node = "_".join(each_child.split("bag")[0].split()[1:])
            if child_node not in directed_bag_graph.nodes:
                directed_bag_graph.add_node(child_node)
            directed_bag_graph.add_edge(child_node, parent_node, weight=int(each_child.split()[0]))

print(len(nx.algorithms.dfs_tree(directed_bag_graph, "shiny_gold").nodes) - 1)

reversed_graph = directed_bag_graph.reverse()


def recursive_sum(graph, node):
    return sum(directed_bag_graph[n][node]['weight'] * recursive_sum(graph, n) for n in graph.neighbors(node)) + 1


print(recursive_sum(reversed_graph, "shiny_gold") - 1)
