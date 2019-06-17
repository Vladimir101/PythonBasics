import greeting
# import specific functions
from greeting import bye, howdy

howdy()
bye()

hello = greeting.Hello()
hello.sayHello("Vlad")