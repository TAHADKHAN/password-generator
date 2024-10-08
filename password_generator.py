import random
import string

def Generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for your password: "))
        if length < 1:
            print("password length should be atleast 1.")
            return
        password = Generate_password(length)
        print(f"generate password : {password}")
    except ValueError:
        print("Invalid input. please enter a valid number.")
        
if __name__ == "__main__":
    main()
