a = int(input("number: ")) # write a number.
mod_list=[]
if(a <= 1):
    print("{} is not prime number.".format(a))

elif(a == 2):
    print("{} is prime number.".format(a))

else:
    for i in range(2,a):
        mod = a%i
        mod_list.append(mod)
    
    if(0 in mod_list):
        print("{} is not prime number.".format(a))

    else:
        print("{} is prime number.".format(a))
