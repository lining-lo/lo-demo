package com.demo.stream;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Set;
import java.util.function.BiConsumer;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamDemo4 {
    /*
        Stream流的收集操作

            public R collect (Collector c) : 将流中的数据收集到集合

                Collectors
                    public static <T> Collector toList()
                    public static <T> Collector toSet()
                    public static  Collector toMap(Function keyMapper , Function valueMapper)
     */
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10);

        List<Integer> result1 = list.stream().filter(s -> s % 2 == 0).collect(Collectors.toList());
        System.out.println(result1);

        Set<Integer> result2 = list.stream().filter(s -> s % 2 == 0).collect(Collectors.toSet());
        System.out.println(result2);

        List<Integer> result3 = list.stream().filter(s -> s % 2 == 0).toList();
    }
}
