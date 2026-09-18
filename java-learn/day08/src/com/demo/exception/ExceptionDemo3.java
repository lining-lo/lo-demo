package com.demo.exception;

import java.io.FileNotFoundException;
import java.io.FileReader;

public class ExceptionDemo3 {
    /*
        异常处理方式2: 抛出异常

        throws: 用在方法上, 作用是声明, 声明这个方法中的异常是抛出处理.

        在继承关系中, 子类重写父类方法, 不能抛出父类中不存在的, 或者比父类更大的异常.
     */
    public static void main(String[] args) throws Exception {
        method();
    }

    public static void method() throws FileNotFoundException, ClassNotFoundException {
        System.out.println("开始");
        FileReader fr = new FileReader("D:\\abc.txt");
        System.out.println("结束");

        Class.forName("com.demo.pojo8.Student");

    }
}

class Fu {
    public void show() throws Exception {
        System.out.println("Fu...show...");
    }
}

class Zi extends Fu {
    @Override
    public void show() throws Exception {
        FileReader fr = new FileReader("D:\\abc.txt");
        Class.forName("com.demo.pojo8.Student");
    }
}