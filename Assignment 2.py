#Question 1 :
def reverse_concatenate(s, i):
    return s[::-1] * i
    print(reverse_concatenate("hello", 2))
#Question 2 :
def rearrange_string(s):
    uppercase = ""
    lowercase = ""

    for char in s:
        if char.isupper():
            uppercase += char
        else:
            lowercase += char

    return uppercase + lowercase
#Question 3 :
def is_reordering(s1, s2):
    return sorted(s1) == sorted(s2)
#Question 4 :
def find_highest(l):
    if not l:
        return "The list is empty."

    highest_value = l[0]
    highest_index = 0

    for i in range(1, len(l)):
        if l[i] > highest_value:
            highest_value = l[i]
            highest_index = i

    return f"highest value in the list : {highest_value} at index {highest_index}."
#Question 5 :
 def digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digit_sum(n // 10)
#Question 6 :
 def remove_duplicates(s):
    if len(s) < 2:
        return s

    if s[0] == s[1]:
        return remove_duplicates(s[1:])
    else:
        return s[0] + remove_duplicates(s[1:])
      




  
    
  

    






