def palindrome_check(word_to_check):
    if word_to_check == word_to_check[::-1]:
        print(True)
    else:
        print(False)


palindrome_check(str(input('Enter a word to check: ').lower()))