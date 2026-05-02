// import java.util.*;

// class Solution {
//     public List<Integer> getRow(int rowIndex) {

//         List<List<Integer>> result = new ArrayList<>();

//         for (int i = 0; i <= rowIndex; i++) {

//             List<Integer> row = new ArrayList<>();
//             row.add(1);

//             for (int j = 1; j < i; j++) {
//                 List<Integer> prev = result.get(i - 1);
//                 int val = prev.get(j - 1) + prev.get(j);
//                 row.add(val);
//             }

//             if (i > 0) row.add(1);

//             result.add(row);
//         }

//         return result.get(rowIndex);
//     }
// }

import java.util.*;

class Solution {
    public List<Integer> getRow(int rowIndex) {

        List<Integer> row = new ArrayList<>();
        row.add(1);

        for (int i = 1; i <= rowIndex; i++) {

            List<Integer> newRow = new ArrayList<>();
            newRow.add(1);

            for (int j = 1; j < i; j++) {
                int val = row.get(j - 1) + row.get(j);
                newRow.add(val);
            }

            newRow.add(1);

            row = newRow; // move to next row
        }

        return row;
    }
}