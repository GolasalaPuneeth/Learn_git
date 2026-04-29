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


# 5 - if and else
# 5 - loops
# 5 - function(*args) position args
# 5 - (loops, if, functions) mixed

# numbers which are divisible by 3 is 'Fizz'
# numbers which are divisible by 5 is 'Buzz'
# numbers which are divisible both 3 & 5 is "FizzBuzz"
def fizz_buzz(num):
    count = 1
    while count<=num :
        if count%3==0 and count%5==0:
            print("FizzBuzz- ",count)
        if count%3==0:
            print("Fizz- ",count)
        elif count%5==0:
            print("Buzz- ",count)
        
        count+=1


#print till 'N'
# fizz_buzz(20)
# ==========================================================
# mypass = "Admin@123"
# count = 2
# while True:
#     user_input = input("Enter pass = ")
#     if user_input == mypass:
#         print("Correct Pass")
#         break
#     elif count==0:
#         print("Wrong Pass Max Tryout")
#         break
#     else:
#         print("Wrong pass")
#     count-=1
# =======================================================
# i=5
# x = f"2 x {i} = {2*i}"
# print(x)




    

    
   


if __name__=="__main__":
    main()