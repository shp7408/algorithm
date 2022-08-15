### 20220815_08
```
```

### 20220815_07
```
import java.util.*;

class Lotto {
    public int one;
    public int two;
    public int three;

    public int four;
    public int five;
    public int six;

    public int numOfSameNum;

    public Lotto() {
    }

    public Lotto(int one, int two, int three, int four,int five, int six) {
        this.one = one;
        this.two = two;
        this.three = three;
        this.four = four;
        this.five = five;
        this.six = six;
    }

    public Lotto(int one, int two, int three,int four, int five, int six, int numOfSameNum) {
        this.one = one;
        this.two = two;
        this.three = three;
        this.four = four;
        this.five = five;
        this.six = six;
        this.numOfSameNum = numOfSameNum;
    }

    // 정렬
    public Lotto sortLottoNumber() {

        int[] ints = new int[]{this.one, this.two, this.three, this.four, this.five, this.six};
        Arrays.sort(ints);
        Lotto printLotto = new Lotto(ints[0], ints[1], ints[2], ints[3], ints[4], ints[5]);

        return printLotto;
    }

    public int getLottoRandomNumber() {
        Random rd = new Random();
        int tmp = rd.nextInt(45) + 1; // (0 ~ 45) + 1 범위 내
        return tmp;
    }

    public void setAllRandomNumber() {
        this.one = this.getLottoRandomNumber();
        this.two = this.getLottoRandomNumber();
        this.three = this.getLottoRandomNumber();;
        this.four = this.getLottoRandomNumber();
        this.five = this.getLottoRandomNumber();
        this.six = this.getLottoRandomNumber();
    }
    
    public void compareToNumbers(Lotto resultLotto) {
        int[] ints = new int[]{this.one, this.two, this.three, this.four, this.five, this.six};
        int[] resultInts = new int[]{resultLotto.one, resultLotto.two, resultLotto.three, resultLotto.four, resultLotto.five, resultLotto.six};

        int returnSameNum = 0;

        for (int i = 0; i < ints.length; i++) {
            for (int j = 0; j < resultInts.length; j++) {
                if (ints[i] == resultInts[j]) {
                    returnSameNum++;
                }
            }
        }
        this.numOfSameNum = returnSameNum;
    }
}

public class JavaAssignment7 {
    public static void main(String[] args) {
        System.out.println("[로또 당첨 프로그램]\n");

        int inputTimes;

        ArrayList<Lotto> lottoArrayList = new ArrayList<>();

        Lotto resultLotto = new Lotto();
        resultLotto.setAllRandomNumber();
        resultLotto = resultLotto.sortLottoNumber();

        do {
            try {
                System.out.print("로또 개수를 입력해 주세요.(숫자 1 ~ 10):");
                inputTimes = new Scanner(System.in).nextInt();
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        char[] chars = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'};

        for (int i = 0; i < inputTimes; i++) {
            Lotto lotto = new Lotto();
            lotto.setAllRandomNumber();
            lotto = lotto.sortLottoNumber();

            lotto.compareToNumbers(resultLotto);
            lottoArrayList.add(lotto);

            System.out.printf("%c\t %02d, %02d, %02d, %02d, %02d, %02d\n", chars[i], lotto.one, lotto.two, lotto.three, lotto.four, lotto.five, lotto.six);
        }

        System.out.println("\n[로또 발표]");
        System.out.printf("\t %02d, %02d, %02d, %02d, %02d, %02d ", resultLotto.one, resultLotto.two, resultLotto.three, resultLotto.four, resultLotto.five, resultLotto.six);


        System.out.println("\n[내 로또 결과]");
        for (int i = 0; i < inputTimes; i++) {
            Lotto lotto = lottoArrayList.get(i);
            System.out.printf("%c\t %02d, %02d, %02d, %02d, %02d, %02d => %d 개 일치\n", chars[i], lotto.one, lotto.two, lotto.three, lotto.four, lotto.five, lotto.six, lotto.numOfSameNum);
        }

    }
}
```

