
# You are given a string A of size N.

 

# Return the string A after reversing the string word by word.

# NOTE:

# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
 



# Problem Constraints
# 1 <= N <= 3 * 10^5



# Input Format
# The only argument given is string A.



# Output Format
# Return the string A after reversing the string word by word.



# Example Input
# Input 1:
#     A = "the sky is blue"
# Input 2:
#     A = "this is ib"


# Example Output
# Output 1:
#     "blue is sky the"
# Output 2:
#     "ib is this"



# Example Explanation
# Explanation 1:
#     We reverse the string word by word so the string becomes "the sky is blue".
# Explanation 2:
#     We reverse the string word by word so the string becomes "this is ib".
# Source: interviewbit.com

def reverse_string_by_word(s: str) -> str:
    s = s.strip()
    string_as_list = s.split(" ")
    print("string_as_list", string_as_list)
    result_str = ""

    for word in string_as_list[::-1]:
        trimmed_word = word.strip()
        if len(trimmed_word) == 0:
            continue
        result_str += trimmed_word
        result_str += " "
    
    return result_str.strip()

