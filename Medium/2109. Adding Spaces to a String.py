class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        r=[]
        ix=0
        for i in range(len(s)):
            if ix<len(spaces) and i==spaces[ix]:
                r.append(" ")
                ix+=1
            r.append(s[i])
        return "".join(r)
    

# class Solution {
#     public String addSpaces(String s, int[] spaces) {
#         StringBuilder r = new StringBuilder();
#         int ss=0;
#         for(int i=0;i<s.length();i++){
#             if(ss<spaces.length && i==spaces[ss]){
#                 r.append(" ");
#                 ss++;
#             }
#             r.append(s.charAt(i));
#         }
#         return r.toString();
#     }
# }