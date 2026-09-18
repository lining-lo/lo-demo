package com.demo.stream;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;

public class FileInputStreamDemo {
    /*
        FileInputStream 字节输入流读取数据

        1. 构造方法:

            FileInputStream(String name)    输入流关联文件, 文件路径以字符串形式给出
            FileInputStream(File file)      输入流关联文件, 文件路径以File对象形式给出

        2. 成员方法:

            public int read()               读取单个字节
            public int read(byte[] bys)     读取一个字节数组
                                                - 将读取到的字节, 存入数组容器, 返回读取到的有效字节个数

     */
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("E:\\A.txt");

        byte[] bys = new byte[2];

        // 将读取到的字节, 存入数组容器, 返回读取到的有效字节个数
        int len;
        while( (len = fis.read(bys)) != -1) {
            String s = new String(bys, 0, len);
            System.out.print(s);
        }

        fis.close();

    }

    private static void method1() throws IOException {
        FileInputStream fis = new FileInputStream("E:\\A.txt");

        int i;
        while( (i = fis.read()) != -1 ){
            System.out.print((char)i);
        }

        fis.close();
    }
}
