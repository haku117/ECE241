"""
UMass ECE 241 - Advanced Programming
Homework #3     Fall 2018
question1.py - Hashing with ordered list chaining

Only fill put() method in HashTable

In this question we are going to use the principles of Hash Table and Ordered link list. We will implement Hash Table by chaining. 
We have 1 list self.slots (which will store an OrderedList in each slot). 

Note: The nodes of the OrderedList have self.key and self.data 
For inserting a key, data pair in self.slots we use following rules: 

1. If position 'pos' of self.slots[pos] is None, we assign it with an OrderedList object and add a node with key, data to it. 

2. In the case of a collision (self.slots[pos] already an entry) the new value should be appended to the OrderedList. 

3. If the same key assigned a value again, the value is replaced:

"""
import sys


class Node:
    def __init__(self, init_key, init_data):
        self.key = init_key
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def getKey(self):
        return self.key

    def getNext(self):
        return self.next

    def setData(self,new_data):
        self.data = new_data

    def setKey(self,new_key):
        self.key = new_key

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        node_print = "[Key:{},Data:{}]".format(self.getKey(), self.getData())
        return str(node_print)


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, key):
        # searches and returns node with corresponding key
        current = self.head
        found = False
        stop = False
        found_node = None
        while (current is not None) and not found and not stop:
            if current.getKey() == key:
                found = True
                found_node = current
            else:
                if current.getKey() > key:
                    stop = True
                else:
                    current = current.getNext()

        return found_node

    def add(self, key, data):
        # adds a node with key and data to the list
        current = self.head
        previous = None
        stop = False
        while (current is not None) and not stop:
            if current.getKey() > key:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(key, data)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def __str__(self):
        print_list=""
        current = self.head
        while current is not None:
            node_print="[Key:{},Data:{}]".format(current.getKey(), current.getData())
            print_list += node_print
            print_list += "->"
            current = current.next

        print_list +="None"

        return str(print_list)


class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.occupied_slots = 0
        self.slots = [None] * self.size
        # self.data = [None] * self.size

    def put(self, key, data):
        """Only fill this function to put key, data in self.slot as per the question description"""

    def slot_size(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        return self.slots[hashvalue].size()

    def slot_content(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        return self.slots[hashvalue]

    def hashfunction(self, key, size):
        return key % size

    def get(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        key_node = self.slots[hashvalue].search(key)
        return key_node

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


# use this function to test your code (by instantiating objects and printing them)
def main():
    h = HashTable(11)
    h[1] = "grass"
    h[12] = "mass"
    print(h[1])
    h[2] = 14
    h[1] = 2
    print(h[1], h[2], h[12])
    print(h.slots)
    print(h.slot_size(1))
    print(h.slot_content(1))


if __name__ == '__main__':
    main()
