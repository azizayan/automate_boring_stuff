def a():
    print("a starts")
    b()
    d()

def b():
    print("b starts")
    c()

def c():
    print("c starts")
    
def d():
    print("d starts")

def main():
    a()

if __name__ == "__main__":
    main()