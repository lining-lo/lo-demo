package com.demo.test;

import java.io.File;

public class FileTest5 {
    /*
        需求: 键盘录入一个文件夹路径，统计文件夹的大小
     */
    public static void main(String[] args) {
        File dir = FileTest1.getDir();

        long length = getDirLength(dir);

        System.out.println("字节数量为:" + length);
    }

    private static long getDirLength(File dir) {
        long result = 0;
        File[] files = dir.listFiles();
        for (File file : files) {
            if (file.isFile()) {
                result += file.length();
            } else {
                if (file.listFiles() != null) {
                    result += getDirLength(file);
                }
            }
        }
        return result;
    }
}
