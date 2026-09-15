package com.demo.lambda;

public class LambdaTest2 {
    public static void main(String[] args) {
        useStringHandler(new StringHandler() {
            @Override
            public void printMessage(String msg) {
                System.out.println("匿名内部类打印的:" + msg);
            }
        });

        useStringHandler(msg ->
            System.out.println("Lambda表达式打印的:" + msg)
        );
    }

    /*
        StringHandler stringHandler = new StringHandler() {
            @Override
            public void printMessage(String msg) {
                System.out.println("匿名内部类打印的:" + msg);
            }
        };

        stringHandler.printMessage("小王");
     */
    public static void useStringHandler(StringHandler stringHandler) {
        stringHandler.printMessage("小王");
    }
}

@FunctionalInterface
interface StringHandler {
    void printMessage(String msg);
}
