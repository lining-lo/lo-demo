package com.demo.stream;

import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamDemo2 {
    /*
        流对象使用完毕后需要关闭
     */
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("E:\\A.txt");

        fos.write("abc".getBytes());

        fos.close();

        fos.write(97);

        while (true) {}
    }
}
