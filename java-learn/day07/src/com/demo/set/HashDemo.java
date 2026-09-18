package com.demo.set;

public class HashDemo {
    public static void main(String[] args) {
        System.out.println("哈哈".hashCode());
        System.out.println("重地".hashCode() % 16);
        System.out.println("通话".hashCode() % 16);

        System.out.println("------------------------");

        for(int i = 1; i <= 100; i++){
            System.out.println(i % 16);
        }
    }
}
