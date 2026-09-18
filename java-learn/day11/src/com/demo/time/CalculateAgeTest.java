package com.demo.time;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Date;
import java.util.Scanner;

public class CalculateAgeTest {
    /*
        需求: 键盘录入用户的生日, 计算出用户的年龄.
     */
    public static void main(String[] args) throws ParseException {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入您的生日: ");
        String birthday = sc.next();

        // 创建时间格式化对象
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy年M月d日");
        LocalDate birthdayDate = LocalDate.parse(birthday, formatter);

        // 计算时间间隔
        long age = ChronoUnit.YEARS.between(birthdayDate, LocalDate.now());

        System.out.println(age);

    }

    private static void method() throws ParseException {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入您的生日: ");
        String birthday = sc.next();

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日");

        // 1. 将用户的生日, 解析为时间对象
        Date birthdayDate = sdf.parse(birthday);
        // 2. 获取此刻的时间
        Date now = new Date();
        // 3. 计算时间差
        long time = now.getTime() - birthdayDate.getTime();
        // 4. 转换单位
        System.out.println(time / 1000 / 60 / 60 / 24 / 365);
    }
}
