marks=[35,36,37,38,39]

def add_mark(mark):
    return mark+1


#map(1,2)
#map(function,sequence)
map_obj=map(add_mark,marks)
new_marks=list(map_obj)

print(marks)
print(new_marks)