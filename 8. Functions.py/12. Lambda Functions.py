#def square(num):

    #return num*num

#square = lambda num: num*num

#print(f"{square(10)}")
#

# return true if user can vote else false
"""
def is_adult(age):
    if age>=18:
        return True
    return False
"""

is_adult = lambda age: True if age>=18 else False

print(is_adult(1))