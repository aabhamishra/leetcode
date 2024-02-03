## Intuition
The `non_zero` attribute is a list of tuples, where each tuple represents a non-zero element in the sparse vector. Each tuple contains two elements: the index of the non-zero element and the value at that index. This approach efficiently captures the sparsity of the vector, as it only stores information about the non-zero elements.

While a dictionary could also be used to represent a sparse vector, there are reasons why the current approach might be preferable:

1. **Memory Efficiency**: Tuples generally have lower memory overhead compared to dictionary items. In the current approach, each non-zero element is stored in a tuple, which can be more memory-efficient than storing key-value pairs in a dictionary.

3. **Cache Locality**: Accessing consecutive elements in a list generally results in better cache locality compared to accessing elements in a dictionary, especially when the number of non-zero elements is relatively small.

## Approach

**Initialize Sparse Vector** 

In the `__init__` method, iterate through the input list `nums`, and for each non-zero element, store its index and value in the `non_zero` list.

**Calculate Dot Product**

- In the `dotProduct` method, initialize pointers `p1` and `p2` to iterate through the `non_zero` lists of both vectors. Use a `while` loop to traverse both lists simultaneously and calculate the dot product.

- If the indices at the current positions of both vectors are equal, multiply their values and add the result to the dot product. Increment both pointers.

- If the index of the first vector is greater than the index of the second vector, increment the second pointer. If the index of the second vector is greater, increment the first pointer.

- Return the calculated dot product.

## Complexity
- Time complexity:
`__init__` method: O(N), where N is the length of the input list `nums`.
`dotProduct` method: O(min(M, N)), where M and N are the lengths of the non-zero of the two sparse vectors.

- Space complexity: 
`__init__` method: O(N), where N is the number of non-zero elements in the input list `nums`.
`dotProduct` method: O(1) as no additional space is used other than pointers and variables.

## Code
```python
class SparseVector:

    def __init__(self, nums: List[int]):
        
        self.non_zero = []
        
        for i in range(len(nums)):
            if nums[i] != 0:
                self.non_zero.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1, p2 = 0, 0
        res = 0

        while p1 < len(self.non_zero) and p2 < len(vec.non_zero):
            if self.non_zero[p1][0] > vec.non_zero[p2][0]:
                p2+=1
            elif self.non_zero[p1][0] < vec.non_zero[p2][0]:
                p1+=1
            else:
                res += self.non_zero[p1][1] * vec.non_zero[p2][1]
                p1+=1
                p2+=1
            
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
```