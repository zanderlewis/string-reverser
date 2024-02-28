def reverse_string(s):
    return s[::-1]

def main():
    input_string = input("Enter a string to reverse: ")
    reversed_string = reverse_string(input_string)
    print(f"The reversed string is: {reversed_string}")

if __name__ == "__main__":
    main()
