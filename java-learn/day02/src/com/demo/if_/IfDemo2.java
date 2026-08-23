package com.demo.if_;

import java.util.Scanner;

public class IfDemo2 {
    public static void main(String[] args) {
        //if-esle 双分支
        /*
           todo 语法
                 if(条件) {
                     代码块1
                 } else {
                    代码块2
                 }
            执行流程：如果条件成立为true就执行 代码块1，否则就实行代码块2
         */
        //需求： 用户输入自己的科目一成绩 score，判断是否通过考试，如果没通过提醒用户
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你的科目一成绩：");
        int score= sc.nextInt();
        //if 双分支语句进行判断
        if(score >= 90){
            System.out.println("恭喜你，狗狗娃，考试通过~~");
        } else {
            System.out.println("冷胖，你么通过~~~");
        }
    }
}
