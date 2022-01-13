class Node:
    def __init__(self, data=None, next= None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def length_of_dll(self):
        count= 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return (count)

    def print_dll(self):
        if self.head == None:
            print("Linked List is Empty")

        itr= self.head
        linked_list = ''
        while itr:
            linked_list += str(itr.data) + " "
            itr = itr.next

        print(linked_list)

    def print_reverse_dll(self):
        if self.head == None:
            print("Linked List is Empty")

        itr= self.tail
        linked_list = ''
        while itr:
            linked_list += str(itr.data) + " "
            itr = itr.prev

        print(linked_list)


    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head == None:  #linked list is empty  
            self.head = node
            self.tail = node

        itr= self.head
        node.next = self.head
        itr.prev = node
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        itr = self.tail
        node.prev = self.tail
        itr.next = node
        self.tail = node

    def insert_at_index(self,data, index):
        if index<0 or index>=self.length_of_dll():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_beginning(data)
            return 

        count =0
        itr = self.head
        while itr:
            if count== index-1:
                node = Node(data, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                
                break
            itr = itr.next
            count += 1

    def delete_beginning(self):
        itr = self.head
        itr.next.prev = None
        self.head = self.head.next
        
    def delete_end(self):
        itr = self.tail
        itr.prev.next = None
        self.tail = self.tail.prev

    def delete_at_index(self, index):
        if index<0 or index>=self.length_of_dll():
            raise Exception("Invalid Index")

        if index==0:
            self.delete_beginning()
            return
        
        count=0
        itr= self.head
        while itr:
            if count == index-1:
                
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            itr = itr.next
            count+=1



    

if __name__ == '__main__':
    ll = Doubly_Linked_List()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(9)
    ll.insert_at_end(3)
    ll.print_dll()
    ll.delete_beginning()
    ll.print_dll()
    ll.insert_at_end(8)
    ll.insert_at_index(9,2)
    ll.print_dll()
    ll.print_reverse_dll()
    ll.delete_end()
    ll.print_dll()
    ll.delete_at_index(1)
    ll.print_dll()
    print(ll.length_of_dll())