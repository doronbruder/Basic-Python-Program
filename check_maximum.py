from ex3 import maximum

def check_max():
    """ This function test if maximum function works well"""
    if maximum([1,2,3]) == 3 : # check for first input
        subtest1 = True
        print("Congrats!, first subtest have succeed")
    else :
        subtest1 = False
        print('oops!, something went wrong with the first subtest')

    if maximum([0,0,0]) == 0:
         subtest2 = True
         print("Second subtest passed!")
    else:
         subtest2= False
         print("second subtest faild!")

    if maximum([1,2,2]) ==  2:
         subtest3 = True
         print("Third subtest succeed!")
    else:
         subtest3 = False
         print("There was a problem with 3rd subtest")
    if maximum([1]) == 1:
        subtest4 = True
        print("The last subtest is OK!")
    else:
         subtest4 = False
         print(" 4th subtest Faild!!") # check for forth input
    if subtest1 and subtest2 and subtest3 and subtest4 :
        return True
    else:
        return False

if __name__ == "__main__":
    check_max()
