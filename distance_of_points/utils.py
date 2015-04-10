from random import randint

list_of_coord = []
single_coord = ()

def random_coord(quantity=8):
    """
    generate the random coordinates
    change the "quantity" value to generate that much tuple. 
    """
    if quantity <= 0:
        return (0,0) #  recursion end
    
    for i in range(2):
        if i == 0:
            x = randint(-10,10) # change this number to get broader number of coord
        else:
            y = randint(-10,10) # change this number to get broader number of coord
    
    single_coord = (x,y)
    list_of_coord.append(single_coord)
    random_coord(quantity-1) # recursion call

def generate_coordinates():
    random_coord()
    return list_of_coord
