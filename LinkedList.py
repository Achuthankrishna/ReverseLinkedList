from operator import truediv
from time import thread_time_ns
from tkinter import N


class node:
    def __init__(self,d,new=None,prev=None):
        self.data=d
        self.next=new
        self.prev=prev
    def __str__(self):
        return('(' +str(self.data)+')')
        
class LL:
    def __init__(self,r=None):
        self.root=r
        self.size=0
    def add(self,d):
        new_node=node(d,self.root)
        self.root=new_node
        self.size+=1
    def find(self,d):
        this_node=self.root
        while this_node is not None:
            if this_node.data==d:
                return d
            else:
                this_node=this_node.next
        return None
    def remove(self,d):
        this_node=self.root 
        prev_node=0
        while this_node is not None:
            if this_node==d:
                if prev_node!=0:
                    prev_node.next= this_node.next
                else:
                    self.root=this_node.next
                    self.size-=1
                return True
            else:
                prev_node=this_node
                this_node= this_node.next
            return False
    def reverse(self):
        this_node=self.root
        prev_node= None
        while this_node is not None:
            next = this_node.next
            this_node.next=prev_node
            prev_node = this_node
            this_node=next
        self.root=prev_node
        print("none")


    def print(self):
        this_node=self.root
        while this_node is not None:
            print(this_node, end="->")
            this_node=this_node.next
        print("none")
        

list=LL()
list.add(18)
list.add(20)
list.add(22)
list.print()
list.reverse()
list.print()
list.remove(20)
print(list.size)
print(list.find(7))
print(list.root)