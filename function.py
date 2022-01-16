# function -> a block of code to perform a particular task.A function is reusable
# a function is always define using def keyword
# calling a function with this ()

#define the function
def demo():
    print('hello world')

#call the function
demo()

# accepting parameters/arguments

#define the function
def people_name(name):
    print(f'Hello {name}')
    # print('hello'+name)

#call the function with parameters
people_name('Raghu')

#return type

#define
def add(x,y):
    return x+y

#call the function
abc=add(5,2)
print(abc)


