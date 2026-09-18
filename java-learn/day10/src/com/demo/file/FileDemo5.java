package com.demo.file;

import java.io.File;
import java.io.IOException;

public class FileDemo5 {
    /*
        File类常用方法: 创建和删除

            public boolean createNewFile()      创建一个新的空的文件
            public boolean mkdir()              只能创建一级文件夹
            public boolean mkdirs()             可以创建多级文件夹
            public boolean delete()             删除由此抽象路径名表示的文件或空文件夹
     */
    public static void main(String[] args) throws IOException {
        File f1 = new File("day03\\B.txt");
        System.out.println(f1.createNewFile());

        File f2 = new File("day03\\aaa");
        System.out.println(f2.mkdirs());

        System.out.println(f1.delete());
        System.out.println(f2.delete());
    }
}
