package com.demo.time;


import java.time.*;

public class LocalDateTimeDemo {
     /*
        ------------------------------------------
        LocalDate、LocalTime、LocalDateTime

        对象的创建方式:

        1. now() : 当前时间

        2. of(...) : 设置时间

        ------------------------------------------
        LocalDateTime 转换LocalDate, LocalTime

        1. toLocalDate()
        2. toLocalTime()
     */
    public static void main(String[] args) {
        show();
    }

    private static void method() {
        LocalDateTime now = LocalDateTime.now();
        System.out.println(now);

        LocalDate localDate = now.toLocalDate();
        LocalTime localTime = now.toLocalTime();
        System.out.println(localDate);
        System.out.println(localTime);

        LocalDateTime localDateTime = LocalDateTime.of(2008, 8, 8, 8, 8, 8, 8);
        System.out.println(localDateTime);

        LocalDate now1 = LocalDate.now();
        LocalTime now2 = LocalTime.now();

        System.out.println(now1);
        System.out.println(now2);
    }

    public static void show() {
        // 日期 时间
        LocalDateTime now = LocalDateTime.now();
        // 年
        int year = now.getYear();
        // 月
        Month month = now.getMonth();
        int monthValue = now.getMonthValue();
        // 日
        int dayOfMonth = now.getDayOfMonth();
        // 星期
        DayOfWeek dayOfWeek = now.getDayOfWeek();
        int week = dayOfWeek.getValue();
        // 时
        int hour = now.getHour();
        // 分
        int minute = now.getMinute();
        // 秒
        int second = now.getSecond();
        // 纳秒
        int nano = now.getNano();
    }
}
