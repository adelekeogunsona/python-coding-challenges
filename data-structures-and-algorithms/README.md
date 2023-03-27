## Challenge 1

__Two Sum__

Given an array of integers, return the indices of the two numbers that add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Function signature:
```
def two_sum(nums: Array[int], target: int) -> Array[int]:
```

Test case 1:
```
nums = [2, 7, 11, 15]
target = 9
assert two_sum(nums, target) == array('i', [0, 1])
```

Test case 2:
```
nums = [3, 2, 4]
target = 6
assert two_sum(nums, target) == array('i', [1, 2])
```

Test case 3:
```
nums = [0, 4, 3, 0]
target = 0
assert two_sum(nums, target) == array('i', [0, 3])
```

Test case 4:
```
nums = []
target = 8
assert two_sum(nums, target) == array('i')
```

## Challenge 2

__Linked List__

Create a class called LinkedList which implements a singly linked list. The class should have the following methods:

```
__init__: Initializes an empty linked list.

insert_at_head: Inserts a new node at the head of the linked list.

insert_at_tail: Inserts a new node at the tail of the linked list.

delete_at_head: Deletes the node at the head of the linked list.

delete_at_tail: Deletes the node at the tail of the linked list.

search: Searches for a node with a given value in the linked list.

display: Displays the linked list.
```

Each node in the linked list should have two attributes:
```
data: The value stored in the node.

next: A reference to the next node in the linked list.
```

Test Cases
```
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
```

