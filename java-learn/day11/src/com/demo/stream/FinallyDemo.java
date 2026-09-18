package com.demo.stream;

public class FinallyDemo {
    /*
        finally 代码块: 被它包裹的代码一定会执行.
     */
    public static void main(String[] args) {
        method();
    }

    public static void method() {
        System.out.println("开始");

        try {
            System.out.println(10 / 2);
            // System.exit(0);
            return;
        } finally {
            System.out.println("看看我执行了吗?");
        }

        // System.out.println("结束");
    }
}
