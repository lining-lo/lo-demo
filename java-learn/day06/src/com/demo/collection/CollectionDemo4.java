package com.demo.collection;

import java.util.ArrayList;
import java.util.Collection;
import java.util.function.Consumer;

public class CollectionDemo4 {
    /*
        集合通用遍历方式 - foreach 方法
     */
    public static void main(String[] args) {
        Collection<String> c = new ArrayList<>();
        c.add("张三");
        c.add("李四");
        c.add("王五");
        c.forEach(s -> System.out.println(s));

        Collection<Integer> c2 = new ArrayList<>();
        c2.add(111);
        c2.add(222);
        c2.add(333);
        c2.forEach(num -> System.out.println(num));
    }
}
