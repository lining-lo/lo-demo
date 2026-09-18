package com.demo.bigdecimal;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class BigDecimalDemo {
    /*
        BigDecimal类 : 用于解决小数运算中, 出现的不精确问题

        BigDecimal创建对象 :

                public BigDecimal(double val) : 不推荐, 无法保证小数运算的精确
                ---------------------------------------------------------------
                public BigDecimal(String val)
                public static BigDecimal valueOf(double val)

        BigDecimal常用成员方法 :

                public BigDecimal add(BigDecimal b) : 加法
                public BigDecimal subtract(BigDecimal b) : 减法
                public BigDecimal multiply(BigDecimal b) : 乘法
                public BigDecimal divide(BigDecimal b) : 除法
                public BigDecimal divide (另一个BigDecimal对象，精确几位，舍入模式) : 除法

                                RoundingMode.HALF_UP : 四舍五入
                                RoundingMode.UP : 进一法
                                RoundingMode.DOWN : 去尾法

        注意: 如果使用BigDecimal运算, 出现了除不尽的情况, 就会出现异常
     */
    public static void main(String[] args) {
        BigDecimal bd1 = BigDecimal.valueOf(10.0);
        BigDecimal bd2 = BigDecimal.valueOf(3.0);

        double result1 = bd1.add(bd2).doubleValue();
        double result2 = bd1.subtract(bd2).doubleValue();
        double result3 = bd1.multiply(bd2).doubleValue();

        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);


        double result4 = bd1.divide(bd2, 2, RoundingMode.HALF_UP).doubleValue();
        System.out.println(result4);

    }

    private static void method() {
        BigDecimal bd1 = new BigDecimal("0.1");
        BigDecimal bd2 = new BigDecimal("0.2");

        System.out.println(bd1.add(bd2));

        BigDecimal bd3 = BigDecimal.valueOf(0.1);
        BigDecimal bd4 = BigDecimal.valueOf(0.2);
        System.out.println(bd3.add(bd4));
    }
}
