package com.demo.map;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.TreeSet;

public class MapDemo5 {
    public static void main(String[] args) {
        HashSet<String> set1 = new HashSet<>();
        set1.add("A");

        TreeSet<String> set2 = new TreeSet<>();
        set2.add("B");

        LinkedHashSet<String> set3 = new LinkedHashSet<>();
        set3.add("C");
    }
}
