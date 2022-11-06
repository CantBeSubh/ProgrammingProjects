class inti {
    public static void main(String[] args) {
        // Integer x = 5, y = 10, z = 5;
        // Short a = 5;
        // // Returns byte primitive data type
        // System.out.println(x.byteValue());
        // // Returns double primitive data type
        // System.out.println(x.doubleValue());
        // // Returns long primitive data type
        // System.out.println(x.longValue());
        // System.out.println(x.compareTo(3));
        // System.out.println(x.compareTo(5));
        // System.out.println(x.compareTo(8));
        // System.out.println(x.equals(y));
        // System.out.println(x.equals(z));
        // System.out.println(x.equals(a));
        // Integer x = Integer.valueOf(9);
        // Double c = Double.valueOf(5);
        // Float a = Float.valueOf("80");
        // Integer b = Integer.valueOf("444", 16);
        // System.out.println(x);
        // System.out.println(c);
        // System.out.println(a);
        // System.out.println(b);
        double x = 11.635;
        double y = 2.76;
        System.out.printf("The value of e is %.4f%n", Math.E);
        System.out.printf("log(%.3f) is %.3f%n", x, Math.log(x));
        System.out.printf("The value of e is %.4f%n", Math.E);
        System.out.printf("exp(%.3f) is %.3f%n", x, Math.exp(x));
        System.out.println(Math.min(12.123, 12.456));
        System.out.println(Math.min(23.12, 23.0));
        System.out.println(Math.max(12.123, 12.456));
        System.out.println(Math.max(23.12, 23.0));
        double d = -100.675;
        float f = -90;
        System.out.println(Math.ceil(d)); // prints -100.0
        System.out.println(Math.ceil(f)); // prints -90.0
        System.out.println(Math.floor(d)); // prints -101.0
        System.out.println(Math.floor(f)); // prints -90.0
    }
}