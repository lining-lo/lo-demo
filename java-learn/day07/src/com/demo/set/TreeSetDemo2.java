package com.demo.set;

import java.util.TreeSet;

public class TreeSetDemo2 {
    public static void main(String[] args) {
        TreeSet<String> set = new TreeSet<>();

        set.add("aaa");
        set.add("a");
        set.add("dd");
        set.add("abc");

        System.out.println(set);

    }
}
