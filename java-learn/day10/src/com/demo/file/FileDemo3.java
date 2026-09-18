package com.demo.file;

import java.io.File;

public class FileDemo3 {
    /*
        File类的判断相关方法

            public boolean isDirectory()    判断此路径名表示的File是否为文件夹
            public boolean isFile()         判断此路径名表示的File是否为文件
            public boolean exists()         判断此路径名表示的File是否存在
     */
    public static void main(String[] args) {

        File f = new File("day03\\A.txt");

        System.out.println(f.isDirectory());
        System.out.println(f.isFile());
        System.out.println(f.exists());

    }
}
