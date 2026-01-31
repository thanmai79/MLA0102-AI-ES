import math
from collections import Counter

# Dataset (from your image)
data = [
    ['True','Hot','High','No'],
    ['True','Hot','High','No'],
    ['False','Hot','High','Yes'],
    ['False','Cool','Normal','Yes'],
    ['False','Cool','Normal','Yes'],
    ['True','Cool','High','No'],
    ['True','Hot','High','No'],
    ['True','Hot','Normal','Yes'],
    ['False','Cool','Normal','Yes'],
    ['False','Cool','High','Yes']
]

attributes = ['a1','a2','a3']

# Entropy
def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    ent = 0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent

# Information Gain
def info_gain(data, attr_index):
    total_entropy = entropy(data)
    values = set([row[attr_index] for row in data])
    subset_entropy = 0

    for v in values:
        subset = [row for row in data if row[attr_index] == v]
        subset_entropy += (len(subset)/len(data)) * entropy(subset)

    return total_entropy - subset_entropy

# Best attribute
def best_attribute(data):
    gains = []
    for i in range(len(attributes)):
        gains.append(info_gain(data, i))
    return gains.index(max(gains))

# ID3 Algorithm
def id3(data, attributes):
    labels = [row[-1] for row in data]

    # If all same class
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    # If no attributes left
    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    best = best_attribute(data)
    tree = {attributes[best]: {}}

    values = set([row[best] for row in data])

    for v in values:
        subset = [row for row in data if row[best] == v]
        sub_attrs = attributes[:best] + attributes[best+1:]

        subtree = id3([row[:best] + row[best+1:] for row in subset], sub_attrs)
        tree[attributes[best]][v] = subtree

    return tree

# Build tree
decision_tree = id3(data, attributes)
print("Decision Tree:")
print(decision_tree)
