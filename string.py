my_str='depressed guy'
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
print(my_str.startswith('e'))
print(my_str.endswith('y'))

print(my_str.find('guy'))
print(my_str.index('d'))
print(my_str.count('s'))
print(my_str.capitalize())
