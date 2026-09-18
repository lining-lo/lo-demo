package com.demo.thread;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class ThreadDemo4 {
    /*
        开启线程的第三种方式 - 实现 Callable 接口

        1. 编写一个类实现Callable接口
        2. 重写call方法 (此方法存在返回值)
        3. 将线程任务代码写在call方法中
        4. 创建线程资源对象
        5. 创建线程任务对象, 封装线程资源
        6. 创建线程对象, 传入线程任务
        7. 使用线程对象调用start开启线程
     */
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        // 4. 创建线程资源对象
        MyCallable mc = new MyCallable();
        // 5. 创建线程任务对象, 封装线程资源
        FutureTask<Integer> task1 = new FutureTask<>(mc);
        FutureTask<Integer> task2 = new FutureTask<>(mc);
        // 6. 创建线程对象, 传入线程任务
        Thread t1 = new Thread(task1);
        Thread t2 = new Thread(task2);

        // 7. 使用线程对象调用start开启线程
        t1.start();
        t2.start();

        Integer result1 = task1.get();
        System.out.println("task1 返回的结果为:" + result1);

        Integer result2 = task2.get();
        System.out.println("task2 返回的结果为:" + result2);
    }
}

// 1. 编写一个类实现Callable接口
class MyCallable implements Callable<Integer> {

    // 2. 重写call方法 (此方法存在返回值)
    @Override
    public Integer call() throws Exception {
        // 3. 将线程任务代码写在call方法中
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        return sum;
    }
}
