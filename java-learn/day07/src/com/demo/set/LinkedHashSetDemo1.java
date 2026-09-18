package com.demo.set;

import com.demo.pojo7.Student;

import java.util.LinkedHashSet;

public class LinkedHashSetDemo1 {
    public static void main(String[] args) {
        LinkedHashSet<Student> lhs = new LinkedHashSet<>();

        lhs.add(new Student("王五", 25));
        lhs.add(new Student("张三", 23));
        lhs.add(new Student("李四", 24));
        lhs.add(new Student("张三", 23));

        for (Student stu : lhs) {
            System.out.println(stu);
        }
    }
}
