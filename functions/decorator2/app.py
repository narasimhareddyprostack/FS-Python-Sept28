def page_check(func):

    def inner(name,login):
        if login == False:
            print("Please Try to Login First")
        else:
            return func(name,login)

    return inner

def home_page(name,login):
    print("Home Page", name)

@page_check
def order_page(name,login):
    print("Order Page",name)

@page_check
def payment_page(name,login):
    print("payment page", name)


home_page("rahul", True)
order_page("rahul", True)
payment_page("rahul",False)