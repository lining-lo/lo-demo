package com.demo.time;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class SimpleDateFormatDemo {
    /*
        SimpleDateFormat类 : 用于日期格式化

        1. 构造方法 :

                public SimpleDateFormat() : 创建一个日期格式化对象, 使用 [默认模式]
                public SimpleDateFormat(String pattern) : 创建一个日期格式化对象, [手动指定模式]

        2. 常用方法 :

                public final String format(Date date) : 将日期对象, 转换为字符串
                public final Date parse(String source) : 将日期字符串, 解析为日期对象

     */
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日");

        Date now = new Date();

        // 将日期对象, 转换为指定格式的字符串.
        String result = sdf.format(now);

        System.out.println(result);

        String birthday = "2008年08月08日";
        Date parse = sdf.parse(birthday);
        System.out.println(parse);
    }
}

