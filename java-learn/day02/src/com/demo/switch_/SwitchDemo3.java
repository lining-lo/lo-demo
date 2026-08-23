package com.demo.switch_;

import java.util.Scanner;

public class SwitchDemo3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("---------- 欢迎使用商品管理系统 ---------");
        System.out.println("1、添加商品");
        System.out.println("2、删除商品");
        System.out.println("3、修改商品");
        System.out.println("4、查询全部商品");
        System.out.println("5、查询单个商品");
        System.out.println("6、退出");
        System.out.println("--------------------------------");
        System.out.println("请输入您的选择：");
        int command = sc.nextInt();
        switch (command) {
            case 1:
                System.out.println("添加商品功能！");
                break;
            case 2:
                System.out.println("删除商品功能！");
                break;
            case 3:
                System.out.println("修改商品功能！");
                break;
            case 4:
                System.out.println("查询全部商品！");
                break;
            case 5:
                System.out.println("查询单个商品！");
                break;
            case 6:
                //关闭虚拟机
                System.exit(0);
                break;
            default:
                System.out.println("请输入正确的命令~~~");
                break;

        }

    }
}
