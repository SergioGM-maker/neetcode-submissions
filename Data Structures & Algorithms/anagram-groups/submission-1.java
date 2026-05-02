class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> mapa = new HashMap<>(); 
        for(String s: strs){ 
            char[] c = s.toCharArray(); 
            Arrays.sort(c); 
            String llave = new String(c);
            if(mapa.get(llave)!=null){ 
                mapa.get(llave).add(s); 
                System.out.println(mapa.get(llave)); 
                }
            else{ 
                ArrayList<String> dis = new ArrayList<String>(); 
                dis.add(s); 
                mapa.put(llave,dis); 
                }

    }
    return new ArrayList<>(mapa.values());
}
}