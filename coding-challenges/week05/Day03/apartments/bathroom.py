class Bathroom:
    def __init__(self,length,breadth,has_sink,has_bathtub,has_tap,has_shower):
        self.length=length
        self.breadth=breadth
        self.has_sink=has_sink
        self.has_bathtub=has_bathtub
        self.has_tap=has_tap
        self.has_shower=has_shower
    def bathing(self):
        if(has_sink or has_tap or has_shower):
            return "suitable for bathing"
        return "unsuitable for bathing"