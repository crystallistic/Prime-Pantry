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
------------------------------------------------------
Desired output:
------------------------------------------------------
['pepsi', 'detergent', 'cereal']
------------------------------------------------------
You only need to return one correct match to get full credit.
Bonus point if you can return all matches. 
'''
from collections import OrderedDict
from operator import itemgetter
import math

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

    sort = OrderedDict(sorted(dict_items.items(), key=itemgetter(1)))
    have_subset = False
    list_keys = list(sort.keys())
    subset = []

    sums = [{} for i in range(len(sort))]
    sums[0].update({list_keys[0]: sort.get(list_keys[0])})

    for i in range(1, num_items):
        j = i
        sums[i].update({list_keys[i]: math.inf})
        while sums[i].get(list_keys[i]) > 100:
            (sums[i])[list_keys[i]] = sums[j-1].get(list_keys[j-1]) + sort.get(list_keys[i])
            j = j - 1
        sums[i].update(sums[j])

    print (sums)
