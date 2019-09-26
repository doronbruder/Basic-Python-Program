def input_list():
    """This function gets strings from the user and return a list of these strings"""
    string_list = list() # this will be the list we will put in the strings from the user
    user_string = input() # the function waiting for the user to input string-with no print to the user
    while not not user_string: # each round the loops check if the string puted is empty -if no it contiues
        string_list.append(user_string) # adds a string to the list
        user_string = input() # wait for another string
    return string_list # after the loop finished<=>empty string puted -the list returned as output


def concat_list(str_list):
    """This function gets a string list from the user and bring back a string created by  the list parts  """
    if not str_list: # if the list is empty it returns an empty string
        return ""
    if(len(str_list)==1): # if the list includes only a single value it will simply return to user that value
        return str_list[0]
    string_from_list = "" # string that serves us to put in the list strings as long string
    for i in range(len(str_list)): # cases where the list includes more than one value
    # the loop goes over the list and sum its strings values toghether  to the string we built
        string_from_list +=" "+str_list[i]
    return string_from_list


def maximum(num_list):
    """This function gets a list of numbres from the user and return the maximal number"""
    if not num_list: # if the list is empty return "None" value
        return None
    max = 0 # created an int to save inside each time maximal value so far
    for i in range(len(num_list)): ## the loop runs all over the list and compare every item to max
        if num_list[i] >= max: # if its bigger than max, max updated with this value
            max = num_list[i]
    return max


def cyclic(lst1, lst2):
    """This function checks if two lists are a cyclic permutation of each other """
    if lst1 == lst2: # if the two lists equal return true,its including the case which both empty lists
        return True
    elif len(lst1) != len(lst2): # if the lists have different length return false
        return False
    length = len(lst1) # since from that point the lengths are the same , we call it just "length"
    for step in range(
            length): # the first loop choooses each time a specific step to the right in lst1 that could represents a cyclic permutation
        flag = True  # each round of the loop its become true until there is a contradiction in the second loop
        for index in range(
                length): # the second loop check if the current step fits between all the items -even if itsnt for one than its false
            if lst1[index] != lst2[(index + step) % length]:
                flag = False
                break
        if flag: # its enouph to finish one rep of the second  loop for some step with no contradictions and its true
            return True
    return False


def seven_boom(n):
    """ Replaces every int from a list [1,2,..,n] that is either divided into 7 or includes the char '7' by 'boom """
    nums_list = list()
    create_num_list(n, nums_list) # create a list of 1,2...n
    for i in range(len(nums_list)): # the loop run and check for each int if its divided into 7 or includes '7'
        if int(nums_list[i]) % 7 == 0: # divided into 7 test
            nums_list[i] = 'boom' # marked as boom
        else:
            includes_7_char(i, nums_list) # test if a number is divided into 7
    return nums_list


def includes_7_char(i, nums_list):
    for digit in range(len(nums_list[i])):  # a loop that is actually test for including '7' in each int
        if nums_list[i][digit] == '7':
            nums_list[i] = 'boom'
            break


def create_num_list(n, nums_list):
    for i in range(1, n + 1):  # initialize the above empty list into list [1,..n]
        nums_list.append(str(i))


def histogram(n, num_list):
    """This function gets a list of numbers and retruns its apropiate histogram list"""
    histogram_list = [0] * n # creates a list that will used as  histogram list
    for i in range(len(num_list)): # the loop runs over the inputed list
        index = num_list[i]
        histogram_list[index] += 1 # updates +1 the item in the index that equal to the item itself in the original list
    return histogram_list # after the loop finished the histogram list is all set, so retur it


def prime_factors(n):
    """This function finds the prime factors of a number-'n' and bring back list of these factors"""
    i = 2
    factors_list = [] # a list that will used as the factors list
    while i <= n: # goes over all the numbres until n
        if (n % i) == 0: # checks if n divided into i if it does check if n/i is divided into i and so on
            factors_list.append(i) # every time when it does divided into i , i is added as prime factor
            n = n / i
        else:
            i = i + 1 # if it doesnt divided into i we'll check for i+1
    return factors_list #after we cheack all potential factors return the list of them


def cartesian(lst1, lst2):
    """ This function returns a list that represents the cartesian multiplication of two groups of
    numbres that represented by two lists """
    cartes_lst=[] # the list that will  represent the cartesian multipication
    for i in range(len(lst1)): # goes over the first list
        for j in range(len(lst2)): # goes over the second list with each value from the first list
            cartes_lst.append([lst1[i],lst2[j]]) #adds all possible pairs
    return cartes_lst

def pairs(num_list, n):
    """This function finds all the pairs from a given list that their sum is n ,
    and puts these pairs as items of a new list"""
    pairs_list=list() # This list will used as the list of the  pairs  that their sum is n
    for i in range(len(num_list)): # runs over the loop
        for j in range(i+1,len(num_list)): # from each point of the list it checks all the items forward to
            if num_list[i]+num_list[j]==n: # cheacks if the sum of a current pair is n
                pairs_list.append([num_list[i],num_list[j]]) # if it does it adds it to the  list
    return pairs_list


