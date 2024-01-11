## Approach

The first three operations the question asks us to do are standard O(1) operations on stacks. These can be easily executed using a list in Python or a LinkedList in java. 

The one function to think about is  `getMin()`. Intuitively, getMin() means that we need to track what the minimum value is at each level of the stack. The best way to do that is to have another stack implementation : let's call it `minStack`. 

`minStack` should be updated whenever the original element stack is. When a new element `val` is added to the original stack, we check what the minimum is before the insertion in `minStack` (let that be called `min`). We then push the smaller of the two i.e. the new minimum value at this stage to `minStack`.

`minStack` should also be updated when an element is popped from the original stack. Just remove the element at the top of `minStack` as well. 

## Complexity
- Time complexity: $O(1)$
O(1) for each operation.

- Space complexity: $O(n)
O(n) - the minimum values stack takes up O(n) auxiliary space.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code

Java
```java
class MinStack {
    List<Integer> stack;
    List<Integer> minStack;
    int len;

    public MinStack() {
        stack = new ArrayList();
        minStack = new ArrayList();
        len = 0;
    }
    
    public void push(int val) {
        stack.add(val);

        if(len != 0) minStack.add(Math.min(val, minStack.get(len-1)));
        else minStack.add(val);

        len++;
    }
    
    public void pop() {
        stack.remove(len-1);
        minStack.remove(len-1);
        len--;
    }
    
    public int top() {
        return stack.get(len-1);
    }
    
    public int getMin() {
        return minStack.get(len-1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

Python3
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```