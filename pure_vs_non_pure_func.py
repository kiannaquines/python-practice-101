names = ["kian","james","irish","jearard","arden","francis"]


# NON PURE FUNCTIONS

# Explaination
# This considered as a non-pure functions since the function change the global variable names.
def non_pure_func(name:str) -> list:
    names.append(name)
    return names
    
print(non_pure_func("abegail"))
print(non_pure_func("baby"))

# PURE FUNCTION
# This is a pure function since it does not directly change the global variable call_sign instead it creates a copy before modifying the list

call_sign = ["baby","abby","love","loveey"]


def pure_func(sign:str) -> list:
    call_sign_copy = call_sign.copy()
    call_sign_copy.append(sign)
    
    return call_sign_copy
    
print(pure_func("abe"))
