my_str='Happy New year 2026'
trimmed_str=my_str.strip('D')
print(trimmed_str)
replaced_str=my_str.replace('Depressed','not depresssed')
print(replaced_str)
split_str=my_str.split()
print(split_str)
#join() elements of iterable to end of string
joind_my_str= "".join(my_str)
print(joind_my_str)
#check startwith and endswith of string
print(my_str.startswith('H'))
print(my_str.endswith('6'))

print(my_str.find('new'))
print(my_str.index('a'))
print(my_str.count('H'))
print(my_str.capitalize())

my_string="Happy New YEAR 2026"
print('new' in my_string)
print('202' in my_string)

my_str3=my_str.format()
print(my_str3)
#str.maketrans(): This method is used to create a table of 1 to 1 character mappings for translation. It is often used with the translate() method which applies that table to a string and return the translated result.
table = str.maketrans("bharath","indians")
print(table)
