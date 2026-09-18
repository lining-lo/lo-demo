package com.demo.test;

import java.util.ArrayList;
import java.util.List;

public class ThreadTest1 {
    /*
        需求：某电影院目前正在上映国产大片，共有100张票，而它有3个窗口卖票，请设计一个程序模拟该电影院卖票
                - 多条线程共享操作同一份资源
     */
    public static void main(String[] args) {
        TicketTask task = new TicketTask();
        List< String> threads = new ArrayList<>();
        threads.add("窗口A");
        threads.add("窗口B");
        threads.add("窗口C");
        threads.add("窗口D");
        System.out.println(threads);


        /*Thread t1 = new Thread(task, "窗口A");
        Thread t2 = new Thread(task, "窗口B");
        Thread t3 = new Thread(task, "窗口C");

        t1.start();
        t2.start();
        t3.start();*/
    }
}

class TicketTask implements Runnable {

    int tickets = 1000;

    @Override
    public void run() {
        while (true) {
            synchronized (TicketTask.class) {
                if (tickets <= 0) {
                    break;
                }

                System.out.println(Thread.currentThread().getName() + "卖出了第" + tickets + "号票");
                tickets--;
            }
        }
    }
}