class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        index = 0

        for num in range(1, len(number)):
            if number[num-1] == digit:
                if int(number[num]) > int(number[num-1]):
                    # we have found the number to return
                    return number[:num-1] + number[num:]
                else:
                    index = num - 1

        if number[-1] == digit:
            index = len(number) - 1

        return number[:index] + number[index+1:]