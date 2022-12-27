package D1;

import java.util.Scanner;

class SW2048 {
    public SW2048() {
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
