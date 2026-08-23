package com.demo.if_;

import java.util.Scanner;

public class IfDemo4 {
    public static void main(String[] args) {
        /*
            TODO 语法
                if (条件1) {
                    // 条件1为true时执行
                } else if (条件2) {
                    // 条件1为false，条件2为true时执行
                } else if (条件3) {
                    // 条件2为false，条件3为true时执行
                }
                ...
                else {
                    // 所有条件都为false时执行（可选）
                }
               执行流程：会依次执行判断条件没如果遇到了成立的条件，就执行对应的代码，要是所有的条件都不成立就执行 else
         */
        //需求：用户键盘输入数字，如果是1就是VIP会员，是0就是非VIP会员，其他数字则提醒用户输入错误
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入命令1或者0：");
        int command = sc.nextInt();
        if (command == 1){
            System.out.println("尊敬的VIP会员，欢迎光临！");
        } else if (command == 0){
            System.out.println("顾客你好，欢迎光临！");
        } else {
            System.out.println("你输入的命令错误~~~");
        }
    }
}
