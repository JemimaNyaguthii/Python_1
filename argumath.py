# Positional arguments 
# Positional arguments should be used whenever you know the order of argument to be passed.
def multiply(a,b):
    print (a*b)

    # //output multiply(36,2)
    # If you try to pass more arguments you get an error stating that the multiply takes only
    #   2 positional argument
def total(student,grade):
    print(f"{student} scored a {grade}")

    #  //output total("jem",76)

    #Keyword arguments
    # values get assigned to the arguments by their keyword name when the function is called.The = operator is used.
    # All the keyword arguments should match the parameters in the function defination,when the functions are
    #  called the order of arguments can be changed 

def total (student,grade):
    print(f"{student} scored a {grade}")    
    # //output total(student="jem",grade=76)  

# We declare a variable length using an asterisk.It enables one to pass multiple arguments to the function
# it does not limit the arguments to be passed
def country(*names):
    for name in names:
       print(f"Am from{name}")    

    #    //output country("Kenya","Uganda","Rwanda")
    
#    We can declare a variable length using ** asterisk.it enables one to pass multiple keyword arguements
#  to the function.it is used the same as accesing a dictionay.


