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
// 다시 작업 진행해야 함
import java.text.SimpleDateFormat;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;
import java.util.regex.Pattern;

enum Sex {
    MALE(3), FEMALE(4);
    private final int sexNum;
    Sex(int sexNum) {this.sexNum = sexNum;};
    public int getSexNum() {return sexNum;};
}

public class Main {
    public static void main(String[] args) {
        System.out.println("[주민등록번호 생성 프로그램]");

        int birthYear, birthMonth, birthDate, sexNum;
        StringBuilder result = new StringBuilder();

        do {
            System.out.print("출생년도를 입력해 주세요.(yyyy):");
            try {
                birthYear = new Scanner(System.in).nextInt();
//                checkDateNum(BirthDayType.YEAR, birthYear);
                String tmpStr = getNumForm(BirthDayType.YEAR, birthYear);
                result.append(tmpStr);
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        do {
            System.out.print("출생월을 입력해 주세요.(mm):");
            try {
                birthMonth = new Scanner(System.in).nextInt();

                checkDateNum(BirthDayType.MONTH, birthMonth);
                String tmpStr = String.format("%02d", getNumForm(BirthDayType.MONTH, birthMonth));

                result.append(tmpStr);
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        do {
            System.out.print("출생일을 입력해 주세요.(dd):");
            try {
                birthDate = new Scanner(System.in).nextInt();

                checkDateNum(BirthDayType.DATE, birthDate);
                String tmpStr = String.format("%02d", getNumForm(BirthDayType.DATE, birthDate));

                result.append(tmpStr);
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        String sc;
        do {
            System.out.print("성별을 입력해 주세요.(m/f):");
            try {
                sc = new Scanner(System.in).next();
                switch (sc) {
                    case "m":
                        sexNum = Sex.MALE.getSexNum();
                        break;
                    case "f":
                        sexNum = Sex.FEMALE.getSexNum();
                        break;
                    default:
                        System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
                        continue;
                }

                String tmpStr = String.format("%01d", sexNum);
                result.append("-").append(tmpStr);

                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);


//        6자리의 랜덤 숫자 생성
        StringBuilder rdStr6 = new StringBuilder();

        for (int i = 0; i < 6; i++) {
            Random rd = new Random();
            int tmp = rd.nextInt(9);
            String tmpStr = String.valueOf(tmp); // 0 ~ 9 의 숫자를 랜덤으로 뽑기
            rdStr6.append(tmpStr);
            System.out.println("rdStr6 = " + rdStr6);
        }
        result.append(rdStr6);

        System.out.println(result);
    }

    enum BirthDayType { // 3가지 타입 (년도, 월, 날짜)
        YEAR, MONTH, DATE, NONE;
    }

    static class BirthDayResult {
        private BirthDayType birthDayType;  // 3가지 타입 (년도, 월, 날짜)
        private int result2Int; // 2자리 수 결과

    }

    public static SimpleDateFormat getNumForm(BirthDayType birthDayType, int dateNum) {

        try {
            SimpleDateFormat sdf;
            String pattern;
            switch (birthDayType.ordinal()) {
                case 0:
                    pattern = "yy";
                    break;
                case 1:
                    pattern = "MM";
                    break;
                case 2:
                    pattern = "dd";
                    break;
                default:
                    throw new IllegalStateException("Unexpected value: " + birthDayType.ordinal());
            }

            sdf = new SimpleDateFormat(pattern);
            sdf.format(dateNum);
            System.out.println("========" + sdf.);
            return sdf;

        } catch (Exception e) {
            throw e;
        }

    }

    public static void checkDateNum(BirthDayType birthDayType, int checkDate) {
        try {
            System.out.println("checkDate = " + checkDate);
            BirthDayResult bdr = new BirthDayResult();
            SimpleDateFormat sdf;
            String pattern;
            switch (birthDayType.ordinal()) {
                case 0:
                    pattern = "yyyy";
                    break;
                case 1:
                    pattern = "MM";
                    break;
                case 2:
                    pattern = "dd";
                    break;
                default:
                    throw new IllegalStateException("Unexpected value: " + birthDayType.ordinal());
            }

            sdf = new SimpleDateFormat(pattern);

        } catch (Exception e) {
            throw e;
        }
    }
}

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
