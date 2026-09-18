package com.demo.stream;

import java.util.ArrayList;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class StreamDemo5 {
    /*
        创建一个 ArrayList 集合，并添加以下字符串
        "张三,23"
        "李四,24"
        "王五,25"
        将数据收集到Map集合中，姓名为键，年龄为值
     */
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("张三,23");
        list.add("李四,24");
        list.add("王五,25");

        Map<String, String> map = list.stream().collect(Collectors.toMap(new Function<String, String>() {
            @Override
            public String apply(String s) {
                return s.split(",")[0];
            }
        }, new Function<String, String>() {
            @Override
            public String apply(String s) {
                return s.split(",")[1];
            }
        }));

        System.out.println(map);
    }
}
