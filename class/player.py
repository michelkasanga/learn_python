
class Player:

    def __init__(self):
        self.name:str|None= None
        self.level:int = 1
        self.score:int = 0
    
    def set_name(self, name:str):
        self.name = name

    def get_name(self)->str:
        return self.name
    
    def set_level(self, level:int):
        self.level = level

    def get_level(self)->int:
        return self.level
    
    def set_score(self, score:int):
        self.score = score
    
    def get_score(self)->int:
        return  self.score
    
    def level_up(self):
        self.level += 1
    
    def increase_score(self, point:int):
        self.score += point

    def __str__(self):
        return f"Name : {self.name} \nScore : {self.score} \nLevel : {self.level}"
    

if __name__ == "__main__":

    player = Player()
    player.set_name('michel')
    player.increase_score(100)
    player.level_up()
    print(player)

 
