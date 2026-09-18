package com.demo.recursion;

public class RecursionDemo1 {
    /*
        递归: 方法直接或者间接调用本身

        递归如果没有控制好终止，会出现递归死循环，导致栈内存溢出现象
     */
    public static void main(String[] args) {
        methodA();
    }

    public static void methodA() {
        methodB();
    }

    public static void methodB() {
        methodC();
    }

    public static void methodC() {
        methodA();
    }
}
