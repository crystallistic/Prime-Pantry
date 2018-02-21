'''
Authors: Asmita Gautam and Mai Ngo

Coding Challenge 3: Prime Pantry v2
Objective: given a dictionary of items and their (integer, positive-valued)
item weights, identify whether or not there is a subset that could fill a
Prime Pantry Box to exactly 100% and report which items are in the subset

Example function call:
------------------------------------------------------
primePantryV2({“pepsi”:55,“detergent”:30, “chips”:25,     
               “cereal”:15}, 4, 100)
------------------------------------------------------
Desired output:
------------------------------------------------------
[“pepsi”, “detergent”, “cereal”]
------------------------------------------------------
You only need to return one correct match to get full credit.
Bonus point if you can return all matches. 
'''

def primePantryV2(dict_items, num_items, total):
    ''' Function to identify whether there is a subset of items that could
    fill a Prime Pantry box to exactly 100% and report which items are in the
    subset, given a dictionary of items and their item weights.

    Parameters:
    dict_items - dictionary of items
    num_items - number of items in the dictionary
    total - the box capacity that needs to be filled to, equals 100 by default

    Return
    have_subset - true/false whether subset exists
    subset - subset of items that fit the requirements

    '''
    have_subset = false
    subset = []
    items = dict_items.keys()

    sum = 0

    while (sum <= 100):
        for irem in items:
            price = dict_items[item]
            if (sum + price < total):
                
