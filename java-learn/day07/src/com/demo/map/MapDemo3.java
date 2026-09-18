package com.demo.map;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

public class MapDemo3 {
    /*
        Map集合的第二种遍历方式: 键值对对象, 获取键和值.

        public Set<Map.Entry<K,V>> entrySet() : 获取集合中所有的键值对对象
     */
    public static void main(String[] args) {
        Map<String, String> map = new LinkedHashMap<>();
        map.put("张三", "北京");
        map.put("李四", "北京");
        map.put("王五", "北京");

        // 1. 调用entrySet方法, 获取所有的键值对对象.
        Set<Map.Entry<String, String>> entrySet = map.entrySet();
        // 2. 遍历Set集合, 获取每一个键值对对象
        for (Map.Entry<String, String> entry : entrySet) {
            // 3. 通过键值对对象, 获取键和值
            String key = entry.getKey();
            String value = entry.getValue();
            System.out.println(key + "---" + value);
        }
    }
}
