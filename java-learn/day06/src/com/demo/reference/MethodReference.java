package com.demo.reference;

import java.util.ArrayList;

public class MethodReference {
    /*
        方法引用是 JDK8 开始出现，主要的作用，是对 Lambda 表达式进行进一步的简化

        方法引用使用一对冒号 ::
        通过方法的名字来指向一个方法
        可以使语言的构造更紧凑简洁，减少冗余代码

        方法调用 -> MethodReference.change(s);
        方法引用 -> MethodReference::change
     */
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Hello");
        list.add("Hi");
        list.add("HEIma");

        MethodReference mr = new MethodReference();

        list.forEach(mr::change);
    }

    public void change(String s) {
        System.out.println(s.toLowerCase());
    }
}
