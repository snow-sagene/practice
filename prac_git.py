print("hello world")

#make 

with open("integers.txt","w") as f : 
    for i in range(1,11):
        f.write(str(i) + "\n")