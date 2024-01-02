class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> res = new ArrayList();
        res.add(new ArrayList<Integer>());
        int size = 0;

        Map<Integer, Integer> freq = new HashMap();

        for(int num : nums) {
            int frequency = freq.getOrDefault(num, 0);
            freq.put(num, frequency + 1);

            if(size >= frequency) {
                res.get(frequency).add(num);
            } else {
                List<Integer> l = new ArrayList<>();
                size++;
                l.add(num);
                res.add(l);
            }
        }

        return res;
    }
}