'''
Created on Jun 16, 2019

@author: vladi
'''
class Hello:
    def sayHello(self, name):
        print("Hello, {}".format(name))

def bye():
    print("Bye, bye")

def howdy():
    print("Howdy, pal!")
    
# This condition is true if the program runs directly
# It's false if the file is imported as a module   
if __name__ == '__main__':
    print("You ran this program directly")