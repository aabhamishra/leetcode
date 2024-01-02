class Solution {
    public int trap(int[] height) {
        int start = 0;
        int end = height.length - 1;
        int water = 0;

        while(start < end) {
            int s = height[start];
            int e = height[end];

            if(s <= e){
                
                start++;
                
                while(start < end && height[start] <= s){
                    water = water + s - height[start];
                    start++;
                } 
            }
            else{
                
                end--;

                while(start < end && height[end] <= e){
                    water = water + e - height[end];
                    end--;
                } 
            }
        }

        return water;
    }
}