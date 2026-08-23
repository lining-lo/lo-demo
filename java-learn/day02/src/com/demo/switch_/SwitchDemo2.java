package com.demo.switch_;

import java.util.Scanner;

public class SwitchDemo2 {
    public static void main(String[] args) {
        //3 月～5 月为春季‌，‌6 月～8 月为夏季‌，‌9 月～11 月为秋季‌，‌12 月～次年 2 月为冬季‌。
        //用户输入对应的月份，打印 对应  季节
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入月份1~12");
        int command = sc.nextInt();
        //根据用户输入的月份判断季节 switch的穿透性，不写break
        switch (command) {
            case 3:
            case 4:
            case 5:
                System.out.println("春季~~");
                break;
            case 6:
            case 7:
            case 8:
                System.out.println("夏季~~");
                break;
            case 9:
            case 10:
            case 11:
                System.out.println("秋季~~");
                break;
            case 12:
            case 1:
            case 2:
                System.out.println("冬季~~");
                break;
            default:
                System.out.println("请输入合法月份");
                break;
        }
    }
}
