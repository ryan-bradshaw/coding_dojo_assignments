local_val = "magical unicorns"
def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

print(square(5))

user = User("Anna")
print(user.name)
print(user.say_hello())

if __name__ == "__main__":
    print("the file is being exectued directly")
else:
        print("the file is executed because it was imported by another file. The file is called : ", __name__)