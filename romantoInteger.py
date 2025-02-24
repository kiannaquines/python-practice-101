class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        final_value = 0
        prev_value = 0
        
        for i in reversed(s):
            
            current_value = roman[i]
            
            if current_value >= prev_value:
                final_value += current_value
            else:
                final_value -= current_value
            
            prev_value = current_value
            
        return final_value


solution = Solution()
print(solution.romanToInt('III'))
print(solution.romanToInt('IV'))
print(solution.romanToInt('IX'))
print(solution.romanToInt('LVIII'))
print(solution.romanToInt('MCMXCIV'))
print(solution.romanToInt('MMXXI'))
print(solution.romanToInt('MMXX'))
print(solution.romanToInt('MMX'))
print(solution.romanToInt('MM'))
print(solution.romanToInt('M'))        