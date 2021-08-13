class Kitchen:
    def __init__(self,length,breadth,slab_material,has_sink,has_slab,furnishing_material,lpg_pipeline):
        self.length=length
        self.breadth=breadth
        self.slab_material=slab_matyerial
        self.has_sink=has_sink
        self.has_slab=has_slab
        self.furnishing_material=furnishing_material
        self.lpg_pipeline=lpg_pipeline
    def cook(self):
        if(self.lpg_pipeline and self.has_sink and self.has_slab):
            return "kitchen can be used for cooking"
        return "kitchen unsuitable for cooking"