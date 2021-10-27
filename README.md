# Merkle-Tree
In cryptography and computer science, a hash tree or Merkle tree is a tree in which every leaf node is labelled with the cryptographic hash of a data block, and every non-leaf node is labelled with the cryptographic hash of the labels of its child nodes.
Hash trees allow efficient and secure verification of the contents of large data structures. Hash trees are a generalization of hash lists and hash chains.

In this code, we implement a Merkle Tree and show how it works using Python. A hash is created and then divided into blocks. The algorithm iterates through these blocks until there is only one
hash left, which is the Merkle root.
