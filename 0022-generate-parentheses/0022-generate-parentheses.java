class Solution {

    List<String> res = new ArrayList();
    int total;

    public List<String> generateParenthesis(int n) {
        // dynamic programming
        total = n;
        dfs(0, 0, "");
        return res;
    }


    private void dfs(int open, int closed, String str) {
        if(open == closed && open == total) {
            res.add(str);
            return;
        }

        if(open < total) {
            dfs(open+1, closed, str+"(");
        }

        if(closed < open) {
            dfs(open, closed+1, str+")");
        }
    }
}