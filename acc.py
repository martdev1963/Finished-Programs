#/--------------------------------------------------------------------------Bank Account Classes-----------------------------------------------------------------------------/
# base class
class Account:

#/----------------------------------------------------------------BEGIN class Account FUNCTION DEFINITIONS-------------------------------------------------------------------------/
    # base class constructor...
    def __init__(self, filepath):
        self.filepath=filepath # object attribute, self.filepath is assigned the value passed in filepath parameter...
        with open(filepath, 'r') as file:
            self.balance=int(file.read()) # store the bank acct balance value from txt file into this instance variable...(cast it to int)
            # read() returns a string by default...must cast to int(read())


    def withdraw(self, amount):
        self.balance=self.balance - amount


    def deposit(self, amount):
        self.balance=self.balance + amount


    def commit(self):
        with open(self.filepath, 'w') as file: # file is a temporary variable in memory...
            file.write(str(self.balance))# commit the changes to the file...note haw the commit() function is the last function in the script...

#/------------------------------------------------------------------END class Account FUNCTION DEFINITIONS-----------------------------------------------------------------------------/


# instantiating an object of class Account...the base class...
account=Account("account//balance.txt") # passing the filepath parameter to the new object...for self parameter, Python will automatically pass the account object instance
# no need to pass the self parameter...


#///////////////////////////////////////////////////////////////////////////////**SUB CLASSES**\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# sub class (inheriting the base class: Account...) The whole point of inheritance is Code Reuse...
class Checking(Account): # passing the base class to the sub class' constructor to establish inheritance...
    # OOP Glossary...
    # class
    # Object Instance
    # Instance variable - instance variables are shared by only object instances...
    # Class variable
    # class variables are declared outside the function definitions or methods of that class...class variables are shared by all the instances of a class.
    # Doc strings
    # Data member - class variables and instance variables...
    # Constructor
    # Methods
    # Instantiation - creating an object from a class...
    # Inheritance - creating a sub class out of a base class...
    # Attributes - class variables and instance variables...

    """This class generates checking account objects""" # this is a Doc string
    type="checking" # also considered a data member...

#/---------------------------------------------------------------BEGIN class Checking FUNCTION DEFINITIONS-------------------------------------------------------------------------/

    def __init__(self, filepath, fee): # sub class contructor...
        Account.__init__(self, filepath) # calls the base class constructor...
        self.fee=fee # instance variable... # also considered a data member...


    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

#/----------------------------------------------------------------END class Checking FUNCTION DEFINITIONS-----------------------------------------------------------------------------/

# object 1
# instantiating an object of class Checking...a sub class...
jacks_checking=Checking("account\\jack.txt", 1) # the first argument, the self argument is automatically passed by Python (implicitly passed...)
# the 2nd argument, filepath is the database file
# the 3rd argument, is the self.fee (the instance variable)
jacks_checking.transfer(200)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)
print(jacks_checking.__doc__) # prints out the doc string which is associated with every object of a particular type of class...

# object 2
# instantiating an object of class Checking...a sub class...
johns_checking=Checking("account\\john.txt", 1) # the first argument, the self argument is automatically passed by Python (implicitly passed...)
# the 2nd argument, filepath is the database file
# the 3rd argument, is the self.fee (the instance variable)
johns_checking.transfer(200)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.__doc__)

#/--------------------------------------------------------------------------FUNCTION CALLS-----------------------------------------------------------------------------------/
print(account.balance) # using dot notation to point to the balance attribute value...otherwise you just get the object memory address location in hexadecimal
#print(account) # outputs: <__main__.Account object at 0x0042F670>

account.deposit(200) # withdraw function takes 2 arguments...the self or object argument is automatically passed by python...and the amount.. # updated balance..
print(account.balance) # updated balance...

# you still have to call the commit() function to update the database file...
account.commit()

print("Base class Checking Account Balance: " + str(account.balance))
#print(checking)
#print(checking.balance)

#checking.deposit(1000)
print("Sub class Checking Account Balance: " + str(jacks_checking.balance))

#checking.transfer(200)

#checking.commit()

#print(checking.balance)

"""
OUTPUT:


"""
