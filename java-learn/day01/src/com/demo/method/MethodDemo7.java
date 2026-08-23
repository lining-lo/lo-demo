package com.demo.method;

public class MethodDemo7 {
    public static void main(String[] args) {
        fire();
        fire("小小日子");
        fire("小小日子", 1000000000);
    }

    //TODO 方法重载的使用场景：开发中处理一类业务，提供多种的解决方案，使用方法重载实现
    //默认可以给你某一个地方发射一枚导弹
    public static void fire() {
        System.out.println("默认给小日子发射1枚氢弹~~~");
    }

    // 给指定的国家发射
    public static void fire(String country) {
        System.out.println("默认给" + country + "发射1枚氢弹~~~");
    }

    // 给指定的国家发射 指定的 数量 导单
    public static void fire(String country, int num) {
        System.out.println("默认给" + country + "发射" + num + "枚氢弹~~~");
    }
}