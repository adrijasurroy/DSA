# Problem Statement: Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list instead, you will be given access to the node to be deleted directly. It is guaranteed that the node to be deleted is not a tail node in the list.

# Examples:

# Example 1:
# Input:
#  Linked list: [1,4,2,3]
#        Node = 2
# Output:
# Linked list: [1,4,3]
# Explanation: Access is given to node 2. After deleting nodes, the linked list will be modified to [1,4,3].

# Example 2:
# Input:
#  Linked list: [1,2,3,4]
#        Node = 1
# Output: Linked list: [2,3,4]
# Explanation:
#  Access is given to node 1. After deleting nodes, the linked list will be modified to [2,3,4].

class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        
    
class LinkedList:
    def insert(head: Node, data : int)->Node:
        n=Node(data)
        if head == None:
            head=n
            return head
        
        temp=head
        while temp.next != None:
            temp=temp.next       
        temp.next = n
        return head
    
    def getNode(head: Node, val: int)-> Node:
        while head.next != val:
            head=head.next 
            
        return head
    
    def delNode(t: Node)->Node:
        t.val = t.next.val
        t.next = t.next.next
        return t
    
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
    temp = insert(head, 8)        
    mid = temp
    print(mid.val)
    while mid.next!=None:
        mid = mid.next
        print(mid.val)
    
    # print(mid.val )
        