package com.demo.pool;

import java.util.concurrent.*;

public class ThreadPoolDemo2 {
    /*
        自定义线程池

        1. 有界队列  new ArrayBlockingQueue<>(10)
        2. 无界队列  new LinkedBlockingQueue<>()
     */
    public static void main(String[] args) {
        ThreadPoolExecutor pool = new ThreadPoolExecutor(
                2,
                5,
                60,
                TimeUnit.SECONDS,
                new ArrayBlockingQueue<>(10),
                Executors.defaultThreadFactory(),
                new ThreadPoolExecutor.CallerRunsPolicy());

        for(int i = 1; i <= 16; i++){
            pool.submit(new Runnable() {
                @Override
                public void run() {
                    System.out.println(Thread.currentThread().getName() + "--- 提交了任务");
                }
            });
        }

    }
}
