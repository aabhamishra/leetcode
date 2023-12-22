class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groups = new HashMap<String, List<String>>();
        for( String s: strs ) {
            //convert string to char array, arrange alphabetically, and convert back to string
            char[] sArr = s.toCharArray();
            Arrays.sort(sArr);
            String sAlpha = String.valueOf(sArr);

            List<String> l = groups.getOrDefault(sAlpha, new ArrayList<String>());
            l.add(s);
            groups.put(sAlpha, l);
        }

        return new ArrayList<>(groups.values());
    }
}