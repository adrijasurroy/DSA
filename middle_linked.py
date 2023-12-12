# Problem Statement: Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

# Examples:

# Input Format: 
# ( Pointer / Access to the head of a Linked list )
# head = [1,2,3,4,5]

# Result: [3,4,5]
# ( As we will return the middle of Linked list the further linked list will be still available )

# Explanation: The middle node of the list is node 3 as in the below image.

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class Sol:
    def middle(head: Node)->Node:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    headl = [1,2,3,4,5]
    # list = [Node((i)) for i in head ]
    head = None
    for i in headl:
        n = Node(i)
        if head == None:
            head = n
            continue
        
        temp = head
        while temp.next != None:
            temp=temp.next       
        temp.next = n
            
    mid = middle(head)
    print("mid", mid.val)