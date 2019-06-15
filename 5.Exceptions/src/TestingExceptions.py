# change i from 1 to 4
import sys
i = 1
j = 0
try:
    if (i == 1):
        print(str(i / j))
    elif (i == 2):
        words = ["Python", "is", "a", "programming", "language"]
        word = words[5]
    elif (i == 3):
        string = "abc"
        ind = string.index("f")
    else:
        print("Ending the try block.")
# except ZeroDivisionError:
#     print("ZeroDivision error:", "j =", str(j))
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except:
    print("Serious problem")
    print("Unexpected error:", sys.exc_info()[0])