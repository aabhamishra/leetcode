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