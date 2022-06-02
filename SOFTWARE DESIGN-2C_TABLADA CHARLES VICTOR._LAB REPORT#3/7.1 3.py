import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def SecondLastNode(head):
    temp = head

    if (temp == None or temp.next == None):
        return -1


    while (temp != None):


        if (temp.next.next == None):
            return temp.data


        temp = temp.next


def push(head, new_data):
    new_node = Node(new_data)

    new_node.next = head
    head = new_node
    return head



if __name__ == '__main__':
    head = None


    head = push(head, 15)
    head = push(head, 27)
    head = push(head, 12)
    head = push(head, 19)
    head = push(head, 8)

    print(SecondLastNode(head))