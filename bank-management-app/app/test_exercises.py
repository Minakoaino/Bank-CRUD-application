def longest_sequence(s):
    current_char = None
    current_count = 0
    longest_char = None
    longest_count = 0

    for char in s:
        if char == current_char:
            current_count += 1
        else:
            current_char = char
            current_count = 1

        if current_count > longest_count:
            longest_char = current_char
            longest_count = current_count

    return longest_char


input_str = "AAaaaaaaaBGTTTRL"
result = longest_sequence(input_str)
print("The result is:", result)



def longest_sequence(s): 
    Current_char = None 
    Current_count = 0 
    Longest_char = None 
    Longest_count = 0 
    for char in s: 
        if char == Current_char: 
            Current_count +=1 
        else: 
            Current_char= char 
            Current_count = 1 
        if Current_count > Longest_count: 
            Longest_char = Current_char 
            Longest_count = Current_count 
            
    return Longest_char 
                    
Input_str = "AABGTTTRL"
Result = longest_sequence(input_str) 
print("Το αποτέλεσμα είναι:", result)