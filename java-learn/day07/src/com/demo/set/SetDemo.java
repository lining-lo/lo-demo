package com.demo.set;

import java.util.*;

public class SetDemo {
    /*
        Set集合特点: 存取无序, 无索引, 不可以存储重复的.
            - 实现类:
                1. TreeSet : 排序
                2. HashSet : 保证元素唯一
                3. LinkedHashSet : 保证元素唯一, 保证存取顺序

            - 赠删改查方法: Collection接口中的方法

            - 遍历方式: 三种通用遍历方式
     */
    public static void main(String[] args) {
        Set<String> set1 = new TreeSet<>();
        set1.add("b");
        set1.add("a");
        set1.add("d");
        set1.add("c");
        set1.add("q");

        Iterator<String> it = set1.iterator();
        while (it.hasNext()) {
            String s = it.next();
            System.out.println(s);
        }

        System.out.println("-----------------------");


        Set<String> set2 = new HashSet<>();
        set2.add("b");
        set2.add("a");
        set2.add("d");
        set2.add("c");
        set2.add("q");

        for (String s : set2) {
            System.out.println(s);
        }

        System.out.println("-----------------------");


        Set<String> set3 = new LinkedHashSet<>();
        set3.add("b");
        set3.add("a");
        set3.add("d");
        set3.add("c");
        set3.add("q");
        set3.add("q");
        set3.add("q");

        set3.forEach(System.out::println);
    }
}
