# write a function called absolute_value that takes a number and returns its absolute value without using the built-in ans() function.

def absolute_value(a):
    if a<0:
        return -a
    else:
        return a
    
print(absolute_value(-67))