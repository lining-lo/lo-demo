package com.demo.stream;

import java.util.*;
import java.util.function.Consumer;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class StreamDemo1 {
    /*
        获取Stream流对象演示
            - 将数据放在流水线的传送带上

            1. 集合获取 Stream 流对象 (使用Collection接口中的默认方法)
                    default Stream<E> stream()

                    * Map集合获取Stream流对象, 需要间接获取
                            - map.entrySet().stream()

            2. 数组获取 Stream 流对象 (使用Arrays数组工具类中的静态方法)
                    static <T> Stream<T> stream (T[] array)

            3. 零散的数据获取 Stream 流对象 (使用 Stream 类中的静态方法)
                    static <T> Stream<T> of(T... values)
     */
    public static void main(String[] args) {

        int[] arr = {11, 22, 33};
        String[] names = {"张三", "李四", "王五"};

        Arrays.stream(arr).forEach(System.out::println);
        Arrays.stream(names).forEach(System.out::println);

        Stream<Integer> s1 = Stream.of(1, 2, 3, 4, 5);
        Stream<String> s2 = Stream.of("张三", "李四", "王五");

    }

    private static void method() {
        List<String> list = new ArrayList<>();
        list.add("张三丰");
        list.add("张无忌");
        list.add("张翠山");
        list.add("王二麻子");
        list.add("张良");
        list.add("谢广坤");

        list.stream().forEach(System.out::println);
        System.out.println("---------------------------");

        Set<String> set = new HashSet<>();
        set.add("张三丰");
        set.add("张无忌");
        set.add("张翠山");
        set.add("王二麻子");
        set.add("张良");
        set.add("谢广坤");

        set.stream().forEach(System.out::println);
        System.out.println("---------------------------");

        Map<String, Integer> map = new HashMap<>();
        map.put("张三丰", 100);
        map.put("张无忌", 35);
        map.put("张翠山", 55);
        map.put("王二麻子", 22);
        map.put("张良", 30);
        map.put("谢广坤", 55);

        Stream<String> s1 = map.keySet().stream();
        s1.forEach(System.out::println);

        Stream<Integer> s2 = map.values().stream();
        s2.forEach(System.out::println);

        System.out.println("---------------------------");

        // 获取map集合中, 所有键值对的对象
        // Set<Map.Entry<String, Integer>> entrySet = map.entrySet();
        // Stream<Map.Entry<String, Integer>> s3 = entrySet.stream();
        // s3.forEach(System.out::println);
        map.entrySet().stream().forEach(System.out::println);
    }
}
