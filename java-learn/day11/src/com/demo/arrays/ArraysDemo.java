package com.demo.arrays;

import java.util.Arrays;
import java.util.Comparator;

public class ArraysDemo {
    /*
        Arrays 数组操作工具类, 专门用于操作数组元素

        public static String toString(类型[] a)                将数组元素拼接为带有格式的字符串
        public static boolean equals(类型[] a, 类型[] b)        比较两个数组内容是否相同 (元素, 个数, 顺序)
        public static int binarySearch(int[] a, int key)       查找元素在数组中的索引 (二分查找法)
                                                                        - 注意: 操作的数组, 必须是排好顺序.
        public static void sort(类型[] a)                       对数组进行默认升序排序
     */
    public static void main(String[] args) {
        int[] arr1 = {11, 22, 33, 44, 55};
        int[] arr2 = {11, 22, 33, 44, 66};

        // 将数组元素拼接为带有格式的字符串
        System.out.println(Arrays.toString(arr1));

        // 比较两个数组内容是否相同
        System.out.println(Arrays.equals(arr1, arr2));

        // 查找元素在数组中的索引 (二分查找法)
        System.out.println(Arrays.binarySearch(arr1, 66));

        // 对数组进行默认升序排序
        Integer[] arr = {22, 11, 66, 77, 44, 55};
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));

        Arrays.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });

        System.out.println(Arrays.toString(arr));
    }
}
