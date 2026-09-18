package com.demo.recursion;

public class RecursionDemo2 {
    /*
        需求: 使用递归求5的阶乘

        5的阶乘（5!）:  5 * 4 * 3 * 2 * 1

            5的阶乘（5!）:  5 * 4!
            4的阶乘（4!）:  4 * 3!
            3的阶乘（3!）:  3 * 2!
            2的阶乘（2!）:  2 * 1!
            1的阶乘（1!）:  1
     */
    public static void main(String[] args) {
        System.out.println(jc(5));
    }

    public static int jc(int num) {
        if (num == 1) {
            return 1;
        } else {
            // 思路: 需要调用一个方法, 获取4的阶乘
            // 5 * jc(4)
            // 4 * jc(3)
            // ...
            return num * jc(num - 1);
        }
    }
}
