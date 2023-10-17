cars=[{'model':'maruthi', 'brand':'swift', 'price':800000,'color':'white'},
{'model':'maruthi', 'brand':'swift', 'price':800000,'color':'blue'},
{'model':'RangeRover', 'brand':'velar', 'price':10000000,'color':'black'},
{'model':'maruthi', 'brand':'alto', 'price':200000,'color':'white'},
{'model':'tata', 'brand':'tiago', 'price':400000,'color':'blue'},
{'model':'kia', 'brand':'swift', 'price':4800000,'color':'yellow'},
{'model':'kai', 'brand':'swift', 'price':3800000,'color':'white'},
{'model':'mahindra', 'brand':'Xuv700', 'price':2800000,'color':'black'},
{'model':'mahindra', 'brand':'scorpio', 'price':1800000,'color':'black'}]


def filter_cars(car):
    if car['price']<1000000:
        return True 
    else:
        return False


below_10_cars=list(filter(filter_cars,cars))
print(below_10_cars)

""" 
white_cars = list(filter(lambda car: car['color'] == 'white', cars))
print(white_cars)

 """

#print all white colors cars -using lambda/with out lambda
""" print(type(cars[0]))
print(type(cars[1]))
print(type(cars[2]))
print(type(cars[3]))
print(type(cars[4]))
print(type(cars[5])) """
