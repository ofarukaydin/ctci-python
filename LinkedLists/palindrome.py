

def palindrome(list):
    if len(list) <= 1:
        return True
    elif list[0].value == list[-1].value:
        list.pop_front()
        list.pop()
        return palindrome(list)
    else:
        return False
