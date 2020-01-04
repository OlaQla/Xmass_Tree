 
def tree():

    n=20
    for i in range(n):
        print(" ", end="")
    print("|")
    
    for h in range(6):
        for j in range(3):
            for i in range(n-1-j-2*h):
                print(" ", end="")  
            print("/", end="")
            max_s=2*j+4*h
            for s in range(max_s + 1):
                if j==2 and h<5 and (s==0 or s==max_s):
                    print("_", end="")
                else:
                    print(" ", end="")  
            print("\\")

    for z in range(n-14):
        print(" ", end="")
        
    print("|", end="")

    for i in range(2*n-1-2*(n-14)):
        print("_", end="")
    print("|")


    for i in range(n-4):
        print(" ", end="")
    print("\\", end="")
    for i in range(7):
        print("_", end="")
    print("/")

tree()

