package com.demo.pojo10;

import com.demo.exception.StudentAgeException;

public class Student {
    private String name;
    private int age;

    public Student() {
    }

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }


    /*
        throw : 用在方法中, 后面跟的是异常对象, 用于真正的抛出异常.
        throws : 用在方法声明上, 后面跟的是异常类名, 作用是声明, 声明方法中的异常做抛出处理.

        细节: 如果抛出的异常对象, 是运行时异常, 就不需要编写throws, 反之必须写.
     */
    public void setAge(int age) {
        if (age >= 0 && age <= 100) {
            this.age = age;
        } else {
           throw new StudentAgeException("年龄有误, 请检查是否是0~100之间的!");
        }
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
