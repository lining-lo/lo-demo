package com.demo.method;

public class MethodDemo5 {
    //设计一个方法, 能够计算出3个整数的最小值
    public static int getMin(int a, int b, int c){
        int tempMin = a < b ? a : b;
        int min = tempMin < c ? tempMin : c;
        return min;  // 方法中 执行到return会就结束整个方法的执行，后面的代码都无法运行
        //System.out.println("哈哈哈");
    }

    public static void main(String[] args) {
        int res = getMin(2,6,8);
        System.out.println(res);
        // 调用用户信息打印
        printUserInfo("小哈",18,1.89,'男');
        System.out.println("--------------");
        printUserInfo("苗强",38,1.59,'男');
    }

    //设计一个方法printUserInfo, 方法能够打印出用户的个人信息 (姓名, 年龄, 身高, 性别)
    public static void printUserInfo(String name, int age,double height,char gender){
        System.out.println("姓名：" + name);
        System.out.println("年龄：" + age);
        System.out.println("身高：" + height);
        System.out.println("性别：" + gender);
    }
}
