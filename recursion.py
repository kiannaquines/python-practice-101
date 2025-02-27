def recursion(counter=0):
    
    if counter >= 10:

        print("Recursion terminated")
        
        return
    
    recursion(counter + 1)

    print(f"Recursion counter: {counter}")
    
recursion()