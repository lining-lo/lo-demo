package com.demo.if_;

import java.util.Scanner;

public class IfDemo1 {
    public static void main(String[] args) {
        //if单分支
        /*TODO 语法
                   if(条件){
                       条件成立为true时执行的代码
                   }
            执行流程： 如果 条件成立为true就执行对应的代码，为false不成立就啥也不干
         */
        //需求： 用户输入自己的科目一成绩 score，判断是否通过考试
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你的科目一成绩：");
        int score = sc.nextInt();
        // if单分支
        if (score >= 90) {
            System.out.println("恭喜你，考试通过！");
        }
    }
}
