# pip,env => pip install package

# inbuilt libraries
# 1.math
import math
print(math.sqrt(16))    
print(math.pow(2, 3))   
print(math.pi)          






# 2.random
import random
print(random.randint(1,100))
print(random.choice(["A","B","C"]))






# 3.datetime
import datetime
today = datetime.date.today()
print("Today is:",today)
now = datetime.datetime.now()
print("Current time:",now)






# 4.OS
import os
print(os.getcwd())
os.mkdir("new_folder")
os.rename("old.txt","new.txt")