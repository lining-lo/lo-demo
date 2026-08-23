package com.demo.if_;

import java.util.Scanner;

public class IfDemo5 {
    public static void main(String[] args) {
        //需求：键盘录入考试成绩，根据成绩所在的区间，程序打印出不同的奖励机制
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你的成绩~~~");
        int score = sc.nextInt();

        // if多分支判断成绩的级别和奖励
        // 95~100
        if (score >= 95 && score <= 100) {
            System.out.println("你很优秀，奖励山地自行车一辆！");
        } else if(score >= 90 && score <= 94) {
            // 90 ~ 94
            System.out.println("你也太棒了，奖励周末去趟迪士尼乐园~~~");
        } else if(score >= 80 && score <= 89) {
            // 80~ 89
            System.out.println("成绩还可以，奖励变形金刚玩具一个~~~");
        } else if(score >= 0 && score <= 79) {
            // 0 ~ 79
            System.out.println("狗狗玩，你要不好好学习就等着挨揍吧~~~");
        } else {
            System.out.println("请输入合法的成绩！！！");
        }
    }
}
