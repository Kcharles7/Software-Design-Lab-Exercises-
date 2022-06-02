import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        new_node.prev = last

        return

    def printList(self, a, node):
        while node:
            if (a == node):
                print("\033[4m" + node.data + "\033[0m", end="")
            else:
                print("{}".format(node.data), end="")
            last = node
            node = node.next

    def deleteNode(self, dele):

        if self.head is None or dele is None:
            return

        if self.head == dele:
            self.head = dele.next

        if dele.next is not None:
            dele.next.prev = dele.prev

        if dele.prev is not None:
            dele.prev.next = dele.next
        gc.collect()

    def moveF(self, a):
        if (a.next != None): a = a.next
        return a

    def moveB(self, a):
        if (a.prev != None): a = a.prev
        return a


listL = DoublyLinkedList()

s = str(input("Enter string: "))
for i in s:
    listL.append(i)
n = 1
a = listL.head
print("Your String: ", end="")
listL.printList(a, listL.head)
while (n != 0):
    m = int(
        input("\n\nEnter your choice:\n 1. Move Left\n 2. Move Right\n 3. Insert Character\n 4. Delete\n 5. exit\n"))
    if (m == 1):
        a = listL.moveB(a)
        print("Your String: ", end="")
        listL.printList(a, listL.head)
    elif (m == 2):
        a = listL.moveF(a)
        print("Your String: ", end="")
        listL.printList(a, listL.head)
    elif (m == 3):
        c = str(input("Enter Character which you want to insert: "))
        listL.insertAfter(a, c)
        print("Your String: ", end="")
        listL.printList(a, listL.head)
    elif (m == 4):
        listL.deleteNode(a)
        a = listL.moveF(a)
        print("Your String: ", end="")
        listL.printList(a, listL.head)
    elif (m == 5):
        n = 0
    else:
        print("wrong choice")
