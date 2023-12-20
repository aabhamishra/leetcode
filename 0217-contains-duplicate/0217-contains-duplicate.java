class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet set = new HashSet<Integer>();
        for(int i : nums) {
            if(set.contains(i)) return true;
            set.add(i);
        }
        return false;
    }
}