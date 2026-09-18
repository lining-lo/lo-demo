package com.demo.collection;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class CollectionDemo2 {
    /*
        集合通用遍历方式 - 迭代器
     */
    public static void main(String[] args) {
        Collection<String> c = new ArrayList<>();
        c.add("张三");
        c.add("李四");
        c.add("王五");

        // 1. 通过集合对象, 获取迭代器
        Iterator<String> it = c.iterator();     // new Itr();
        // 2. 循环判断是否还有元素可以迭代
        while (it.hasNext()) {
            // 3. 循环内部获取元素
            String s = it.next();
            System.out.println(s);
        }
    }
}
