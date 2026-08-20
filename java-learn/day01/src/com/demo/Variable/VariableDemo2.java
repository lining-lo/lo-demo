package com.demo.Variable;

public class VariableDemo2 {
    public static void main(String[] args) {
        // 目标：掌握变量的特点，搞清楚应用场景。
        // 特点：变量里装的数据是可以变化的。
        int age = 18; // 定义变量记住18岁（从右往左看）
        age = 19; // 从新给变量赋值新数据19（从右往左看）
        System.out.println(age);

        age = age + 1; //（从右往左看）
        System.out.println(age);

        System.out.println("----------------------------------------");
        // 需求：微信钱包现在有9.9，一个妹子让我给他发了5.2的红包，又有一个妹子给我发了3000元红包。随时可能看红包余额。
        double money = 9.9;
        System.out.println(money);

        // 发出红包 5.2
        money = money - 5.2;
        System.out.println(money);

        // 收红包 3000
        money = money + 3000;
        System.out.println(money);
    }
}

