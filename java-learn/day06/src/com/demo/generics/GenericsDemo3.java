package com.demo.generics;

public class GenericsDemo3 {
    /*
        泛型方法

              非静态方法: 跟着类的泛型去匹配的
                            类的泛型, 是在创建对象的时候确定到具体数据类型.

              静态方法: 调用方法的时候, 传入实际参数, 在这时候确定到具体的数据类型
                            注意: 静态方法如果声明了泛型, 必须声明出自己独立的泛型.
     */
    public static void main(String[] args) {

        String[] arr1 = {"张三", "李四", "王五"};
        Integer[] arr2 = {11, 22, 33};
        Double[] arr3 = {11.1, 22.2, 33.3};

        printArray(arr1);
        printArray(arr2);
        printArray(arr3);

    }

    public static <T> void printArray(T[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length - 1; i++) {
            System.out.print(arr[i] + ", ");
        }
        System.out.println(arr[arr.length - 1] + "]");
    }
}
