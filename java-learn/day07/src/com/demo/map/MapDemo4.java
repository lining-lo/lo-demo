package com.demo.map;

import java.util.Map;
import java.util.TreeMap;
import java.util.function.BiConsumer;

public class MapDemo4 {
    /*
        Map集合的第三种遍历方式: foreach方法

        public default void forEach (BiConsumer<? super K,? super V> action)
                                                        遍历Map集合, 获取键和值
     */
    public static void main(String[] args) {
        Map<String, String> map = new TreeMap<>();
        map.put("张三", "北京");
        map.put("李四", "北京");
        map.put("王五", "北京");

        map.forEach((key, value) -> System.out.println(key + "---" + value));
        map.forEach((k, v) -> System.out.println(k + "---" + v));
    }
}
