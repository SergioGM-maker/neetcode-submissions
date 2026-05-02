class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
   
        HashMap<String, List<String>> mapa = new HashMap<>();

        for (String s : strs) {
            char[] c = s.toCharArray();
            Arrays.sort(c);
            String key = new String(c);

            mapa.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }     
        return new ArrayList<>(mapa.values());
    }
}
