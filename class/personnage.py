
class Personnage:
    
    def __init__(self):
        self.name:str|None = None
        self.vie:int = 100

    def set_name(self, name:str):
        self.name = name

    def get_name(self)->str:
        return self.name
    
    def degats(self, degat:int):
        self.vie = max(0,self.vie - degat)

    def get_vie(self):
        return self.vie
