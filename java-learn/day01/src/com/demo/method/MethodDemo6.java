package com.demo.method;

public class MethodDemo6 {
    public static void main(String[] args) {
        getSum(3,6);
        getSum(2.6,6.8);
        getSum(3,6,8);
        getSum(2.8,9);
    }
    //方法重载：一个类中，出现多个方法，方法的名是相同的，但是参数不同
    //理解为： 同一个方法名，传入不同的参数，实现不同的功能
    // 定义一个加法运算的方法 getSum
    //求两个整数的和
    public static void getSum(int a, int b){
        System.out.println(a + b);
    }
    // 参数的类型相同，顺序不同不算方法重载
//    public static void getSum(int b, int a){
//        System.out.println(a + b);
//    }
    //求两个浮点数的和
    // TODO 参数的类型不同算方法重载
    public static void getSum(double a, double b){
        System.out.println(a + b);
    }
    //求3个整数的和
    // TODO 参数的数量不同算方法重载
    public static void getSum(int a, int b, int c){
        System.out.println(a + b + c);
    }
    //求 一个整数和一个浮点数的和
    // TODO 参数的类型不同，但是数量一致，也算方法重载
    public static void getSum(int a, double b){
        System.out.println(a + b);
    }
    // TODO 如果参数的类型不一致，顺序不同也算方法重载
    public static void getSum(double a,  int b){
        System.out.println(a + b);
    }
}
