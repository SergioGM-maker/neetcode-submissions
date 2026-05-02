class Solution {
    public boolean isAnagram(String s, String t) {

        while(!s.isEmpty()){
            if(t.contains(String.valueOf(s.charAt(0)))){
                t= t.substring(0, t.indexOf(s.charAt(0))) + t.substring(t.indexOf(s.charAt(0))+1);
                s= s.substring(1);
                }else {
                return false;
            }
        }
        if(!t.isEmpty()){
            return false;
        }
        return true;
    }
}
