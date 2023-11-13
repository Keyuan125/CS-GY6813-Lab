def checkPalindrome(input_string):
    length = len(input_string)
    if length == 0:
        return False
    else:
        l, r = 0, length - 1
        while l < r:
            if input_string[l] != input_string[r]:
                return False
            else:
                l += 1
                r -= 1
    return True
