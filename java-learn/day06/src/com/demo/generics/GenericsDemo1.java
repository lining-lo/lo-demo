package com.demo.generics;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Random;

public class GenericsDemo1 {
    /*
        泛型介绍 : JDK5引入的, 可以在编译阶段约束操作的数据类型, 并进行检查

        泛型如果没有指定具体的类型, 默认为Object

        泛型的好处 :
                    1. 统一数据类型
                    2. 将运行期的错误提升到了编译期
     */
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("abc");
        list.add("abc");
        list.add("abc");

        Iterator<String> it = list.iterator();
        while (it.hasNext()) {
            String s = it.next();
            System.out.println(s.length());
        }
    }
}
