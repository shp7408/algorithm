package newcodingtest.week1.problem1;

import java.util.Arrays;

// n  보다 작은 소수의 개수를 출력하라
// -> 어떤 수의 배수는 소수가 아니므로, 범위 내에서 소수가 아닌, 수를 제외하는 방식
// 2의 배수 : 2, 4, 6, 8, 10, 12 ...
// 3의 배수 : 3, 6, 9, 12 ...

public class Solution {
    public int solution (int n) {
        int[] intArray = new int[n];

//        1로 초기화 (0, 1 제외)
//        -> 수들의 배열을 구하는 것이 아니라, 개수만 구하면 되므로,
//        {0, 0, 1, 1, 0, 1} -> 2, 3, 5 (index) :  가 바로 구하고자 하는 수임.
//        위 배열의 원소들의 합만 구하면, 소수의 개수를 구할 수 있음.
//
        for (int i = 2; i < n; i++) {
            intArray[i] = 1;
        }

//        sqrt(n) 까지만 반복
//        java.lang.Math 클래스의 sqrt(n) 메소드 : 특정값 n 의 제곱근 구하기
//        16 이하의 소수를 구한다 -> 16의 제곱근인 4 이하의 숫자들의 배수만 확인하면 된다.
        for (int i = 2; i < (int)Math.sqrt(n); i++) {
            if (intArray[i] == 0) continue; // 이미 검사된 숫자의 배수는 무의미
            int num = i * 2;
            while (num < n) {
                intArray[num] = 0;
                num += i;
            }
        }


        return Arrays.stream(intArray).sum();
    }
}

class Test {
    public static void main(String[] args) {

    }
}
