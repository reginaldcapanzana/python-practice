# Create a function that reverses a string
def reverse(str):
    # Uses built in Python function 
    revStr = str[::-1]
    return revStr

def main():
    usrInput = input("Enter a string: ")
    print(usrInput)
    print("String in reverse")
    print(reverse(usrInput))

if __name__ == "__main__":
    main()