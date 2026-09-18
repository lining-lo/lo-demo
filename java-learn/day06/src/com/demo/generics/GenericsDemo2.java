package com.demo.generics;

public class GenericsDemo2 {
    /*
        泛型常见的标识符:

            E : Element 元素
            T : Type 类型
            K : Key 键
            V : Value 值
     */
    public static void main(String[] args) {
        Student<Integer> stu1 = new Student<>();
        stu1.setE(10);
        stu1.getE();
    }
}

class Student<E> {
    private E e;

    public E getE() {
        return e;
    }

    public void setE(E e) {
        this.e = e;
    }
}