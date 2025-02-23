def palindrome(word:str) -> bool:
  length = len(word)
  word = word.lower()
  for i in range(length // 2):
    if word[i] != word[length - i - 1]:
      return False

  return True


print(palindrome("madaM"))

def palindrome(word:str) -> bool:
  word = word.lower()
  return word == word[::-1]
