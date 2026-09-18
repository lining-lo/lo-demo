package com.demo.file;

import java.io.File;
import java.util.Date;

public class FileDemo4 {
    /*
        File类常用方法:

        public long length()                返回文件的大小（字节数量）
                                                    注意: 如果是文件夹对象, 调用该方法, 返回的结果是错误的.
        public String getAbsolutePath()     返回文件的绝对路径
        public String getPath()             返回定义文件时使用的路径
        public String getName()             返回文件的名称，带后缀
        public long lastModified()          返回文件的最后修改时间（时间毫秒值）
     */
    public static void main(String[] args) {
        File f1 = new File("E:\\A.txt");
        System.out.println(f1.length());

        File f2 = new File("E:\\Develop");
        System.out.println(f2.length());

        File f3 = new File("day03\\A.txt");
        System.out.println(f3.getAbsolutePath());

        System.out.println(f2.getPath());
        System.out.println(f3.getPath());

        System.out.println(f3.getName());

        long time = f1.lastModified();
        System.out.println(time);

        Date d = new Date(time);
        System.out.println(d);
    }
}
