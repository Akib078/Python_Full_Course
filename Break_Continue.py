names =["Anamika","Akib","Sadia","Tinni","Neelima","Mehedi"]

for i in names:
    if i=="Tinni":
        break      #Stops loop at Tinni
    print(i)

print("")

for j in names:
    if j=="Tinni":
        continue   #Continue loop without Tinni
    print(j)