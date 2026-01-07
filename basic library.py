 #modules usage prevents the manually doing tasks
#syntax: import module_name
import math
math.sqrt(36)
#giving a alias for module name
import math as m
fun_1=m.sqrt(999)
print(fun_1)

#importing functions at a time
from math import radians,sin,cos,tan,tanh
degrees_1=40
radians=radians(degrees_1)
sin_value=sin(radians)
cos_value=cos(radians)
tan_value=tan(radians)
tanh_value=tanh(radians)

print(sin_value)
print(cos_value)
print(tan_value)
print(tanh_value)
#importing all functions from module
from math import *
print(pow(5,3))

import datetime
birthday = datetime.date(2005,11,26)
print(birthday.day)
print(birthday.month)
print(birthday.year)

from statistics import*
mean_value=[23,4,45,5,66,66]
print(mean(mean_value))
print(stdev(mean_value))
print(variance(mean_value))