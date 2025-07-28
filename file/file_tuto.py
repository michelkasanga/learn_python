import os
import random
import shutil

"""food_list = ['apple', 'banana', 'cherry', 'date', 'elderberry'  ,]
with open('food.txt', 'w') as file:
    for food in food_list:
        file.write(food + 'n')
        
 
     
if  os.path.exists('food.txt'):
    with open('food.txt', 'r+') as file:
       # Move to the beginning of the file
        food_view = file.readlines()
        random_food = random.choice(food_view)
        print(random_food)
        file.seek(0)    """
        
source = 'food.txt' #chemi du ficher a copier
target = 'copie/food.txt' #chemi du ficher de destination

shutil.move(source, target) #copie le fichier source vers la destination
if  os.path.exists(target):
    with open(target, 'r+') as file:
       # Move to the beginning of the file
        food_view = file.readlines()
        random_food = random.choice(food_view)
        print(random_food)
        file.seek(0)   