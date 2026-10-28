#keyword arguments 

def calculate_marks(maths, eng, hindi, comp=0, history=0): #required parameters on left and default parameters on right
    print(f"maths = {maths}")
    print(f"english = {eng}")
    print(f"hindi = {hindi}")
    print(f"computer = {comp}")
    print(f"history = {history}")
    total_marks = maths+eng+hindi+comp+history
    print(f"Total marks scored = {total_marks}")

calculate_marks(maths=43, eng=66, hindi=54)