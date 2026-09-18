package com.demo.exception;

public class ExceptionDemo1 {
    /*
        异常默认的处理方式: 向上抛出
     */
    public static void main(String[] args) {
        System.out.println("main方法开始执行...");
        method();                   // ③ main方法接收到异常对象, 继续向上抛出 new ArithmeticException();
                                    // ④ JVM虚拟机接收到异常对象, 将异常的错误信息打印在控制台, 将程序停止.
        System.out.println("main方法执行结束...");
    }

    private static void method() {
        System.out.println("method方法开始...");
        int i = 1 / 0;              // ① 会在出现异常的位置, 创建一个异常对象  new ArithmeticException();
                                    // ② 将异常对象向上抛出, 抛给main方法
        System.out.println("method方法结束...");
    }
}
