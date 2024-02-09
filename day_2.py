
# what is the differrence between python lists and arrays.( we will discuss that)
# Nested Lists

# python list can contain any data typess
# my_list = [1,2,4,6,'3asd', 8.6]

nest_list = [[1,3], [6,5], 4, [3,4], 'str', ]
# print(nest_list)

# indexing in nested list
number = nest_list[0][1]
# print(number)

my_other = nest_list[1][0]
# print(my_other)


# Nested Dictionaries
nest_dict = {
    1:{
        "usa":'new york',
        1:2
    },
   2:{
        "uk":'london'
    }, 
    3: [3,42,4]
}

# indexing in nested dictioniies
# Json = python dictionaries
el = nest_dict.get(1)
# print(el.get('usa'))

# normal_dict = { 1:'value1', 2: [1,3,4]}


# aritmaitcs Operators 
# +, - , *, / , modulules



# print (50*'#')


# comparsion operators
# ==, != , < , > , <= , >=

# Logical Operators
# and , not, or 

# Bitwise operator >> 

# Conditional statemetns
# if this thing is true:
#     do this
# otherwise :
#    do that

# Indentation is used to write separate blocks
# Chercking equality
var_1= 4
var_2 = 5
# if var_1 == var_2:
#     print('both are equal')
# else:
#     print('both or not equal')


# checking not equal to 
# if var_2 != var_1:
#     print('these are not equal')


# if not (var_2 == var_1):
#     print('these are not equal')

# if (var_2 == var_1):
#     print('these are not equal')

# Checking > , < 
# if var_1 < var_2:
#     print('var 1 is less than var 2')

# Checking >=  , <=  
if var_1 >= var_2:
    print('var 1 is less than var 2')

# Combining multiple expressions in the condition

if (var_1==4) and (var_2==5):
    print('both expression exxecuted to true')

if (var_1==4) & (var_2==5):
    print('both expression exxecuted to true')

# in or one statement should be true in order to execute the block
if (var_1==4) or (var_2==5):
    print('both expression exxecuted to true')
    print('do this things')
    print('dosd')

if (var_1==2) | (var_2==4):
    print('do something')




# if , elif , else
temp = 45 
if temp > 45:
    print('it is very hot')
elif temp > 50:
    print('it is beyound hot')
elif temp > 60:
    print('it is severe')
else:
    print('it is normal')

# Take input from user
uer_input = input('Enter a number:')
print(uer_input)


# Nested conditioanl statmetts




