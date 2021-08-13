from bedroom import Bedroom
from bathroom import Bathroom
from kitchen import Kitchen
class Flat:
    def _init_(self,bed_rooms,bath_rooms,kitchens,owner_name,current_renter,has_parking_permission):
        self.bed_rooms=[]
        self.bath_rooms=[]
        self.kitchens=[]
        self.owner_name=None
        self.current_renter=None
        self.has_parking_permission=False
    def rent_out(self):
        if(current_renter==None):
            carpet_area=0
            for item in self.bed_rooms:
                carpet_area+=item.length*item.breadth
            for item in self.bath_rooms:
                carpet_area+=item.length*item.breadth
            for item in self.kitchens:
                carpet_area+=item.length*item.breadth
            print(f"the rent of house is {carpet_area*5} per month")
            x=input("Do you agree to pay this rent?Y/N")
            if x=="Y":
                renter_name=input("enter your name")
                self.current_renter=renter_name
            return carpet_area*5
    def change_owner(self):
        name=input("enter owner name")
        self.owner_name=name