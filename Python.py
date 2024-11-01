#Anagram Check
def find_anagram(list1,list2):
    # Sort list1,list2
    list1.sort()  
    list2.sort()  
  
    position = 0  
    matches = True  
  
    while position < len(list1) and matches:  
        if list1[position]==list2[position]:  
            position = position + 1  
        else:  
            matches = False  
  
    return matches  
list1 = [1,1,2,3,4,5]  # Assign list1
list2 = [5,4,3,2,1,1]  # Assign list2

print(find_anagram(list1,list2)) 

