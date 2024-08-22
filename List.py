marks = [85,87,89]
print(marks[-2]) #87

print(marks[0]) #85

print(marks[0:2]) #85 to 87

marks.append(90) #add 99 to end

marks.insert(0,92) #add 92 to start

print(len(marks)) #length of list

for i in marks:
    print(i) #All marks

print(99 in marks) #False

marks.clear() #empty list
print(marks)

