### 20220818 1차 1번
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

```
class Solution {
    public String sol(int[] numbers) {
        String answer = "";

//        1. int to String
        for (int i = 0; i < numbers.length; i++) {

        }

//        2. 원소들끼리 문자열 결합 -> 원소가 n개인 경우, 경우의 수? = 

        return  answer;
    }


    Solution() {}
}

public class Main {
    public static void main(String[] args) {

//        test code
        Solution solution = new Solution();
        System.out.println("============= 1 번");

        int[] array1 = new int[]{6, 10, 2};
        String return1 = "6210";

        String answer = solution.sol(array1);
        if (answer.equals(return1)) {
            System.out.println("passsssss!!!! : " + answer);
        } else {
            System.out.println("false!" + answer);
        }

        System.out.println("============= 2 번");

        array1 = new int[]{3, 30, 34, 5, 9};
        return1 = "9534330";

        answer = solution.sol(array1);
        if (answer.equals(return1)) {
            System.out.println("passsssss!!!! : " + answer);
        } else {
            System.out.println("false!" + answer);
        }


    }
}
```