import joblib
import matplotlib.pyplot as plt
import pandas
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

decisions = ["decision"]
attributes = ["season", "trash_type", "mass", "space", "trash_mass"]


# return tree made from attributes
def tree():
    dataset = pandas.read_csv('decision_tree/tree_dataset.csv', sep=";")

    x = dataset[attributes]
    y = dataset[decisions]
    decision_tree = DecisionTreeClassifier()
    decision_tree = decision_tree.fit(x.values, y.values)

    return decision_tree


# return decision made from tree and attributes
def decision(decision_tree, season, trash_type, mass, space, trash_mass):
    decision = decision_tree.predict(
        [[season, trash_type , mass, space, trash_mass]])

    return decision


'''
we shall save output of our decision tree. It is possible for a few ways:
txt, png or structure
'''


def tree_as_txt(decision_tree):
    with open('./decision_tree/tree_as_txt.txt', "w") as file:
        file.write(export_text(decision_tree))


def tree_to_png(decision_tree):
    plt.figure()
    plot_tree(decision_tree, feature_names=attributes, filled=True)
    plt.title("Decision tree")
    plt.show()


def tree_to_structure(decision_tree):
    joblib.dump(decision_tree, './decision_tree/tree_model')


def tree_from_structure(file):
    return joblib.load(file)

#drzewo = tree()
#tree_as_txt(drzewo)
#tree_to_png(drzewo)
#tree_to_structure(drzewo)
