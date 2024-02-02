class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_p = 0
        abbr_p = 0

        while abbr_p < len(abbr) and word_p < len(word):
            if abbr[abbr_p].isalpha():
                if word[word_p] != abbr[abbr_p]:
                    return False
                abbr_p+=1
                word_p+=1
            else:
                num = abbr[abbr_p]
                if num == '0':
                    return False
                
                abbr_p += 1
            
                while abbr_p < len(abbr) and abbr[abbr_p].isnumeric():
                    num += abbr[abbr_p]
                    abbr_p+=1
                
                word_p+= int(num)
        
        return word_p == len(word) and abbr_p == len(abbr)
