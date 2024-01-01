class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int cookies = s.length;
        if (cookies == 0) return 0;

        Arrays.sort(g);
        Arrays.sort(s);

        int curr = 0;
        int content = 0;

        for (int i = 0; i < g.length; i++) {
            while (s[curr] < g[i]) {
                curr++;
                if (curr == cookies) return content;
            }

            content++;
            curr++;
            if (curr == cookies) return content;
        }

        return content;
    }
}
