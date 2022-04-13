def hello(name= 'Jose'):
    print("The hello() function has been executed")

    def greet():
        return '\t This is the greet() func inside hello!'
    print(greet())

    def welcome():
        return '\t This is welcome() inside hello'

    print("I am going to return a function!!")

    if name == "Jose":
        return greet
    else: 
        return welcome

my_new_func = hello('Jose')