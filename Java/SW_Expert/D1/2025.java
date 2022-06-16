import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int first, result;
        first = sc.nextInt();
        result = 0;
        for (int i = 1; i <= first; i ++){
            result = result + i;
        }
        System.out.println(result);
    }
}
