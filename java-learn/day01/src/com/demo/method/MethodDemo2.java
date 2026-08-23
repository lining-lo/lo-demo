package com.demo.method;

public class MethodDemo2 {
    //main 是一个Java的方法，是整个程序的入口
    public static void main(String[] args) {
        //求任意两个整数的和
        /*
        int num1 = 10;
        int num2 = 20;
        System.out.println(num1 + num2);

        int num3 = 4;
        int num4 = 5;
        System.out.println(num3 + num4);

        int num5 = 100;
        int num6 = 200;
        System.out.println(num5 + num6);

        int num7 = 400;
        int num8 = 600;
        System.out.println(num7 + num8);
        */
        // 调用方法 void方法直接使用   方法名(实参)
        // 调用方法的时候，传入的实参必须和形参的数量一致，并且数据类型也要一直
        getSum(2,3);
        getSum(8,5);
        getSum(80,60);
        //getSum("徐璈",8);  报错 实参和形参的类型不匹配
        //getSum(3);  报错，实参的数量和形参匹配
    }

    // 方法不能直接定义在另一个方法里面,方法只有被调用了才能执行
    // 求任意两个整数的和，打印在控制体
    public static void getSum(int num1, int num2) {
        int sum = num1 + num2;
        System.out.println(sum);
    }
    /*TODO 定义方法的通用语法
         修饰符 返回值类型 方法名(形参列表) {
             // 方法体（需要执行的功能代码）
             return 返回值; // 若返回值类型不是void，必须有return
         }
         修饰符：暂时都使用 public static
         返回值类型：如果有返回值此处设置具体返回数据的类型，如果没有返回值直接用void代替
         方法名：就是给方法起的名字，命名规范遵守 小驼峰命名（首字母小写，如果是多个单词，从第二个单词开始首字母大写）
         形参列表：根据需求设置如果需求有参数就设置对应类型的，没有就不设置，是用来占位的，方法被调用时需要传入实际参数
         方法体：就是具体要实现的功能代码
         return：也是根据需求设置的，如果功能需要返回一个结果去其他地方使用，就设置return，此时返回值类型需要设置对应类型
    */
}
