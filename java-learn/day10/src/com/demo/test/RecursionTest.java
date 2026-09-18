package com.demo.test;

public class RecursionTest {
    /*
        有一对兔子，从出生后第3个月起每个月都生一对兔子
        小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问第二十个月的兔子对数为多少？

        规律: 从第三个月开始，兔子的对数是前两个月相加的和
     */
    public static void main(String[] args) {
        System.out.println(get(20));
    }

    public static int get(int month) {
        // 第一个, 第二个月兔子的对数为1
        if (month == 1 || month == 2) {
            return 1;
        } else {
            // 第三个月: 第一个月 + 第二个月  month 3
            // 第四个月: 第二个月 + 第三个月  month 4
            // ...
            return get(month - 2) + get(month - 1);
        }
    }
}
