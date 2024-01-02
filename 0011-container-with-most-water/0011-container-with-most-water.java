class Solution {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length - 1;
        int max = -1;

        while(start < end) {
            int s = height[start];
            int e = height[end];
            max = Math.max(Math.abs(end - start) * Math.min(s,e), max);
            if(s < e){
                while(start < end && height[start] <= s) start++;
            } else {
                while(start < end && height[end] <= e)end--;
            }
        }

        return max;
    }
}