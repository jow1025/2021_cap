fire=False

def a():
    global fire
    fire=True
    
def b():
    global fire
    fire=False
    
print(fire)
a()
print(fire)
b()
print(fire)