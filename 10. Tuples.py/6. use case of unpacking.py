#Make a function which returns min and max of a list

def min_max(lst):
    #Logic
    mini = min(lst)
    maxi = max(lst)
    return mini, maxi

#print(min_max([5, 67, 3, 2, 1, 65, 7, 43]))
ans1 , ans2 = min_max([5, 67, 3, 2, 1, 65, 7, 43])
print(f"Minimum number is {ans1} and Maximum number is {ans2}")