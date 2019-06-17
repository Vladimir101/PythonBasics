# import the entire module
import greeting

print(dir(greeting))
print(type(greeting))

hello = greeting.Hello()
hello.sayHello("Vlad")

greeting.bye()