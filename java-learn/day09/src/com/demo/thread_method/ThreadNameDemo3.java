package com.demo.thread_method;

import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

public class ThreadNameDemo3 {
    /*
        线程设置名字和获取名字

        Thread类的方法:

            public String getName() : 获取线程名字
            public void setName() : 设置线程名字
            public static Thread currentThread() : 获取当前线程的对象

     */
    public static void main(String[] args) throws Exception {
        MyCallable mc = new MyCallable();

        FutureTask<Integer> task1 = new FutureTask<>(mc);
        FutureTask<Integer> task2 = new FutureTask<>(mc);

        Thread t1 = new Thread(task1, "线程A: ");
        Thread t2 = new Thread(task2, "线程B: ");

        t1.start();
        t2.start();

        Integer result1 = task1.get();
        Integer result2 = task2.get();

        System.out.println(t1.getName() + "获取到的结果为:" + result1);
        System.out.println(t2.getName() + "获取到的结果为:" + result2);

    }
}

class MyCallable implements Callable<Integer> {
    @Override
    public Integer call() throws Exception {
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        return sum;
    }
}