def list_to_string(list):
    if len(list) == 0:
        return

    str = ""
    for i in range(len(list)):
        if i == len(list)-1:
            str += "and " + list[i]
        else:
            str += list[i] + ',' + ' '
    
    return str


if __name__ == "__main__":
    list = ['apples', 'bananas', 'tofu', 'cats']
    str = list_to_string([])
    print(str)
