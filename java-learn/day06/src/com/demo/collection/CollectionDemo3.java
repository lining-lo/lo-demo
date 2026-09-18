package com.demo.collection;

import java.util.ArrayList;
import java.util.Collection;

public class CollectionDemo3 {
    /*
        集合通用遍历方式 - 增强 for 循环
     */
    public static void main(String[] args) {
        Collection<String> c = new ArrayList<>();
        c.add("张三");
        c.add("李四");
        c.add("王五");

        for (String s : c) {
            System.out.println(s);
        }

        int[] arr = {11, 22, 33, 44, 55};

        for (int i : arr) {
            System.out.println(i);
        }
    }
}
