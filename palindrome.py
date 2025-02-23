def isPalindrome(word:str) -> bool:
    word = word.lower()
    wordLength = len(word)
    
    for i in range(wordLength // 2):
        if word[i] != word[wordLength - i - 1]:
            return False
    return True

print(isPalindrome("madam"))
print(isPalindrome("ABBA"))


def isPalindromeSimple(word):
    word = word.lower()
    return word == word[::-1]
    
print(isPalindromeSimple("MADAM"))
print(isPalindromeSimple("ABBA"))
print(isPalindromeSimple("KIAN"))
print(isPalindromeSimple("USM"))
print(isPalindromeSimple("LENOVO"))