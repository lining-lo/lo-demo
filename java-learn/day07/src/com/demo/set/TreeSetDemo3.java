package com.demo.set;

import java.util.Comparator;
import java.util.TreeSet;

public class TreeSetDemo3 {
    /*
        TreeSet集合排序方式 - 比较器排序

            特点: 如果同时具备自然排序和比较器排序, 优先按照比较器排序的规则进行操作.
     */
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>((o1, o2) -> o2 - o1);
        set.add(222);
        set.add(111);
        set.add(555);
        set.add(333);
        set.add(444);

        System.out.println(set);

        TreeSet<String> set2 = new TreeSet<>((o1, o2) -> o2.length() - o1.length());
        set2.add("a");
        set2.add("bb");
        set2.add("ddd");
        set2.add("c");
        set2.add("qqqqq");

        System.out.println(set2);
    }
}
