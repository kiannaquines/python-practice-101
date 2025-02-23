def palindrome(word:str) -> bool:
  length = len(word)
  for i in range(length // 2):
    if word[i] != word[length - i - 1]:
      return False

  return True


print(palindrome("madam"))
