package com.demo.exception;

public class ExceptionDemo2 {
    /*
        异常处理方式1

        try {
            ...
        } catch (异常类名 对象名) {
            ...
        }

        执行流程:
        1. 执行try语句中的代码, 看是否有异常发生
        2. 有的话, catch捕获异常, 执行内部的异常处理代码
        3. 没有的话, 不会执行catch内部代码, 程序继续执行.
     */
    public static void main(String[] args) {
        System.out.println("开始");

        try {
            int i = 1 / 1;

            int[] arr = new int[10];

            System.out.println(arr[10]);

        } catch (ArithmeticException e) {       // ArithmeticException e = new ArithmeticException();
            System.out.println("捕获了运算异常...");
        } catch (NullPointerException e) {      // NullPointerException e = new NullPointerException();
            System.out.println("捕获了空指针异常...");
        } catch (Exception e) {                 // Exception e = new ArrayIndexOutOfBoundsException();
            System.out.println("捕获了其它异常...");
        }

        System.out.println("结束");
    }
}
