
def myPrint(printinput, printmessage = None, holdvariable = True):

    """ A new print function that prints an output given by the first argument
   underneath an output message given by the second argument, and then waits
   for a user input before moving on.  """

    try:
        if printmessage != None: 
            print('_'*20, printmessage, '_'*20)
        print(printinput)

        if holdvariable:
            input("Press any button to continue.")
    except:
        print("Error in input")



##### - Test case of myFunctions - #####

if __name__ == "__main__":

    import pandas as pd
    
    train = pd.read_csv("train.csv")
    myPrint(train.head(), "Test Data")
    myPrint("Test no hold", None, False)
    myPrint("Test no message")
