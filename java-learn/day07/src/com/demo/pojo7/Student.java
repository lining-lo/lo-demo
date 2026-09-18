package com.demo.pojo7;

import java.util.Objects;

public class Student implements Comparable<Student> {

    private String name;
    private int age;

    @Override
    public int compareTo(Student o) {
        // 排序要求: 倒序排序
        // 需求: 根据年龄作为主要排序条件, 根据姓名作为次要排序条件, 同姓名同年龄, 需要保留.
        int ageResult = o.age - this.age;
        int nameResult = ageResult == 0 ? o.name.compareTo(this.name) : ageResult;
        return nameResult == 0 ? -1 : nameResult;
    }


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

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student stu = (Student) o;
        return age == stu.age && Objects.equals(name, stu.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}
