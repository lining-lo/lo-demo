package com.demo.switch_;

import java.util.Scanner;

public class SwitchDemo1 {
    public static void main(String[] args) {
        /*TODO
            switch (表达式) {
                case 值1:
                    // 表达式等于常量1时执行
                    break;  // 跳出switch（不写会"穿透"到下一个case）
                case 值2:
                    // 表达式等于常量2时执行
                    break;
                ...
                default:  // 所有case都不匹配时执行（可选）
                    // 执行语句
                    break;
            }
            执行流程： 表达式 的结果值，和case的值依次对比，
            如果一致就执行对应的代码，遇到break就结束当前分支执行
            如果多有的case和表达式的结果值不同就执行 default
         */
        //需求：用户输入 1-7 的整数，
        // 程序输出对应的星期几（1 = 周一，2 = 周二 .......7 = 周日），
        // 输入其他数字则提示错误。
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入数字1~7：");
        int command = sc.nextInt();
        switch (command) {
            case 1:
                System.out.println("星期一");
                //break;
            case 2:
                System.out.println("星期二");
                //break;
            case 3:
                System.out.println("星期三");
                //break;
            case 4:
                System.out.println("星期四");
                //break;
            case 5:
                System.out.println("星期五");
                break;
            case 6:
                System.out.println("星期六");
                break;
            case 7:
                System.out.println("星期天");
                break;
            default:
                System.out.println("命令输入错误~~~");
                break;
        }
    }
}
