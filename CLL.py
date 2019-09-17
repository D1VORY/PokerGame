class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


class CircularList:
    # Declaring head and tail pointer as null.
    def __init__(self):
        self.head = Node(None);
        self.tail = Node(None);
        self.head.next = self.tail;
        self.tail.next = self.head;
        self.start = None
        self.myList = []
        # This function will add the new node at the end of the list.

    def add(self, data):
        newNode = Node(data);
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = newNode;
            self.tail = newNode;
            newNode.next = self.head;
            self.start = self.head
            self.myList.append(self.head.data)
        else:
            # tail will point to new node.
            self.tail.next = newNode;
            # New node will become new tail.
            self.tail = newNode;
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head;
            self.myList.append(self.tail.data)
            # Displays all the nodes in the list


    def find(self,data):
        current = self.head
        if self.head is None:
            print("List is empty");
            return;
        else:
            while (current.next != self.head):
                current = current.next;
                if current.data == data:
                    return current
            return None

    def moveToNext(self):
        self.start = self.start.next


    def runTrhough(self , func):
        if self.head is None:
            print("List is empty");
            return;
        current = self.start
        while (current.next != self.start):
            func(current.data)
            current = current.next
        func(current.data)

        self.start = self.start.next
        return None


