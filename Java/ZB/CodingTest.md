```
// 1, 2, 3, 4 를 이용하여 세 자리 자연수를 만드는 방법 (순서 X, 중복 X)의 각 결과를 출력
public class Main {
    int solution(int[] d, int budget){
        int answer = 0;

        boolean[] visited = new boolean[d.length];

//        for (int i = d.length; i == 0; i--) { // r 큰수부터 정하기
//
//        }


        combination(d, visited, 0, d.length, d.length-1);

        return answer;
    }

    void combination(int[] arr, boolean[] visited, int depth, int n, int r) {

        int[] resultArr = new int[visited.length];

        if (r == 0) {
            for (int i = 0; i < n; i++) {
                if (visited[i]) {
                    System.out.print(arr[i] + " ");
//                    resultArr[i] = arr[i];
                }
            }
            System.out.println();
            return;
        }

        if (depth == n) {
            return;
        }
        visited[depth] = true;
        combination(arr, visited, depth + 1, n, r-1 );

        visited[depth] = false;
        combination(arr, visited, depth + 1, n, r);

    }

    public static void main(String[] args) {
//        Test code
        int[] arr = {1, 3, 2, 5, 4};

        Main p = new Main();
        int r = p.solution(arr, 9);
        System.out.println("result 1 :" + r);

        int[] arr2 = {2, 2, 3, 3};
        r = p.solution(arr2, 4);
        System.out.println("result 1 :" + r);
    }
}

```

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
<br>

### 2차 1번
```
```
<br>

### 2차 2번
```
```
<br>

### 2차 3번
```
import java.util.ArrayList;

class Solution {
    public String sol(String code) {
        String answer = code;

        char[] codeChars = code.toCharArray();
        ArrayList<Character> list = new ArrayList<>();
        for (char c : codeChars) {
            list.add(c);
        }

        int lastOpenIndex = list.lastIndexOf('{'); // 문자열에서 가장 마지막에 나오는 { 의 인덱스
        int firstCloseIndex = answer.length()  - list.indexOf('}'); // 문자열에서 가장 처음 나오는 { 의 인덱스

        ArrayList<Character> replaceArr = new ArrayList<>();
        char numChar = list.get(lastOpenIndex - 1); // 반복하려는 숫자의 char형
        int numInt = Character.getNumericValue(numChar); // 반복 수

        for (int i = 0; i < firstCloseIndex - lastOpenIndex - 1; i++) {
            replaceArr.add(list.get(lastOpenIndex + 1));
            list.remove(lastOpenIndex);
        }
        list.remove(lastOpenIndex-1);

        for (int i = 0; i < numInt; i++) {
            for (int j = 0; j < replaceArr.size(); j++) {

                replaceArr.add(replaceArr.get(j));
            }
            list.add(firstCloseIndex + i, replaceArr.get(i));
        }


        return answer;
    }
    Solution() {}
}

public class Main {
    public static void main(String[] args) {

//        test code
        Solution solution = new Solution();
        System.out.println("============= 1 번");
        String testStrs = "5{he2{l}o}friend";
        String result = "hellohellohellohellohellofriend";

        if (solution.sol(testStrs).equals(result)) {
            System.out.println("passsssss!!!! : ");
        } else {
            System.out.println("false!");
        }

        System.out.println("============= 2 번");
        testStrs = "de2{afew}w3{rq5{f}}";
        result = "deafewafewwrqfffffrqfffffrqfffff";
        if (solution.sol(testStrs).equals(result)) {
            System.out.println("passsssss!!!! : ");
        } else {
            System.out.println("false!");
        }

//        System.out.println("============= 3 번");
//        testStrs = new String[]{"12", "123", "1235", "567", "88"};
//        case1 = solution.sol(testStrs);
//        if (case1 == true) {
//            System.out.println("passsssss!!!! : " + case1);
//        } else {
//            System.out.println("false!" + case1);
//        }
        }
    }

```