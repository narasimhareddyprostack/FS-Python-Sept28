
from SA import SA
from CA import CA


def get_service(obj):
    print(obj.cal_bal())


get_service(SA(301, 'rajni', 'rajni@gmail.com', 'chennai', 8000))
get_service(CA(401, 'kamal', 'kamal@gmail.com', 'bangalore', 38000))
