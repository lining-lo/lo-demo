package com.demo.test;

import com.demo.exception.StudentAgeException;
import com.demo.pojo8.Student;

import java.util.Scanner;

public class ExceptionTest {
    /*
        键盘录入学生的姓名和年龄, 封装为学生对象并打印.

        异常的两种处理方式:
        1. try...catch捕获异常
        2. 抛出异常

        使用思路: 看问题是否需要暴露
                    要: 抛出异常
                    不要: try...catch捕获.
     */
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Student stu = new Student();

        System.out.println("请输入学生姓名: ");
        String name = sc.next();
        stu.setName(name);

        while (true) {
            try {
                System.out.println("请输入学生年龄: ");
                int age = Integer.parseInt(sc.next());
                stu.setAge(age);
                break;
            } catch (NumberFormatException e) {
                System.out.println("您输入的年龄有误, 请检查!");
            } catch (StudentAgeException e) {
                System.out.println(e.getMessage());
            }
        }

        System.out.println(stu);
    }
}
