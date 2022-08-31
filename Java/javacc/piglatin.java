import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class piglatin {
    public static void main(String[] args) {
        String word, final_str;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String:");
        word = sc.nextLine();
        int i = 0, pos = 0;
        List<Character> chars = new ArrayList<>();
        for (char ch : word.toCharArray()) {

            chars.add(ch);
        }
        if (chars.get(0) == 'a' || chars.get(0) == 'e' || chars.get(0) == 'i' || chars.get(0) == 'o'
                || chars.get(0) == 'u') {
            final_str = word + "ay";
        } else if (chars.get(0) == 'y') {
            for (i = 0; i < word.length(); i++) {
                if (chars.get(i) == 'a' || chars.get(i) == 'e' || chars.get(i) == 'i' || chars.get(i) == 'o'
                        || chars.get(i) == 'u') {
                    pos = i;
                    break;
                }
            }
            // StringBuilder sb = new StringBuilder(word);
            final_str = word.substring(pos);
            final_str = final_str + word.substring(0, pos) + "ay";
        } else {
            for (i = 0; i < word.length(); i++) {
                if (chars.get(i) == 'a' || chars.get(i) == 'e' || chars.get(i) == 'i' || chars.get(i) == 'o'
                        || chars.get(i) == 'u' || chars.get(i) == 'y') {
                    pos = i;
                    break;
                }
            }
            StringBuilder sb = new StringBuilder(word);
            final_str = word.substring(pos);
            final_str = final_str + word.substring(0, pos) + "ay";
        }
        System.out.println(final_str);
        sc.close();
    }
}
