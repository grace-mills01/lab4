import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**9)


comes_before: TypeAlias = Callable[[Any, Any], bool]
BinTree: TypeAlias = Union["Node", None]


@dataclass
class Node:
    value: Any
    left: BinTree
    right: BinTree


@dataclass
class BinarySearchTree:
    fn: comes_before
    binTree: BinTree


# searches through bin tree from bst
def lookup_helper(bintree: BinTree, val: Any, fn: comes_before) -> bool:
    match bintree:
        case None:
            return False
        case Node(v, left, right):
            if not fn(v, val) and not fn(val, v):  # equal
                return True
            elif fn(val, v):  # val comes before v, go left
                return lookup_helper(left, val, fn)
            else:  # go right
                return lookup_helper(right, val, fn)


# finds if a given value is in a given bst, returns True if present and False otherwise
def lookup(bst: BinarySearchTree, val: Any) -> bool:
    return lookup_helper(bst.binTree, val, bst.fn)


# handles recursive logic of insert
def insert_helper(bins: BinTree, val: Any, fn: comes_before) -> Optional[BinTree]:
    match bins:
        case None:  # empty
            return Node(val, None, None)
        case Node(v, l, r):
            if not fn(v, val) and not fn(
                val, v
            ):  # equal, so value already excists in bst and doesn't need to be added
                return None
            elif fn(val, v):  # val comes before v, go left
                return Node(v, insert_helper(l, val, fn), r)
            else:  # go right
                return Node(v, l, insert_helper(r, val, fn))


# inserts a given value into a bst and returns the new bst
def insert(bst: BinarySearchTree, val: Any) -> BinarySearchTree:
    if insert_helper(bst.binTree, val, bst.fn) == None:
        return bst
    else:
        return BinarySearchTree(bst.fn, insert_helper(bst.binTree, val, bst.fn))


# find minimum on right to move up
def get_min(bintree: BinTree) -> Any:
    match bintree:
        case Node(v, None, right):
            return v
        case Node(v, left, right):
            return get_min(left)


# recursivly goes through bin tree of bst passed into delete to find val and delete it
def delete_helper(bintree: BinTree, val: Any, fn: comes_before) -> BinTree:
    match bintree:
        case None:
            return None
        case Node(v, left, right):
            if not fn(v, val) and not fn(val, v):  # found it
                match (left, right):
                    case (None, None):  # leaf
                        return None
                    case (None, _):  # only right child
                        return right
                    case (_, None):  # only left child
                        return left
                    case _:  # two children: replace with in-order successor
                        successor = get_min(right)
                        return Node(
                            successor, left, delete_helper(right, successor, fn)
                        )
            elif fn(val, v):  # go left
                return Node(v, delete_helper(left, val, fn), right)
            else:  # go right
                return Node(v, left, delete_helper(right, val, fn))


# removes the wanted value from a bst
def delete(bst: BinarySearchTree, val: Any) -> BinarySearchTree:
    return BinarySearchTree(bst.fn, delete_helper(bst.binTree, val, bst.fn))
