package ch04_condition;

public class Exercise04_09 {
    public static void main(String[] args) {
        String str = "12345";
        int sum = 0;


        for (int i=0; i<str.length(); i++) {
            sum += str.charAt(i) - '0';
        }
        System.out.println("sum="+sum);
    }
}
