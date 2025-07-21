class Building:

    def __init__(self):
        self.adress:str|None = None
        self.level:int = 1

    def get_adress(self)->str:
        return self.adress
    
    def get_level(self)->int:
        return self.level
    
    def set_adress(self, adress:str):
        self.adress = adress

    def set_level(self, level:int):
        self.level = level