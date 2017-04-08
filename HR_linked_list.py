#The following functions correspond to the Linked List problems from the data
#structures subsection of HackerRank challenges. Solutions by Dan March.

#The functions use the following Node object:

 # class Node(object):
 #
 #   def __init__(self, data=None, next_node=None):
 #       self.data = data
 #       self.next = next_node

def print_list(head):
    """Prints the elements of a linked list in forward order.
    @param head: The head node of the linked list."""
    while head != None:
        print(head.data)
        head = head.next

def Insert(head, data):
    """Inserts a node at the end of a linked list.
    @param head: The head node of the linked list.
    @param data: The data containted by the inserted node."""
    inserted_node = Node(data)
    if head == None:
        return inserted_node
    pointer = head
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = inserted_node
    return head

def Insert(head, data):
    """Inserts a node at the front of a linked list.
    @param head: The head node of the linked list.
    @param data: The data containted by the inserted node."""
    return Node(data,head)

def InsertNth(head, data, position):
    if head == None:
        return Node(data)
    elif position == 0:
        return Node(data,head)
    else:
        inserted_node = Node(data)
        pointer = head
        for _ in range(position-1):
            pointer = pointer.next
        saved_elm = pointer.next
        pointer.next = inserted_node
        inserted_node.next = saved_elm
        return head

def Delete(head, position):
    """Deletes a node in a linked list at an input location.
    @param head: The head node of the linked list.
    @param position: The index of the node being deleted."""
    if position == 0:
        return head.next
    pointer = head
    for _ in range(position-1):
        pointer = pointer.next
    pointer.next = pointer.next.next
    return head

def Reverse(head):
    """Reverses a linked list.
    @param head: The head node of the linked list."""
    pointer = head
    prev, next_elm = None, None
    while pointer.next != None:
        next_elm = pointer.next
        pointer.next = prev
        prev = pointer
        pointer = next_elm
    pointer.next = prev
    return pointer

def ReversePrint(head):
    """Prints the elements of a linked list in reverse order. NOTE: relies on
    the Reverse(head) function implemented above.
    @param head: The head node of the linked list."""
    if head == None:
        return head
    head = Reverse(head)
    while head != None:
        print(head.data)
        head = head.next

def CompareLists(headA, headB):
    """Determines whether or not two linked lists are identical.
    @param headA: The head node of the first linked list.
    @param headB: The head node of the second linked list.
    @return: 0 for non-equality, 1 for equality."""
    while headA != None and headB != None:
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    if headA == None and headB == None:
        return 1
    return 0

def MergeLists(headA, headB):
    """Merges two sorted linked lists.
    @param headA: The head node of the first sorted linked list.
    @param headB: The head node of the second sorted linked list."""
    if headA == None:
        return headB
    elif headB == None:
        return headA
    else:
        if headA.data <= headB.data:
            pointer = headA
        else:
            temp = headA
            headA = headB
            headB = temp
            pointer = headA
        while headA.next != None:
            if headB.data < headA.next.data:
                temp = headA.next
                headA.next = headB
                headB = temp
            headA = headA.next
        if headB != None:
            headA.next = headB
        return pointer

def GetNode(head, position):
    """Gets the data from the node at the 'position'th index from the end of
    the linked list.
    @param head: The head node of the linked list.
    @param position: The index of the desired node starting from the end."""
    length = 0
    pointer1, pointer2 = head, head
    while pointer1 != None:
        length += 1
        pointer1 = pointer1.next
    for _ in range(length-position-1):
        pointer2 = pointer2.next
    return pointer2.data

def RemoveDuplicates(head):
    """Removes repeated elements from a linked list so that each node in the
    list appears only one time.
    @param head: The head node of the linked list."""
    seen_set = set()
    pointer = head
    seen_set.add(pointer.data)
    while pointer.next != None:
        if pointer.next.data not in seen_set:
            seen_set.add(pointer.next.data)
            pointer = pointer.next
        else:
            pointer.next = pointer.next.next
    return head

def has_cycle(head):
    """Determines whether or not a linked list has a cycle.
    @param head: The head node for the linked list.
    @return: 0 for non-cyclic, 1 for cyclic."""
    pointer1, pointer2 = head, head
    while pointer1.next != None and pointer2.next != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
        if pointer1 == pointer2:
            return 1
    return 0

def FindMergeNode(headA, headB):
    """Finds the node where two intersecting linked lists meet.
    @param headA: The head node of the first linked list.
    @param headB: The head node of the second linked list.
    @return: The data at the intersection node."""
    #Find which list is longer and make it a circlularly linked list
    lengthA,lengthB = 1,1
    pointerA, pointerB = headA, headA
    while pointerA.next != None:
        lengthA += 1
        pointerA = pointerA.next
    while pointerB.next != None:
        lengthB += 1
        pointerB = pointerB.next
    if lengthB <= lengthA:
        pointerA.next = headA
        pointerA, pointerB = headB, headB
    else:
        pointerB.next = headB
        pointerA, pointerB = headA, headA

    #Run the cycle detection algorithm to find the insertection node
    while pointerA.next != None and pointerB.next != None:
        pointerA = pointerA.next
        pointerB = pointerB.next.next
        if pointerA == pointerB:
            intersection_node = pointerA
            break

    #Increment a pointer starting at the beginning of the shorter list
    #until it hits the pointer in the loop. This is the intersection point.
    if lengthB <= lengthA:
        pointerA = headB
    else:
        pointerA = headA
    while pointerA != pointerB:
        pointerA = pointerA.next
        pointerB = pointerB.next
    return pointerA.data

#The last function uses the doubly linked node object:

 # class Node(object):
 #
 #   def __init__(self, data=None, next_node=None, prev_node = None):
 #       self.data = data
 #       self.next = next_node
 #       self.prev = prev_node

 def SortedInsert(head, data):
     """Inserts an element with the provided data into a doubly linked list
     in order to preserve sorted order.
     @param head: The head node of the doubly linked list.
     @param data: The data for the inserted node"""
    if head.next == None and head.prev == None:
        inserted_node = Node(data)
        head.next = inserted_node
        return head
    elif data <= head.next.data:
        temp = head.next
        inserted_node = Node(data,temp)
        inserted_node.next.prev = inserted_node
        head.next = inserted_node
        return head
    else:
        inserted_node = Node(data)
        pointer = head
        while pointer.next != None and pointer.next.data <= data:
            pointer = pointer.next
        temp = pointer.next
        inserted_node.prev = pointer
        inserted_node.next = temp
        pointer.next = inserted_node
        if temp != None:
            pointer.next.next.prev = inserted_node
        return head
