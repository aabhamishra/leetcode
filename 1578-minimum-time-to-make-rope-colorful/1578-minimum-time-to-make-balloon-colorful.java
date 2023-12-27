class Solution {
    public int minCost(String colors, int[] neededTime) {
        int time = 0;
        int first = 0;
        int second = 1;
        int len = colors.length();
        int i = 1;
        while( first < len && second < len) {
            if(colors.charAt(first) == colors.charAt(second)) {
                if(neededTime[first] <= neededTime[second]) {
                    time += neededTime[first];
                    first+=i;
                    i = 1;
                    second++;
                } else {
                    time += neededTime[second];
                    i++;
                    second++;
                }
            } else {
                first+=i;
                i = 1;
                second++;
            }
        }

        return time;
    }
}