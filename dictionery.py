# similar to object from other programming language
# dict={'key1':'value1','key2':'value2'}

student={'name':'bindu','age':20,'height':5.5,'gender':'female'}
print(student['name'])
print(student['name'].upper())

student={'name':'bindu','age':20,'gender':'female','subject':['python','django','restapi','react','next']}
print(student['subject'])
print(student['subject'][0])

#nesting with dictionaries
x={'key1':{'nestkey':{'subnestkey':'value'}}}
print(x['key1']['nestkey']['subnestkey'])

#print all the keys
print(student.keys())

#print all the values
print(student.values())

#method to return tuples of all items
print(student.items())


