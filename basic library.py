 #modules usage prevents the manually doing tasks
#syntax: import module_name
import math
math.sqrt(36)
#giving a alias for module name
import math as m
fun_1=m.sqrt(999)
print(fun_1)

#importing functions at a time
from math import radians,sin,cos,tan
degrees_1=40
radians=radians(degrees_1)
sin_value=sin(radians)
cos_value=cos(radians)
print(sin_value)
print(cos_value)
