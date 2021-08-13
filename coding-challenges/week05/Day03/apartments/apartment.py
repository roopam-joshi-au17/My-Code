from flat import Flat
class Apartment:
    def _init_(self,flats,builder_name,amneties,parking_spots,number_floors,maintenance_monthly,has_elevator,num_stairs,fire_safety):
        self.flats=flats
        self.builder_name=builder_name
        self.amneties=amneties
        self.parking_spots=parking_spots
        self.number_floors=number_floors
        self.maintenance_monthly=maintenance_monthly
        self.has_elevator=has_elevator
        self.num_stairs=num_stairs
        self.fire_safety=fire_safety
    def rent_flat(self):
        for item in self.flats:
            if item.current_renter==None:
                x=item.rent_out()
            if(self.has_elevator):
                x+=500
            if(self.fire_safety):
                x+=500
            for item in self.amneties:
                x+=500
            x+=self.maintenance_monthly
            return f"the monthly rent is {x}"
    def issue_parking_spot(self):
        if(self.parking_spots>0):
            print("parking spot issued")
            self.parking_spots-=1
    def revoke_parking_spot(self,flat):
        if(flat.has_parking_permission!=False):
            flat.has_parking_permission=False
            self.parking_spots+=1