### 20220815_06
```
import java.util.*;

enum CandidateEnum {
    LJM(1, "이재명"),
    YSY(2, "윤석열"),
    SSJ(3, "심상정"),
    ACS(4, "안철수");
    private final int candidateNum;
    private final String candidateName;

    private int voteCounts;

    CandidateEnum(int candidateNum, String candidateName ) {
        this.candidateNum = candidateNum;
        this.candidateName = candidateName;
    }

    public int getCandidateNum() {
        return this.candidateNum;
    }

    public String getCandidateName() {
        return this.candidateName;
    }

    public static CandidateEnum valueOfNumber(int candidateNum) {
        return Arrays.stream(values())
                .filter(value -> Objects.equals(value.candidateNum, candidateNum))
                .findFirst()
                .orElseThrow(()-> new IllegalArgumentException(String.format("%d는 유효한 번호가 아닙니다.",  candidateNum)));
    }

    public void plusVoteCount(){
        this.voteCounts++;
    }

    public int getVoteCounts() {
        return this.voteCounts;
    }

}


public class JavaAssignment6 {
    public static void main(String[] args) {
        int allVotes = 10000;
        double nowProgressPercent;
        int rdInt;

        for (int i = 1; i < allVotes + 1; i++) {
            Random rd = new Random();//랜덤 객체 생성
            rdInt = rd.nextInt(4);
            int candiRdInt = rdInt + 1;
            System.out.println(rdInt);

            CandidateEnum candidate = CandidateEnum.valueOfNumber(candiRdInt);
            candidate.plusVoteCount();

            nowProgressPercent = (double) i / allVotes * 100;
            System.out.printf("[투표진행율]: %.2f%%, %d명 투표 => %s\n", nowProgressPercent, i, candidate.getCandidateName());

            System.out.printf("[기호:%d] %s: %.2f%%, (투표수: %d)\n",
                    CandidateEnum.LJM.getCandidateNum(),
                    CandidateEnum.LJM.getCandidateName(),
                    (double) CandidateEnum.LJM.getVoteCounts() / i * 100,
                    CandidateEnum.LJM.getVoteCounts()
            );
            System.out.printf("[기호:%d] %s: %.2f%%, (투표수: %d)\n",
                    CandidateEnum.YSY.getCandidateNum(),
                    CandidateEnum.YSY.getCandidateName(),
                    (double) CandidateEnum.YSY.getVoteCounts() / i* 100,
                    CandidateEnum.YSY.getVoteCounts()
            );
            System.out.printf("[기호:%d] %s: %.2f%%, (투표수: %d)\n",
                    CandidateEnum.SSJ.getCandidateNum(),
                    CandidateEnum.SSJ.getCandidateName(),
                    (double) CandidateEnum.SSJ.getVoteCounts() / i* 100,
                    CandidateEnum.SSJ.getVoteCounts()
            );
            System.out.printf("[기호:%d] %s: %.2f%%, (투표수: %d)\n",
                    CandidateEnum.ACS.getCandidateNum(),
                    CandidateEnum.ACS.getCandidateName(),
                    (double) CandidateEnum.ACS.getVoteCounts() / i* 100,
                    CandidateEnum.ACS.getVoteCounts()
            );
        }

        CandidateEnum[] allCandidates = CandidateEnum.values();
        Arrays.sort(allCandidates, Comparator.comparing(CandidateEnum::getVoteCounts));

        CandidateEnum result = null; // 당선인
        for (CandidateEnum candidateEnum: allCandidates) {
            result = candidateEnum;
        }

        System.out.printf("[투표결과] 당선인 : %s", result.getCandidateName());
    }
}


```

