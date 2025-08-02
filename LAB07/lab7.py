import random
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def get_balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right
    
    x.right = y
    y.left = T2
    
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    
    y.left = x
    x.right = T2
    
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    
    return y

def insert_node(root, key):
    if not root:
        return TreeNode(key)
        
    if key < root.key:
        root.left = insert_node(root.left, key)
    elif key > root.key:
        root.right = insert_node(root.right, key)
    else:
        return root
        
    root.height = 1 + max(height(root.left), height(root.right))
    
    balance = get_balance_factor(root)
    
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
        
    return root

# Analysis functions
def generate_random_sequence(size=20):
    return random.sample(range(1, size + 1), size)

def build_bst(sequence):
    root = None
    for num in sequence:
        if not root:
            root = Node(num)
        else:
            root = insert_node(root, num)
    return root

def build_avl(sequence):
    root = None
    for num in sequence:
        root = insert_node(root, num)
    return root

def get_tree_stats(tree):
    return {
        'height': height(tree),
        'imbalance': abs(get_balance_factor(tree))
    }

num_trials = 1000
stats = defaultdict(list)

for _ in range(num_trials):
    sequence = generate_random_sequence(20)
    bst_root = build_bst(sequence)
    avl_root = build_avl(sequence)
    
    bst_stats = get_tree_stats(bst_root)
    avl_stats = get_tree_stats(avl_root)
    
    stats['bst_height'].append(bst_stats['height'])
    stats['avl_height'].append(avl_stats['height'])
    stats['bst_imbalance'].append(bst_stats['imbalance'])

print("\nSummary Statistics ({num_trials} trials):")
print("\nBST Statistics:")
print(f"Average Height: {np.mean(stats['bst_height']):.2f}")
print(f"Max Height: {max(stats['bst_height'])}")
print(f"Min Height: {min(stats['bst_height'])}")

print("\nAVL Statistics:")
print(f"Average Height: {np.mean(stats['avl_height']):.2f}")
print(f"Max Height: {max(stats['avl_height'])}")
print(f"Min Height: {min(stats['avl_height'])}")

print("\nBST Imbalance Statistics:")
print(f"Average Imbalance: {np.mean(stats['bst_imbalance']):.2f}")
print(f"Max Imbalance: {max(stats['bst_imbalance'])}")

most_imbalanced_idx = np.argmax(stats['bst_imbalance'])
sequence = generate_random_sequence(20)
bst_root = build_bst(sequence)
print(f"\nMost Imbalanced Tree Example:")
print(f"Sequence: {sequence}")
print(f"Height: {height(bst_root)}")
print(f"Balance Factor: {get_balance_factor(bst_root)}")

plt.figure(figsize=(12, 5))

plt.subplot(121)
plt.hist(stats['bst_height'], bins=range(min(stats['bst_height']), max(stats['bst_height']) + 2, 1))
plt.title('Distribution of BST Heights')
plt.xlabel('Tree Height')
plt.ylabel('Frequency')

plt.subplot(122)
plt.hist(stats['bst_imbalance'], bins=30)
plt.title('Distribution of BST Imbalances')
plt.xlabel('Absolute Balance Factor')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('tree_analysis.png')