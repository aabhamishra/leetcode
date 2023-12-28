class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        # hashmap of counts already executed
        executed = {}

        # counts the minimum length of optimal compression 
        # i = current index
        # k = removals left
        # prev = character at i-1 index
        # prev_count = number of consecutive "prev" characters before i
        def count(i, k, prev, prev_count):
            # 3 base cases below:
            # 1. if this count is already calculated, just return
            if (i, k, prev, prev_count) in executed:
                return executed[(i, k, prev, prev_count)]
            # 2. if removals exceed what can be executed, return inf so that this iteration is dismissed
            if k < 0:
                return float("inf")
            # 3. if i reaches end of string
            if i == len(s): 
                return 0

            # recursive cases: 
            # 1. if current element equals previous
            if s[i] == prev:
                # check if this rle encoding will increase in length. this only happens for below previous counts 
                incr = 1 if prev_count in [1,9,99,9999,99999] else 0   
                # return recursive call for next element
                res = incr + count(i+1,k,s[i], prev_count+1)
            # 2. if current element does not equal previous aka new sequence is being started
            else:
                # return minimum of count if : (A) s[i] is deleted and (B) s[i] is kept
                res = min(
                    count(i+1, k-1, prev, prev_count), # s[i] deleted
                    1 + count(i+1, k, s[i], 1) # s[i] kept
                )
            
            executed[(i, k, prev, prev_count)] = res
            return res
        return count(0, k, "", 0)        

        """
        :type s: str
        :type k: int
        :rtype: int
        """


        