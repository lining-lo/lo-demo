package com.demo.list;

import com.demo.pojo6.Student;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class ListDemo1 {
    /*
        List接口特点: 存取有序, 有索引, 可以存储重复的

        遍历方式:
        1. 迭代器
        2. 增强for
        3. foreach方法
        4. 普通for循环
        5. 列表迭代器 (ListIterator)
     */
    public static void main(String[] args) {
        List<Student> list = new ArrayList<>();
        list.add(new Student("张三", 23));
        list.add(new Student("李四", 24));
        list.add(new Student("王五", 25));
        list.add(new Student("王五", 25));

        // 1. 迭代器
        Iterator<Student> it = list.iterator();
        while (it.hasNext()) {
            Student stu = it.next();
            System.out.println(stu);
        }

        System.out.println("------------------------------");

        // 2. 增强for
        for (Student stu : list) {
            System.out.println(stu);
        }

        System.out.println("------------------------------");

        // 3. foreach方法
        list.forEach(System.out::println);

        System.out.println("------------------------------");

        // 4. 普通for循环
        for (int i = 0; i < list.size(); i++) {
            Student stu = list.get(i);
            System.out.println(stu);
        }

        System.out.println("------------------------------");

        // 5. 列表迭代器 (ListIterator)
        ListIterator<Student> listIt = list.listIterator();
        System.out.println("列表迭代器正序遍历: ");
        while(listIt.hasNext()){
            Student stu = listIt.next();
            System.out.println(stu);
        }

        System.out.println("列表迭代器倒序遍历: ");
        while(listIt.hasPrevious()){
            Student stu = listIt.previous();
            System.out.println(stu);
        }
    }
}
