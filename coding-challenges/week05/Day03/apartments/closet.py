class Closet:
    def __init__(self,length,breadth,height,max_capacity,items):
        self.length=length
        self.breadth=breadth
        self.height=height
        self.max_capacity=max_capacity
        self.items=items
    def store_item(self,item):
        if (len(self.items)<self.max_capacity):
            self.items.append(item)
    def fetch_item(self):
        return self.items[0]