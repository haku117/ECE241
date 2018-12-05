"""
UMass ECE 241 - Advanced Programming
Homework #3     Fall 2018
question2.py

Find the shortest path between 2 nodes in a binary search tree.
Modify function _find_path() which is called from find_path().
Follow instructions in _find_path() method to return list_path and steps.

"""
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get_Node(self,key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def find_path(self, element_1_key, element_2_key):
        """This function calls _find_path()"""
        ### You can use the variables given here or define your own (to be used in _find_path()), below this line (line 123 till line 154)
        self.element_1 = self.get_Node(element_1_key) # Get the node corresponding to key
        self.element_2 = self.get_Node(element_2_key) # Get the node corresponding to key

        if (not self.element_1) or (not self.element_2):
            print("Keys Not present!!")
            return

        self.original_element_1_key = element_1_key # The end points (keys) of the path
        self.original_element_2_key = element_2_key # The end points (keys) of the path

        self.list_1 = [element_1_key] # List for path from key_1
        self.list_2 = [element_2_key] # List for path from key_2

        # To indicate which element is greater. To be used in constructing path
        if element_1_key < element_2_key:
            nature = 0
        elif element_1_key is element_2_key:
            print(self.list_1)
            return [self.list_1, 1]
        else:
            nature = 1

        self.stop = [0, 0]  # to stop traversing when you exceed limit or find common path
        # [1,0] to stop appending to path from element_1
        # [0,1] to stop appending to path from element_2
        # [1,1] found common path or exceeded limits

        self.node_in_list = [0,0] # to stop Recursion in _find_path() when self.list1, self.list2 are full

        self.steps = 0
    ### Above this line you can use the variables given here or define your own function (line 123 till line 154)

        # Don't change return
        return self._find_path(self.element_1, self.element_2, nature) # pass nodes and nature

    def _find_path(self, element_1, element_2, nature):
        """Fill in this function to get a path between element_1 and element_2:
        return: (check line 169 (commented return statement))
        list_path = [] which contains keys of the nodes in the path
        steps = int() which counts the number of nodes traversed in the path"""
        self.steps += 1
        # TODO: Fill in code
        # return [list_path, self.steps] # TODO: uncomment this line after filling this function

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


def main():
    mytree = BinarySearchTree()

    mytree[4] = "red"
    mytree[8] = "yellow"
    mytree[6] = "blue"
    mytree[3] = "pew"

    """Use this for testing and debugging your code"""
    # print(mytree[6])
    # print(mytree[2])

    # path_list_steps = mytree.find_path(3, 8)
    # print(path_list_steps[0], path_list_steps[1]) # this prints list_path, steps


if __name__ == "__main__":
    main()
