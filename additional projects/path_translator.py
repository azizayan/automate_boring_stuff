# this program converts the path of the folders between macOS and windows
# however it does not produce the exact path in your computer, it only changes slashes depending OS.



def translate(path):
    new_path = ""
    for char in path:
        if char == '/':
            new_path += '\\'
        elif char == '\\':
            new_path += '/'
        else:
            new_path += char
    return new_path

def main():
    print('Enter folder path to convert: ')
    path = input()
    print(translate(path))



main()