class Solution {
    public boolean isAnagram(String s, String t) {
        if(t.length() != s.length()){
            return false;
        }
        while(!s.isEmpty() && t.contains(String.valueOf(s.charAt(0)))){
            t= t.substring(0, t.indexOf(s.charAt(0))) + t.substring(t.indexOf(s.charAt(0))+1);
            s= s.substring(1);
        }

        if(!t.isEmpty() || !s.isEmpty()){
            return false;
        }
        return true;
    }
}
