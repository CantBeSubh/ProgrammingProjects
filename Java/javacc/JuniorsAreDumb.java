import java.util.Scanner;

public class JuniorsAreDumb {
    public static int getNthDigit(int integer, int position) {
        int totalDigits = countDigits(integer);
        int digitsFromTheRight = totalDigits - position;

        for (int i = 1; i <= digitsFromTheRight; i++) {
            integer /= 10;
        }

        return integer % 10;
    }

    public static int countDigits(int n) {
        int count = 0;
        while (n != 0) {
            n = n / 10;
            ++count;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Your mom hates you");
        System.out.println("Enter a positive integer: ");
        int integer = sc.nextInt();
        System.out.println("Enter the position where you wish to retrieve the digit: ");
        int position = sc.nextInt();
        int digit = getNthDigit(integer, position);

        System.out.println("You have entered: " + integer);
        if (digit % 2 == 0) {
            System.out.println("The digit at " + position + " position is " + digit + " and it is EVEN");
        } else {
            System.out.println("The digit at " + position + " position is " + digit + " and it is ODD");
        }
        sc.close();
    }
}
