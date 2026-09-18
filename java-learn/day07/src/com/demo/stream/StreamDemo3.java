package com.demo.stream;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Stream;

public class StreamDemo3 {
    /*
        Stream流的终结操作方法
            - 流水线中的最后一道工序

            public void forEach (Consumer action) 对此流的每个元素执行遍历操作
            public long count () 返回此流中的元素数
     */
    public static void main(String[] args) {
        System.out.println(Stream.of(1, 2, 3).count());

        // 细节: 流中的操作, 不会修改数据源
        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list, 1,2,3,4,5,6,7,8,9,10);

        list.stream().filter(s -> s % 2 == 0).forEach(System.out::println);

        System.out.println(list);
    }
}
