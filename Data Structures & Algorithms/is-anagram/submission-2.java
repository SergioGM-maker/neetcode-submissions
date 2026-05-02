class Solution {
    public boolean isAnagram(String s, String t) {
        boolean sol = true;

        while(!s.isEmpty() && sol){
            if(t.contains(String.valueOf(s.charAt(0)))){

                t= t.substring(0, t.indexOf(s.charAt(0))) + t.substring(t.indexOf(s.charAt(0))+1);



                s= s.substring(1);



            }else {
                sol=false;
            }
        }

        if(!t.isEmpty()){
            sol=false;
        }

        return sol;
    }
}
