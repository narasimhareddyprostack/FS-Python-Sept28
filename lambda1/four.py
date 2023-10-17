marks=[35,36,37,38,39]

new_marks=[]

def add_mark(mark):
    return mark+1


for mark in marks:
    new_marks.append(add_mark(mark))


print(marks)
print(new_marks)

