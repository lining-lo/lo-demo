package com.demo.type;

public class TypeConversionDemo1 {
    public static void main(String[] args) {
        // 目标：记住八种基本数据类型。
        // 1、byte 字节整型
        byte age = 12;

        // 2、short 短整型
        short number = 32424;

        // 3、int 整型(默认)
        int number2 = 424244242;

        // 4、long 长整型
        // 注意：随便写的整数字面量默认是int类型的，32424242424424虽然没有超过long的范围
        // 32424242424424超了本身int的范围，所以报错！如果希望32424242424424是long类型的数据必须在后面加上L/l
        long lg = 32424242424424L;

        // 5、float 单精度浮点型
        // 注意：随便写小数默认是double，如果希望小数是float加上F/f
        float ft = 3.14F;

        // 6、double 双精度浮点型(默认)
        double ft2 = 3.15;

        // 7、char 字符型
        char c = 'a';
        char c2 = '中';

        // 8、boolean 布尔型
        boolean flag = false;
        boolean flag2 = true;

        // String 字符串类型（引用数据类型）
        // String的变量可以用于记住字符串数据
        String name = "组织部";
        System.out.println(name);
    }
}

