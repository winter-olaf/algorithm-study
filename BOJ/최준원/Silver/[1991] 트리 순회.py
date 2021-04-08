class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    print(tree[node].val, end="")
    if tree[node].left != '.':
        preorder(tree[node].left)
    if tree[node].right != '.':
        preorder(tree[node].right)

def inorder(node):
    if tree[node].left != '.':
        inorder(tree[node].left)
    print(tree[node].val, end="")
    if tree[node].right != '.':
        inorder(tree[node].right)

def postorder(node):
    if tree[node].left != '.':
        postorder(tree[node].left)
    if tree[node].right != '.':
        postorder(tree[node].right)
    print(tree[node].val, end="")

import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = {}

for i in range(N):
    val, l, r = input().split()
    tree[val] = Node(val, l, r)

preorder('A')
print()
inorder('A')
print()
postorder('A')