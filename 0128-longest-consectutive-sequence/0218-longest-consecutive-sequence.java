class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;
        Set<Integer> set = new HashSet();
        //populate the set with the input array
        for(int num : nums) set.add(num);

        //iterate through the input array, check if element denotes the start of a sequence
        for( int num : nums) {
            //start of sequence is found
            if(!set.contains(num-1)) {
                int length = 1;
                //check how many numbers are there in this sequence
                while(set.contains(num + length)) {
                    length++;
                }

                //update max length
                max = Math.max(max, length);
            }
        }

        return max;
    }
}