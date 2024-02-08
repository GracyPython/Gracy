
# Data types
num=4
num1=2.5
num2='abcd'
print(num,num1,num2)

num=2,3.4,'xyz'
print(num)

#diff types of  defining string

str='abcde'
print(str)

str="welcome to my world"
print(str)

str='''this is the first program i wrote
     welcome to this first program
     Hope this looks good'''
print(str)

#length of a string

str="welcome to my world"
len=len(str)
print(len)

# dictnories different types

names={
    'sunny':'10',
    'Gracy':'20',
    'nithu':'30',
}
print(names)

keys = names.keys()
print(keys)

values=names.values()
print(values)

names1=names.get('sunny')
print(names1)

names1=names['sunny']  #with using index
#index=names1[0]   #doubt i want output as s
print(names1)

names1=names.get('sunny1') #returns None if the value dosen't exist
print(names1)

#names1=names['sunny1']   #with using index not advisabble to use as it gives error
#print(names1)


#type conversions

my_number=6
my_number_float=7.6
#my_number_str='xyz'
my_number_str='8'

#converting float to int

my_number_float=int(my_number_float)
print(my_number_float)

#converting str to int

my_number_str=int(my_number_str)
print(my_number_str)

#coverting int to string

#my_number=str(my_number) # Doubt we cannot convert int to string error
#print(my_number)

#converting int to float
my_number=float(my_number)
print(my_number)


#naming convenstions

_name='john'
name123='alex'
print(_name,name123)

$name='max'   #not acceptable
123name='mark'  #not acceptable


