def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
       return " and ".join(items)
    elif len(items) == 3:
        all_but_last = items[:-1]
        last_item = items[-1]
        joined = ", ".join(all_but_last)
        final_string = joined + ", and " + last_item
        return final_string
    elif len(items) > 3:
        all_but_last = items[:-1]
        last_item = items[-1]
        joined = ", ".join(all_but_last)
        final_string = joined + ", and " + last_item
        return final_string
        
 
        


    