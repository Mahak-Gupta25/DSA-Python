class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def length_of_ll(self):
        count= 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return (count) 

    def print_ll(self):
        if self.head == None:
            print("Linked List is Empty")

        itr= self.head
        linked_list = ''
        while itr:
            linked_list += str(itr.data) + " "
            itr = itr.next

        print(linked_list)

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        if self.head== None:
            self.head = node
            return 

        itr = self.head
        while itr.next != None:
            itr = itr.next

        itr.next = node

    def insert_at_index(self,data, index):
        if index<0 or index>=self.length_of_ll():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_beginning(data)
            return 

        count =0
        itr = self.head
        while itr:
            if count== index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


    def insert_data_list_at_end(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

        return


    def delete_beginning(self):
        self.head = self.head.next

    def delete_at_end(self):
        itr = self.head
        while itr.next.next != None:
            itr = itr.next

        itr.next = None
        return

    def delete_at_index(self, index):
        if index<0 or index>=self.length_of_ll():
            raise Exception("Invalid Index")

        if index==0:
            self.delete_beginning()
            return
        
        count=0
        itr= self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_beginning(5)
    ll.print_ll()
    ll.insert_beginning(2)
    ll.print_ll()
    ll.insert_end(6)
    ll.print_ll()
    ll.insert_at_index(8, 2)
    ll.print_ll()
    ll.delete_beginning()
    ll.print_ll()
    ll.delete_at_end()
    ll.print_ll()
    ll.delete_at_index(1)
    ll.print_ll()
    print(ll.length_of_ll())