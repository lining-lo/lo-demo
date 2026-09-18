package com.demo.system;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class SystemDemo {
    /*
        System类常见方法 :

            1. public static void exit (int status) : 终止当前运行的 Java 虚拟机，非零表示异常终止
            2. public static long currentTimeMillis () : 返回当前系统的时间毫秒值形式
                                                                - 返回1970年1月1日 0时0分0秒, 到现在所经历过的毫秒值
                                                                - 返回1970年1月1日 8时0分0秒, 到现在所经历过的毫秒值

            3. public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length) : 数组拷贝

                                                        1. 数据源数组
                                                        2. 起始索引
                                                        3. 目的地数组
                                                        4. 起始索引
                                                        5. 拷贝的个数
     */
    public static void main(String[] args) {
        int[] arr1 = {11, 22, 33, 44, 55};
        int[] arr2 = new int[3];

        System.arraycopy(arr1, 1, arr2, 0, 3);

        for (int i : arr2) {
            System.out.println(i);
        }
    }

    private static void method() {
        long start = System.currentTimeMillis();

        String s = "";

        for (int i = 1; i <= 100000; i++) {
            s += i;
        }

        System.out.println(s);


        long end = System.currentTimeMillis();

        System.out.println(end - start);
    }
}
