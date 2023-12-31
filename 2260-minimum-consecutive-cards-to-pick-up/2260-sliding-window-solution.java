class Solution {
    public int minimumCardPickup(int[] cards) {
        
        int len = cards.length;
        int min = Integer.MAX_VALUE;
        
        if(len == 1) return -1;
        
        int start = 0;
        int end = 0;
        
        Set<Integer> set = new HashSet();
        
        while(end < len) {
            if(!set.add(cards[end])) {
                int dupl = cards[end];
                // we have found a duplicate
                while(cards[start] != dupl) {
                    set.remove(cards[start]);
                    start++;
                }
                // we have the current minimum consecutive sequence
                min = Math.min(min, end-start+1);
                start++;
                
            }
            end++;
        }
        