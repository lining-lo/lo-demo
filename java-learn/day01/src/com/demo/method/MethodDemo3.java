package com.demo.method;

public class MethodDemo3 {
    public static void main(String[] args) {
        //调用有返回值的方法，需要使用和返回值类型一致的 变量接收返回结果
        int he = getSum(4, 8, 7);
        //平均值 = 和 / 3
        //double avg = he / 3; //整数
        double avg = he * 1.0 / 3; //浮点数
        System.out.println("三个数的平均值：" + avg);
    }

    //求3个整数的 和，并且返回和这个和的结果，用结果求出平均值
    //求和方法
    // 返回值类型是int，说明需要return一个 int类型数据作为结果
    public static int getSum(int a, int b, int c) {
        int sum = a + b + c;
        // 将结果返回 是 int类型
        return sum;
    }
}
