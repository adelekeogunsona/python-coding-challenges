#!/usr/bin/python3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_head = self.head
        self.head = new_node
        self.head.next = current_head
    
    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    
    def delete_at_head(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        next_node = self.head.next
        self.head = next_node
    
    def delete_at_tail(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        last_node = current_node

        current_node = self.head
        while current_node.next is not last_node:
            current_node = current_node.next
        current_node.next = None

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def display(self):
        all = []
        current_node = self.head
        while current_node is not None:
            all.append(current_node.data)
            current_node = current_node.next
        return all


# Test insert_at_head() method
linked_list = LinkedList()
linked_list.insert_at_head(1)
linked_list.insert_at_head(2)
assert linked_list.display() == [2, 1]

# Test insert_at_tail() method
linked_list2 = LinkedList()
linked_list2.insert_at_tail(1)
linked_list2.insert_at_tail(2)
assert linked_list2.display() == [1, 2]

# Test delete_at_head() and delete_at_tail() methods
linked_list3 = LinkedList()
linked_list3.insert_at_tail(1)
linked_list3.insert_at_tail(2)
linked_list3.delete_at_head()
linked_list3.delete_at_tail()
assert linked_list3.display() == []

# Test search
linked_list4 = LinkedList()
linked_list4.insert_at_head(5)
assert linked_list4.search(5) == True
assert linked_list4.search(1) == False
