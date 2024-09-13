# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # TODO: Implement a basic anagram check
    return ...

# Follow-up: Modify the function to account for case sensitivity and spaces
def are_anagrams_ignore_case_spaces(str1, str2):
    # TODO: Implement anagram check ignoring case sensitivity and spaces
    return ...


# Define main function
def main():
    string1 = "Listen"
    string2 = "Silent"
    print(are_anagrams(string1, string2))  # Expected output: True
    print(are_anagrams_ignore_case_spaces(string1, string2))  # Expected output: True


if __name__ == "__main__":
    main()