class Solution {
    public boolean isPathCrossing(String path) {
        HashMap<Character, Pair<Integer, Integer>> moves = new HashMap();
        moves.put('N', new Pair(0, 1));
        moves.put('S', new Pair(0, -1));
        moves.put('W', new Pair(-1, 0));
        moves.put('E', new Pair(1, 0));
          
        HashSet<Pair<Integer, Integer>> visited = new HashSet<>();
        visited.add(new Pair(0, 0));

        int x = 0;
        int y = 0;

        for(Character move : path.toCharArray()) {
            x += moves.get(move).getKey();
            y += moves.get(move).getValue();

            if(visited.contains(new Pair(x,y))) return true;
            visited.add(new Pair(x, y));
        }

        return false;
    }
}