input = "aabaa"


def is_palindrome(string):
    if len(string)==1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])



    return True


print(is_palindrome(input))