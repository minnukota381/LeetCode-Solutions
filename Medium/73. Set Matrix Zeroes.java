class Solution {
    public void setZeroes(int[][] matrix) {
        int n=matrix.length;
        int m=matrix[0].length;

        int r[] = new int[n];
        int c[] = new int[m];

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(matrix[i][j]==0){
                    c[j]=1;
                    r[i]=1;
                }
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(r[i]==1 || c[j]==1){
                    matrix[i][j]=0;
                }
            }
        }
    }
}