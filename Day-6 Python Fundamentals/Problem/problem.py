data=True
Line=1
word="Python"

with open("input.txt", "r") as f:
    while data:
        data=f.readline()

        if(word in data):
            print(f"{word} Found on Line {Line}")
            break

        Line+=1
        #print(data)