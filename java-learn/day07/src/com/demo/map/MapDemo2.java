package com.demo.map;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapDemo2 {
    /*
        Map集合的第一种遍历方式: 键找值

        public V get(Object key) : 根据键查找对应的值
        public Set<K> keySet() : 获取 Map 集合中所有的键
     */
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("张三", "北京");
        map.put("李四", "上海");
        map.put("王五", "成都");

        // 1. 获取Map集合中, 所有的键
        Set<String> keySet = map.keySet();
        // 2. 遍历set集合, 获取每一个键
        for (String key : keySet) {
            // 3. 通过map集合的get方法, 根据键查找对应的值
            String value = map.get(key);
            System.out.println(key + "---" + value);
        }
    }
}
