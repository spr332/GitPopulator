import os
import random
import numpy as np

def didSomethingToday():
    #50% chance of committing a number on any given day
    return (random.randint(0,101) > 50)

def howManyToday():
    #Random amount of commits, can be zero
    return abs(int(np.random.normal(3,2)))
    
def main():
    days_ago=366
    os.system("git init")
    os.system("git add GitPopulator.py")
    os.system("git add README.md")
    os.system("git add requirements.txt")
    os.system("git add random.txt")
    os.system("git commit -m \"Initial Commit\"")
    for i in range(days_ago,1,-1):
        if didSomethingToday():
            for j in range(howManyToday()):
                file = open("random.txt", "w")
                file.write(str(random.randint(0,999999999)))
                file.close()
                os.system("git commit --date=\""+str(i)+" day ago\" -m \""+str(random.randint(0,999999999))+"\" -a")

if __name__ == "__main__":
    main()
