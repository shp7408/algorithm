import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p, k, r = 0;
        p = sc.nextInt();
        k = sc.nextInt();
        for (int i = k; i <= p; i++) {
            r++;
        }
        System.out.println(r);
    }
}
