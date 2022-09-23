import os, random
droga = random.choice([x for x in os.listdir("J:\\") if os.path.isfile(os.path.join("J:\\", x))])

print(droga)