'''
Authors: Asmita Gautam and Mai Ngo
Coding Challenge 3: Prime Pantry v2
Objective: given a dictionary of items and their (integer, positive-valued)
item weights, identify whether or not there is a subset that could fill a
Prime Pantry Box to exactly 100% and report which items are in the subset
Example function call:
------------------------------------------------------
primePantryV2({'pepsi':55,'detergent':30, 'chips':25,     
               'cereal':15}, 4, 100)
primePantryV2({'pepsi':55,'detergent':30, 'chips':25,     
               'cereal':15, 'chocolate' : 70, 'soy milk' : 45}, 6, 100)
------------------------------------------------------
Desired output:
------------------------------------------------------
['pepsi', 'detergent', 'cereal']
------------------------------------------------------
You only need to return one correct match to get full credit.
Bonus point if you can return all matches. 
'''

#Global variable to keep track of whether there are any subsets
#that match the given criteria
have_solution = False 

def primePantryV2(dict_items, num_items, total):
    
    ''' Function to identify whether there is a subset of items that could
    fill a Prime Pantry box to exactly 100% and report which items are in the
    subset, given a dictionary of items and their item weights.
    Parameters:
    dict_items - dictionary of items
    num_items - number of items in the dictionary
    total - the box capacity that needs to be filled to, equals 100 by default
    '''
    
    try:
        if not (isinstance(dict_items, dict) and isinstance((list(dict_items.values()))[0], int)
                and isinstance(num_items, int) and isinstance(total, int)):
            raise ValueError()
        
        # turn the list of items and their weights into a list of tuples
        items = list(dict_items.items())
        
        # after every recursive call, only look at a partial list of original list of items
        partial_lst = []
        
        # set global variable to False
        global have_solution
        have_solution = False

        # call recursive worker function to find subsets that match the criteria
        workerFunc(items, total, partial_lst) 
        
        if (have_solution == False):
            print ("No possible subset gives the desired total")
            
    except (ValueError):
        print("Invalid input. Needs to be primePantryV2(dict, int, int) types.")
        print("dict_values must be int.")
   
def workerFunc(items, total, partial_lst):
    
    '''Recursive function that prints out all possible combinations
    for desired total weight'''
    
    curr_sum = sum([tup[1] for tup in partial_lst]) # get the sum of weights

    # check if curr_sum is equal to desired total
    if curr_sum == total:

        # update global var
        global have_solution
        have_solution = True

        # print subset that matches criteria and number of items in it
        print([tup[0] for tup in partial_lst]) 
        print("Number of items in the subset: ", len(partial_lst), "\n")

    # do not proceed with subsets whose total weight >= total
    elif curr_sum >= total:
        return

    # recursion: consider gradually smaller parts of the original items list
    for i in range(len(items)):
        n = items[i]
        remaining = items[i+1:]
        workerFunc(remaining, total, partial_lst + [n])
   
