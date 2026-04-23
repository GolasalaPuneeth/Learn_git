def sample_1(a:int,b:int) -> int:
    """
    This function will gives u sum of 2 numbers
    a : should be int
    b : should be int

    return : int

    """
    print("in Function - ",a+b)
    return a+b

# =============================================

def greet(name):
    print(f"Hi {name} how are you")
    return f"Hi {name} how are you"
# =================================================

def area_square(s:int)->float:
    return(float(s**2))
# ===================================================

def  greet_mult(*names):
    for i in names:
        greet(i)
# =====================================================

def greet_everyone(time_ist: int,name="Everyone"):
    print(f"Hi {name} How are you {time_ist}")
# ======================================================

#    count = 0
#     while(count<10):
#         # count+=1
#         print(count)
#         count = count + 1

# =======================================================
def main():
    count = 0
    while 1:
        count+=1
        if count==10:
            continue
        print(count)






    

    
   


if __name__=="__main__":
    main()