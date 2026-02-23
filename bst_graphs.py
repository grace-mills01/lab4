import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import time

sys.setrecursionlimit(10**9)
from bst import *

TREES_PER_RUN: int = int(1e4)
N_MAX: int = 50

def float_before(a: float, b: float) -> bool:
    return a < b

def random_tree(n: int) -> BinarySearchTree:
    if(n == 0):
        return BinarySearchTree(float_before, None)
    if(n == 1):
        return BinarySearchTree(float_before, Node(random.random(), None, None))
    return insert(random_tree(n-1), random.random())

def get_max_height(bst: BinarySearchTree) -> int:
    all_heights : list[int] = []

    def traverse_tree(bin_tree: BinTree, all_heights: list[int], depth: int) -> None:
        match bin_tree:
            case None:
                all_heights.append(depth)
            case Node(val, left, right):
                traverse_tree(left, all_heights, depth+1)
                traverse_tree(right, all_heights, depth+1)

    traverse_tree(bst.binTree, all_heights, 0)

    return max(all_heights)


def graph_1() -> None:
    def f_to_graph(n: int) -> float:
        heights_sum = 0
        for i in range(TREES_PER_RUN):
            heights_sum += get_max_height(random_tree(n))

        mean: float = heights_sum / TREES_PER_RUN
        print(f"n: {n}, avg: {mean}")
        return mean

    x_coords: List[float] = [float(i/50*N_MAX) for i in range(1, 50)]
    y_coords: List[float] = [f_to_graph(round(x)) for x in x_coords]

    x_numpy: np.ndarray = np.array(x_coords)
    y_numpy: np.ndarray = np.array(y_coords)
    plt.plot(x_numpy, y_numpy, label="")
    plt.xlabel("Number of values in the tree")
    plt.ylabel("Average height of the tree")
    plt.title("Height of a random tree as a function of N")
    plt.grid(True)
    plt.legend()  # makes the 'label's show up
    plt.show()

def graph_2() -> None:
    def f_to_graph(n: int) -> float:
        times_sum = 0
        for i in range(TREES_PER_RUN):
            start: float = time.perf_counter()
            insert(random_tree(n), random.random())
            end: float = time.perf_counter()
            times_sum += end-start

        mean: float = times_sum / TREES_PER_RUN
        print(f"n: {n}, avg: {mean}")
        return mean

    x_coords: List[float] = [float(i/50*N_MAX) for i in range(1, 50)]
    y_coords: List[float] = [f_to_graph(round(x)) for x in x_coords]

    x_numpy: np.ndarray = np.array(x_coords)
    y_numpy: np.ndarray = np.array(y_coords)
    plt.plot(x_numpy, y_numpy, label="")
    plt.xlabel("Number of values in the tree")
    plt.ylabel("Time it takes to insert one random value")
    plt.title("Insert time as a function of N")
    plt.grid(True)
    plt.legend()  # makes the 'label's show up
    plt.show()

if __name__ == "__main__":
    graph_2()
