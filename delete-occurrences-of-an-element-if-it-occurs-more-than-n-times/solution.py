def delete_nth(order,max_e):
    d = {}
    return_list = []
    
    for item in order:
        if (item not in d):
            d[item] = 1
        else:
            d[item] += 1
            
        if (d[item] <= max_e):
            return_list.append(item)
    
    return return_list