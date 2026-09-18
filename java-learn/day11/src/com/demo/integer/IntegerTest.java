package com.demo.integer;

public class IntegerTest {
    /*
        已知字符串
        String s = "10,50,30,20,40";

        请将该字符串转换为整数并存入数组
        随后求出最大值打印在控制台
     */
    public static void main(String[] args) {
        String content = "10,50,30,20,40";

        String[] arr = content.split(",");

        int[] nums = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            nums[i] = Integer.parseInt(arr[i]);
        }

        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }

        System.out.println("最大值为:" + max);
    }
}
