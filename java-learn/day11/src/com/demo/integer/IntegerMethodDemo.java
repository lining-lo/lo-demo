package com.demo.integer;

public class IntegerMethodDemo {
    /*
        Integer类的常见方法:

            public static String toBinaryString(int i)      得到二进制
            public static String toOctalString(int i)       得到八进制
            public static String toHexString(int i)         得到十六进制
            public static int parseInt(String s)            将字符串类型的整数转成int类型的整数

     */
    public static void main(String[] args) {
        System.out.println(Integer.toBinaryString(12));
        System.out.println(Integer.toOctalString(12));
        System.out.println(Integer.toHexString(12));

        int i = Integer.parseInt("123");
        System.out.println(i + 100);

        String s = "gugugaga";

        // Character中不存在 parseXxx方法, 其它的包装类都有.

        char c = s.charAt(0);
        char[] charArray = s.toCharArray();
        System.out.println(c);
        System.out.println(charArray);

    }
}
