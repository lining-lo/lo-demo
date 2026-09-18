package com.demo.thread_method;

public class ThreadNameDemo2 {
    /*
        线程设置名字和获取名字

        Thread类的方法:

            public String getName() : 获取线程名字
            public void setName() : 设置线程名字
            public static Thread currentThread() : 获取当前线程的对象

     */
    public static void main(String[] args) {
        MyRunnable mr = new MyRunnable();
        Thread t = new Thread(mr, "线程A");
        t.start();

        for (int i = 1; i <= 200; i++) {
            System.out.println(Thread.currentThread().getName() + "线程执行了" + i);
        }
    }
}

class MyRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 1; i <= 200; i++) {
            System.out.println(Thread.currentThread().getName() + "线程任务执行了" + i);
        }
    }
}