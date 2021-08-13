from closet import Closet
from bed import Bed
class Bedroom:
    def __init__(self,length,breadth,height,has_balcony,has_window,num_lights,has_ac,has_fan,num_charging_points):
        self.length=length
        self.breadth=breadth
        self.height=height
        self.bed=None
        self.closet=None
        self.has_balcony=has_balcony
        self.has_window=has_window
        self.num_lights=num_lights
        self.has_ac=has_ac
        self.has_fan=has_fan
        self.num_charging_points=num_charging_points
    def carpet_area(self,length,breadth):
        return self.length*self.breadth
    def add_bed(self):
        l=int(input("enter length of bed"))
        b=int(input("enter breadth of bed"))
        y=int(input("enter year"))
        has_head=bool(input("has headboard?enter 0 or 1"))
        has_post=bool(input("has post?enter 0 or 1"))
        material=input("enter material")
        if(self.closet!=None and l*b<self.length*self.breadth-self.closet.length*self.closet.breadth):
            self.bed = Bed(l,b,y,has_head,has_post,material)
        elif(l*b<self.length*self.breadth):
            self.bed = Bed(l,b,y,has_head,has_post,material)
        else:
            return "no space"

    def add_closet(self):
        l=int(input("enter length of closet"))
        b=int(input("enter breadth of closet"))
        h=int(input("enter height of closet"))
        max_cap=int(input("enter maximum capacity of closet"))
        items=input("enter items in closet")
        items=items.split(" ")
        if(self.bed!=None and l*b<self.length*self.breadth-self.bed.length*self.bed.breadth):
            self.closet = Closet(l,b,y,has_head,has_post,material)
        elif(l*b<self.length*self.breadth):
            self.closet = Closet(l,b,y,has_head,has_post,material)
        
    def remove_bed(self):
        if self.bed==None:
            return "No bed found in room"
        self.bed=None
        return "bed removed from the room"
    def remove_closet(self):
        if self.closet==None:
            return "No closet found in room"
        self.closet=None
        return "closet removed from room"
    
    
