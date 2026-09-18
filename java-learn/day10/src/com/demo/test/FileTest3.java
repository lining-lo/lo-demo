package com.demo.test;

import java.io.File;

public class FileTest3 {
    /*
        需求：键盘录入一个文件夹路径，找出这个文件夹下所有的 .java 文件 (考虑子文件夹)

     */
    public static void main(String[] args) {
        File dir = FileTest1.getDir();
        printJavaFile(dir);
    }

    private static void printJavaFile(File dir) {
        // 获取当前目录下, 所有文件和文件夹对象
        File[] files = dir.listFiles();
        // 遍历数组, 获取每一个文件和文件夹对象
        for (File file : files) {
            // 如果是文件, 并且是.java文件, 就打印在控制台
            if (file.isFile() && file.getName().endsWith(".java")) {
                System.out.println(file);
            } else if (file.isDirectory()) {
                // 说明是文件夹, 进入这个文件夹, 继续查找.java文件
                // 思路: 需要调用一个方法, 进入文件夹查找.java文件, 发现自己这个方法就是解决此问题, 递归调用.
                if (file.listFiles() != null) {
                    printJavaFile(file);
                }
            }
        }
    }
}
