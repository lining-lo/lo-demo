package com.demo.file;

import java.io.File;
import java.io.IOException;

public class FileDemo2 {
    /*
        绝对路径: 从盘符根目录开始，一直到某个具体的文件或文件夹
                        E:\\A.txt
                        E:\\Develop

        相对路径: 相对于当前项目
     */
    public static void main(String[] args) throws IOException {
        File f1 = new File("A.txt");
        f1.createNewFile();

        File f2 = new File("");
        System.out.println(f2.getAbsoluteFile());

        File f3 = new File("day03\\A.txt");
        f3.createNewFile();
    }
}
