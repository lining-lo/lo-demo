package com.demo.set;

import com.demo.pojo7.Person;

import java.util.HashSet;

public class HashSetDemo1 {
    /*
        HashSet集合保证元素唯一, 需要同时重写hashCode和equals方法
     */
    public static void main(String[] args) {
        HashSet<Person> set = new HashSet<>();

        set.add(new Person("张三", 23));
        set.add(new Person("李四", 24));
        set.add(new Person("王五", 25));
        set.add(new Person("王五", 25));

        System.out.println(set);
    }
}
