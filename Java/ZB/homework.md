### 20220815_08
```
```

### 20220815_07
```
```

### 20220815_06
```
```

### 20220815_05
```
```

### 20220815_04
```
```

### 20220815_03
```
import java.util.InputMismatchException;
import java.util.Scanner;

enum TicketPrice {
    FREE_PRICE(0),
    DEFAULT_PRICE(10000),
    SPECIAL_DISCOUNT(4000),
    GENERAL_DISCOUNT(8000);

    private final int price;
    TicketPrice(int price) {this.price = price;}
    public int getPrice() {return price;}
}

public class JavaAssignment3 {
    public static void main(String[] args) {
        System.out.println("[입장권 계산]");

        int price;
        int age, time;
        boolean is_national_merit = false, is_welfare_card = false;

        do {
            System.out.print("나이를 입력해 주세요.(숫자):");
            try {
                age = new Scanner(System.in).nextInt();
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        do {
            System.out.print("입장시간을 입력해 주세요.(숫자입력):");
            try {
                time = new Scanner(System.in).nextInt();
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        String sc2;

        do {
            System.out.print("국가유공자 여부를 입력해 주세요.(y/n):");
            sc2 = new Scanner(System.in).next(); // Scanner 클래스 다시 생성해야 함
            switch (sc2) {
                case "y":
                    is_national_merit = true;
                    break;
                case "n":
                    break;
                default:
                    System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
                    continue;
            }
            break;
        } while (true);

        do {
            System.out.print("복지카드 여부를 입력해 주세요.(y/n):");
            sc2 = new Scanner(System.in).next(); // Scanner 클래스 다시 생성해야 함

            switch (sc2) {
                case "y":
                    is_welfare_card = true;
                    break;
                case "n":
                    break;
                default:
                    System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
                    continue;
            }
            break;
        } while (true);

        if (age < 3) { // 3세 미만 무료
            price = TicketPrice.FREE_PRICE.getPrice();
        } else if (age < 13) { // 13세 미만
            price = TicketPrice.SPECIAL_DISCOUNT.getPrice();
        } else { // 13세 이상
            price = TicketPrice.DEFAULT_PRICE.getPrice();
            // 국가유공자 여부, 복지카드 소유 여부
            if (is_national_merit || is_welfare_card) {
                price = TicketPrice.GENERAL_DISCOUNT.getPrice();
            }
            // 입장시간 17시 이후
            if (time >= 17) {
                price = TicketPrice.GENERAL_DISCOUNT.getPrice();
            }
        }

        String result = "입장료:  " + price;
        System.out.println(result);
    }
}
```

### 20220815_02
```
import java.util.Scanner;

public class JavaAssignment2 {
    public static void main(String[] args) {
        System.out.print("[캐시백 계산]\n결제 금액을 입력해 주세요.(금액):");
        Scanner sc = new Scanner(System.in);
        int scInt = sc.nextInt();

        int price = scInt;
        double discount = 0.1; // 할인율 10 %
        int change;

        price = (int) (price * discount * 0.01); // 12000 -> 10%(0.1) -> 0.01 = 12

        if (price > 3) { // 최대 300원을 넘을 수 없다.
            change = 300;
        } else {
            change = price * 100; // 100원 단위로 보여주기 위함
        }
        String result = "결제 금액은 " + scInt + "이고, 캐시백은 " +change +  "원 입니다.";
        System.out.println(result);
    }
}
```

### 20220815_01
```
public class JavaAssignment1.java {
    public static void main(String[] args) {
        System.out.println("[구구단 출력]");
        for (int i = 1; i < 10; i++) {
            for (int j = 1; j < 10; j++) {

                String strI = String.format("%02d", i);
                String strJ = String.format("%02d", j);
                String strIJ = String.format("%02d", i*j);
                String all = strI + " x " + strJ + " = " + strIJ + "    ";

//              j (행) 이 9인 경우, 문자열 all 에 줄바꿈을 추가한다.
                if (j == 9) {
                    all = all + "\n";
                }

                System.out.print(all);
            }
        }
    }
}
```
