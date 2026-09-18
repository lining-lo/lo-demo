package com.demo.args;

public class ArgsDemo {
    /*
        可变参数用在形参中可以接收多个数据
        可变参数的格式: 数据类型...参数名称

        传输参数非常灵活, 方便, 可以不传输参数, 可以传输一个或者多个, 也可以传输一个数组

        ---------------------------------------------------------------------------------------

        注意事项
        1. 可变参数, 在方法中只能有一个
        2. 如果方法中除了可变参数, 还有其它的参数, 需要将可变参数放在最后
     */
    public static void main(String[] args) {

        System.out.println(getSum());
        System.out.println(getSum(1));
        System.out.println(getSum(1, 2));
        System.out.println(getSum(1, 2, 3));

        int[] arr = {1,2,3,4,5};

        System.out.println(getSum(arr));

    }

    public static int getSum(int... nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;
    }
}
