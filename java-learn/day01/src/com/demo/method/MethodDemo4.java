package com.demo.method;

import java.util.Random;

public class MethodDemo4 {
    public static void main(String[] args) {
        String res = getVcode();
        System.out.println(res);
    }

    // 定义一个方法 getVcode，此处需要使用for循环，随机生成4位验证码
    // 并且返回验证码
    public static String getVcode() {
        Random r = new Random();
        // 定义一个空字符串 用来存储验证码
        String vcode = "";
        // 此处需要石红for循环，循环4次，每一次需要生成一个随机0~9的数
        // 从0到3 开始循环4次
        for (int i = 0; i < 4; i++) {
            //顶一个随机数变量接收生成随机数
            // 以下代码没循环一次就给vcode字符串拼接一个 数
            vcode += r.nextInt(10);
            //vcode = vcode + r.nextInt(10);
        }
        // i = 0, 0<4 满足循环条件,循环第1次，生成一个随机数，然后拼接给vcode，然后 i++
        // i = 1, 1<4 满足循环条件,循环第2次，生成一个随机数，然后拼接给vcode，然后 i++
        // i = 2, 2<4 满足循环条件,循环第3次，生成一个随机数，然后拼接给vcode，然后 i++
        // i = 3, 3<4 满足循环条件,循环第4次，生成一个随机数，然后拼接给vcode，然后 i++
        // i = 4，  此时4 < 4，不满足循环条件，结束循环
        return vcode;
    }
}
