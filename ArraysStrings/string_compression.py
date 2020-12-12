
def string_compression(string):

    list = []

    count = 1

    for i in range(len(string)):
        if i == len(string) - 1:
            list.append(f'{string[i]}{count}')
        elif string[i] == string[i + 1]:
            count += 1
        else:
            list.append(f'{string[i]}{count}')
            count = 1

    return "".join(list)
