import random

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def getdata(self, i):
        if self.head is None:
            return 0
        itr =self.head
        while i!=0:
            itr = itr.next
            i=i-1
        return itr.data
        

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remall(self):
        flag=0
        itr = self.head
        while itr:
            self.head = self.head.next
            if self.head is None:
                break


    def remove(self, data):
        

        flag=0
        if self.head==None:
            print("linked list empty")
            return
        itr = self.head
        if itr.data==data:
            self.head = self.head.next
            return
        it = None
        while itr.data!=data:
            it = itr
            itr = itr.next
            if itr is None:
                flag=1
                break
        if flag==0:
            it.next=itr.next

    

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


def pr(ll, li):
    ll.print()
    ll.remove("mango")
    ll.print()
    global hh, a
    hh=li
    li.append("jak")
    a=0

def del(li):
    li=[]
    

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove("banana")
    li=[]
    for i in range(ll.get_length()):
        print(ll.getdata(i), " ")
        li.append(ll.getdata(i))
    pr(ll, li)
    ll.print()
    print(li)
    print(hh)
    arr=random.choices(li)
    print(arr)
    print(a)

    print(li)
    li = []
    print(li)
    ll.remall()
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
    print(ll.get_length())

