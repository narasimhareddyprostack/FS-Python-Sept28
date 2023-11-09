from Programmer import Programmer
from HR import HR
def get_service(obj):
    print(obj.cal_leaves())

get_service(Programmer("Arjun",12,"APPdeveloper", 6, 4))
get_service(HR("Shrushti", 25, "Marketing", 8, 7))