package com.demo.generics;


import java.util.ArrayList;
import java.util.List;

public class GenericsDemo4 {
    /*
        泛型接口
                1. 实现类, 实现接口的时候确定到具体的类型
                2. 实现类实现接口, 没有指定具体类型, 就让接口的泛型, 跟着类的泛型去匹配
     */
    public static void main(String[] args) {
        InterCImpl<String> c1 = new InterCImpl<>();
        c1.show("abc");

        InterCImpl<Integer> c2 = new InterCImpl<>();
        c2.show(123);
    }
}

interface Inter<E> {
    void show(E e);
}

class InterAImpl implements Inter<String> {

    @Override
    public void show(String s) {

    }
}

class InterBImpl implements Inter<Integer> {

    @Override
    public void show(Integer integer) {

    }
}

class InterCImpl<E> implements Inter<E> {

    @Override
    public void show(E e) {

    }
}