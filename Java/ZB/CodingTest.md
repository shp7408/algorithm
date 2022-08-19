```
class Solution {
    public int sol(int n) {
        int answer = 0;

        int count;
        int allCount = 0;

        for (int i = 2; i < n; i ++) {
            count = 0;
            for (int j = 2; j < i; j++) {
                if (i % j == 0)
                    count++;
            }
            if (count == 0)
                allCount++;
        }
        answer = allCount;

        return answer;
    }


    Solution() {}
}

public class Main {
    public static void main(String[] args) {

//        test code
        Solution solution = new Solution();
        System.out.println("============= 1 번");
        int case1 = solution.sol(15);
        if (case1 == 6) {
            System.out.println("good! case1 : " + case1);
        } else {
            System.out.println("false!" + case1);

        }
        System.out.println("============= 2 번");
        int case2 = solution.sol(20);
        if (case2 == 8) {
            System.out.println("good! case2 : " + case2);
        } else {
            System.out.println("false!" + case2);
        }

    }
}


```