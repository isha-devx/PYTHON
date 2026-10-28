#EXAMPLE 1
#normal way using a loop

#squares = {}
#for i in range(1, 11):
    #squares[i] = i*i

#print(squares)

#using list comprehension

#squares = {i: i*i for i in range(1,11)}
#print(squares)


#EXAMPLE 2
#marks = {"math": 85, "science": 92, "english": 60, "hindi": 45}

#top = {sub:m for sub, m in marks.items() if m>80}
#print(top)


#ZIP()
subjects = ["maths","science","english"]
marks = [99, 88, 77]
result = {sub: m for sub, m in zip(subjects,marks)}
print(result)

