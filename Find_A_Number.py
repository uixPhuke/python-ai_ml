my_list=[33,65,75,12,33,0]

x=int(input("Enter a No. to find index: "))

index=0
for i in my_list:
    if(i==x):
        print(f"Found in index {index}")
        break
    index+=1
else:
    print("Not found")
    