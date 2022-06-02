class Node(object):
    def __init__(self, data = None, next_node = None ):
        self.data = data
        self.next = next_node
def MergeLists (headL, headM):
    head = tail = Node(' ',None)
    while headL or headM:
        if headL is not None:
            if (headL and headL.data <= headM.data) or (headM is None):
                tail.next = headL
                tail = headL
                headL = headL.next
        if headM is not None:
            if ( headL and headM.data <= headL.data) or (headL is None):
                tail.next = headM
                tail = headM
                headM = headM.next
    return head.next

