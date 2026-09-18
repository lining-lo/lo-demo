package com.demo.set;

import com.demo.pojo7.Student;

import java.util.TreeSet;

public class TreeSetDemo1 {
    /*
        TreeSet两种排序方式 - 自然排序

        1. 让类实现Comparable接口
        2. 重写compareTo方法
        3. 根据方法的返回值来指定排序规则
     */
    public static void main(String[] args) {
        TreeSet<Student> set = new TreeSet<>();

        set.add(new Student("李四", 24));
        set.add(new Student("张三", 23));
        set.add(new Student("王五", 25));
        set.add(new Student("李四", 24));

        System.out.println(set);
    }
}