### 20220815_05
```
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.YearMonth;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int inputYear, inputMonth;
        System.out.println("[달력 출력 프로그램]");
        do {
            System.out.print("달력의 년도를 입력해 주세요.(yyyy):");
            try {
                inputYear = new Scanner(System.in).nextInt();
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        do {
            System.out.print("달력의 월을 입력해 주세요.(mm):");
            try {
                inputMonth = new Scanner(System.in).nextInt();
                break;
            } catch (InputMismatchException e) {
                System.out.println("유효하지 않은 값입니다. 다시 값을 입력해주세요.");
            }
        } while (true);

        String resultDate = "[" + inputYear+"년 "+ String.format("%02d", inputMonth) +"월]";
        System.out.println(resultDate);

//        해당월의 첫째날 date
        LocalDate date = LocalDate.of(inputYear, inputMonth, 1);

//      해당 월의 1일의 요일 구하기
        DayOfWeek dayOfWeek = date.getDayOfWeek();

//        YearMonth 객체 생성
        YearMonth yearMonth = YearMonth.from(date);

//        해당 월의 일 수(int)
        int lenthOfMonth = yearMonth.lengthOfMonth();

//        월, 화, 수 ... 일
        System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n","월","화","수","목","금","토","일");

//        해당 월의 날짜 array ["01", "02" ... "31"]
        ArrayList<String> datesArray = new ArrayList<>();
        for (int i = 1; i < lenthOfMonth + 1 ; i++) {
            datesArray.add(String.format("%02d", i));
        }

        if (dayOfWeek != DayOfWeek.SUNDAY) { // 해당 월의 1일이 일요일이 아닌 경우,
            for (int i = 0; i < dayOfWeek.ordinal() + 1 ; i++) {
                datesArray.add(0, "  ");
            }
        }

//        날짜들 배열 출력
        for (int i = 0; i < datesArray.size(); i++) {
            int j = i + 1;
            if (j % 7 == 0) {
                System.out.printf("%s\t\n", datesArray.get(i));
            } else {
                System.out.printf("%s\t", datesArray.get(i));
            }
        }
    }
}


```

### 20220815_04
```
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

enum Sex {
    MALE(3), FEMALE(4);
    private final int sexNum;
    Sex(int sexNum) {this.sexNum = sexNum;};
    public int getSexNum() {return sexNum;};
}

class InputBirtDay {
    public int userInput; // 사용자 입력값
    public BirthDayType birthDayType; // 3가지 타입 (년도, 월, 날짜)

    InputBirtDay(int _userInput, BirthDayType _birthDayType){
        this.userInput = _userInput;
        this.birthDayType = _birthDayType;
    }

    public String printResultOuput() {
        String resultOutput;

        switch (birthDayType.ordinal()) {
            case 0:
                resultOutput = String.valueOf(userInput);
                resultOutput = resultOutput.substring(resultOutput.length()-2);
                break;
            case 1:
            case 2:
                resultOutput = String.format("%02d", userInput);
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + birthDayType.ordinal());
        }


        return resultOutput;
    }
}

enum BirthDayType { // 3가지 타입 (년도, 월, 날짜)
    YEAR, MONTH, DATE, NONE;
}

public class JavaAssignment4 {
    public static void main(String[] args) {
        System.out.println("[주민등록번호 생성 프로그램]");

        int birthYear, birthMonth, birthDate, sexNum;
        StringBuilder result = new StringBuilder();

        do {
            System.out.print("출생년도를 입력해 주세요.(yyyy):");
            try {
                birthYear = new Scanner(System.in).nextInt();
                InputBirtDay inputBirtDay = new InputBirtDay(birthYear, BirthDayType.YEAR);
                String tmpStr = inputBirtDay.printResultOuput();
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

                InputBirtDay inputBirtDay = new InputBirtDay(birthMonth, BirthDayType.MONTH);
                String tmpStr = inputBirtDay.printResultOuput();
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

                InputBirtDay inputBirtDay = new InputBirtDay(birthDate, BirthDayType.DATE);
                String tmpStr = inputBirtDay.printResultOuput();
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
        }
        result.append(rdStr6);

        System.out.println(result);
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
