package com.demo.stream;

import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamDemo4 {
    /*
        IO流的异常处理方式: jdk7版本开始

        try
            (需要调用close方法的流对象)
            {
                IO流逻辑代码
            }
        catch (异常类名 对象名) {
            异常处理方案
        }

        ()中的流对象, 会自动调用close方法, 就算有异常, 也会调用close.
     */
    public static void main(String[] args) {

        try (FileOutputStream fos = new FileOutputStream("E:\\A.txt");) {
            fos.write("abc".getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (Demo d = new Demo();) {

            System.out.println(10 / 0);

        } catch (NullPointerException e) {

        }

    }
}

class Demo implements AutoCloseable {

    @Override
    public void close() throws NullPointerException {
        System.out.println("我关了.");
    }
}