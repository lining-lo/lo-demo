package com.demo.file;

import java.io.File;
import java.io.IOException;

public class FileDemo1 {
    /*
        File类的常用构造方法

            public File(String pathname)               根据文件路径创建文件对象
            public File(String parent, String child)   根据父路径名字符串和子路径名字符串创建文件对象
            public File(File  parent, String child)    根据父路径对应文件对象和子路径名字符串创建文件对象
     */
    public static void main(String[] args) throws IOException {
        File f1 = new File("D:\\A.txt");
        System.out.println(f1.exists());

        File f2 = new File("D:\\Develop");
        System.out.println(f2.exists());

        File f3 = new File("D:\\","workspace");
        System.out.println(f3.exists());

        File f4 = new File(new File("D:\\"),"Develop");
        System.out.println(f4.exists());

        File f5 = new File("D:\\B.txt");
        f5.createNewFile();
    }
}
