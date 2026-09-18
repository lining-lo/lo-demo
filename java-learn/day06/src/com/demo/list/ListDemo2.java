package com.demo.list;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class ListDemo2 {
    /*
        并发修改异常: ConcurrentModificationException

        使用迭代器遍历集合的过程中，调用了集合对象的添加，删除方法，就会出现此异常

        解决方案: 不允许使用集合的添加或删除方法, 就使用迭代器自身的添加或删除.
     */
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("张三");
        list.add("李四");
        list.add("王五");
        list.add("赵六");

        ListIterator<String> it = list.listIterator();
        while (it.hasNext()) {
            String name = it.next();
            if ("李四".equals(name)) {
                it.remove();
            }
        }

        System.out.println(list);
    }
}
