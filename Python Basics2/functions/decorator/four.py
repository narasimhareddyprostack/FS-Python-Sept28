def user_uppercase(func):

    def inner():
        msg = func()
        return msg.upper()


    return inner

@user_uppercase
def print_user():
    return "Hi, Rahul Gandhi"


print(print_user())