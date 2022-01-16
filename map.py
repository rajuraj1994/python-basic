# the map function allows you to  'map' a  function to an iterable object.This means yo can call the same function to every item in an iterable  such as list.
def square(num):
    return num**2

my_num=[1,2,3,4,5]
a=map(square,my_num)
print(a)

x=list(map(square,my_num))
print(x)

def splicer(mytext):
    if len(mytext)%2==0:
        return 'even'
    else:
        return mytext[0]

mynames=['ramesh','raghu','sudip','ashim','spriha','bindu','gaurav','sanjay','sanjeev']
abc=list(map(splicer,mynames))
print(abc)

