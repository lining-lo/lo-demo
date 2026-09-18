package com.demo.map;

import java.util.HashMap;
import java.util.Map;
import java.util.function.BiConsumer;

public class MapTest1 {
    /*
        需求: 字符串 aababcabcdabcde
                    请统计字符串中每一个字符出现的次数，并按照以下格式输出

	    输出结果
                    a(5)b(4)c(3)d(2)e(1)
     */
    public static void main(String[] args) {
        String s = "aababcabcdabcde";
        // 创建Map集合, 键的位置存储字符, 值的位置存储次数
        Map<Character, Integer> map = new HashMap<>();

        // 遍历字符串, 获取每一个字符
        char[] charArray = s.toCharArray();
        for (char c : charArray) {
            // 判断当前字符在Map集合中是否存在
            if (!map.containsKey(c)) {
                // 不存在: 直接存入, 值的位置写1
                map.put(c, 1);
            } else {
                // 存在: 取出旧值, +1存回去
                map.put(c, map.get(c) + 1);
            }
        }


        // a(5)b(4)c(3)d(2)e(1)
        StringBuilder sb = new StringBuilder();
        map.forEach((key, value) -> sb.append(key).append("(").append(value).append(")"));
        System.out.println(sb);

    }
}
