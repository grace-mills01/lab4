import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**9)
from bst import *


def alpha_before(a: str, b: str) -> bool:
    return a < b


def reverse_int_before(a: int, b: int) -> bool:
    return a > b  # 10 "comes before" 9 in reverse order


@dataclass
class Point2D:
    x: float
    y: float


def dist_before(a: Point2D, b: Point2D) -> bool:
    return (a.x**2 + a.y**2) < (b.x**2 + b.y**2)


class BSTTests(unittest.TestCase):

    def test_string_lookup_present(self):
        bst = BinarySearchTree(alpha_before, None)
        bst = insert(bst, "banana")
        bst = insert(bst, "apple")
        bst = insert(bst, "cherry")
        self.assertTrue(lookup(bst, "apple"))
        self.assertTrue(lookup(bst, "cherry"))

    def test_string_lookup_absent(self):
        bst = BinarySearchTree(alpha_before, None)
        bst = insert(bst, "banana")
        self.assertFalse(lookup(bst, "grape"))

    def test_string_no_duplicates(self):
        bst = BinarySearchTree(alpha_before, None)
        bst = insert(bst, "apple")
        bst = insert(bst, "apple")
        # tree should only have one node
        self.assertEqual(bst.binTree.left, None)
        self.assertEqual(bst.binTree.right, None)

    def test_string_delete(self):
        bst = BinarySearchTree(alpha_before, None)
        bst = insert(bst, "banana")
        bst = insert(bst, "apple")
        bst = insert(bst, "cherry")
        bst = delete(bst, "banana")
        self.assertFalse(lookup(bst, "banana"))
        self.assertTrue(lookup(bst, "apple"))
        self.assertTrue(lookup(bst, "cherry"))

    def test_string_delete_absent(self):
        bst = BinarySearchTree(alpha_before, None)
        bst = insert(bst, "apple")
        bst = delete(bst, "grape")  # should not crash
        self.assertTrue(lookup(bst, "apple"))

    # --- Point2D tests ---

    def test_point_lookup_present(self):
        bst = BinarySearchTree(dist_before, None)
        p1 = Point2D(1, 0)  # dist 1
        p2 = Point2D(3, 4)  # dist 5
        p3 = Point2D(0, 2)  # dist 2
        bst = insert(bst, p1)
        bst = insert(bst, p2)
        bst = insert(bst, p3)
        self.assertTrue(lookup(bst, p2))
        self.assertTrue(lookup(bst, p3))

    def test_point_lookup_absent(self):
        bst = BinarySearchTree(dist_before, None)
        bst = insert(bst, Point2D(1, 0))
        self.assertFalse(lookup(bst, Point2D(3, 4)))

    def test_point_delete(self):
        bst = BinarySearchTree(dist_before, None)
        p1 = Point2D(1, 0)
        p2 = Point2D(3, 4)
        bst = insert(bst, p1)
        bst = insert(bst, p2)
        bst = delete(bst, p1)
        self.assertFalse(lookup(bst, p1))
        self.assertTrue(lookup(bst, p2))

    # --- Reverse integer tests ---

    def test_reverse_int_lookup_present(self):
        bst = BinarySearchTree(reverse_int_before, None)
        bst = insert(bst, 10)
        bst = insert(bst, 9)
        bst = insert(bst, 5)
        self.assertTrue(lookup(bst, 10))
        self.assertTrue(lookup(bst, 5))

    def test_reverse_int_lookup_absent(self):
        bst = BinarySearchTree(reverse_int_before, None)
        bst = insert(bst, 10)
        self.assertFalse(lookup(bst, 3))

    def test_reverse_int_order(self):
        # 10 comes before 9 in reverse order, so 10 should be root, 9 to the right
        bst = BinarySearchTree(reverse_int_before, None)
        bst = insert(bst, 10)
        bst = insert(bst, 9)
        self.assertEqual(bst.binTree.value, 10)
        self.assertEqual(bst.binTree.right.value, 9)

    def test_reverse_int_delete(self):
        bst = BinarySearchTree(reverse_int_before, None)
        bst = insert(bst, 10)
        bst = insert(bst, 9)
        bst = insert(bst, 5)
        bst = delete(bst, 9)
        self.assertFalse(lookup(bst, 9))
        self.assertTrue(lookup(bst, 10))
        self.assertTrue(lookup(bst, 5))

    def test_empty_lookup(self):
        bst = BinarySearchTree(reverse_int_before, None)
        self.assertFalse(lookup(bst, 1))

    def test_empty_delete(self):
        bst = BinarySearchTree(reverse_int_before, None)
        bst = delete(bst, 1)  # should not crash
        self.assertFalse(lookup(bst, 1))


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
