package com.demo.collections;

import com.demo.pojo7.Person;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class CollectionsDemo {
    /*
        Collections并不属于集合，是用来操作集合的工具类。

        public static <T> boolean addAll(Collection<? super T> c, T... elements)        给集合对象批量添加元素
        public static void shuffle(List<?> list)                                        打乱List集合元素的顺序
        public static <T> void max/min(Collection<T> coll)                              根据默认的自然排序获取最大/小值
        public static <T> void sort(List<T> list)                                       将集合中元素按照默认规则排序
        public static <T> void sort(List<T> list，Comparator<? super T> c)               将集合中元素按照指定规则排序
     */
    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list, 1, 2, 3, 4, 5, 6, 7);

        Collections.sort(list, new Comparator<Integer>() {

            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });

        System.out.println(list);

        // 洗牌
        Collections.shuffle(list);

        System.out.println(list);

        // 求最值
        System.out.println(Collections.max(list));
        System.out.println(Collections.min(list));

        ArrayList<Person> persons = new ArrayList<>();
        Collections.addAll(persons, new Person("张三", 28), new Person("李四", 24), new Person("王五", 25));

        System.out.println(Collections.max(persons));
        System.out.println(Collections.min(persons));

        Collections.sort(persons);
        System.out.println(persons);
    }
}
