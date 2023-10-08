def top_n (items, n):
    """Retruns the top n items in an array, in desc order,
    
    Args:
        items (array): list or array-like object
        n (int): number of items to return
    
    return:
        array: top n items, in desc order
    
    EGs: 
        >>> top_n([8,3,2,7,4],3)
        [8,7,3]
    """
    for i in range (n): # keep sorting untill we have the top n items
        for j in range (len(items)-1-i):

            if items[j] > items [j+1]: # if this item is bigger than next item..
                items[j], items[j+1] = items[j+1],items[j] # swap the two!
    # get last two items

    top_n = items[-n:]

    #return in desc order
    return top_n[::-1]

top_n([8,3,2,7,4],3)