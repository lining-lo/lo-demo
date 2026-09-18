package com.demo.properties;

import java.util.Properties;
import java.util.Set;

public class PropertiesDemo1 {
    /*
        Properties作为集合的使用

            Object setProperty (String key, String value) : 类似Map集合的put方法
            String getProperty (String key) : 类似Map集合的get方法
            Set<String> stringPropertyNames() : 类似Map是集合的keySet方法
     */
    public static void main(String[] args) {
        Properties prop = new Properties();

        prop.setProperty("username", "admin");
        prop.setProperty("password", "123456");

        String username = prop.getProperty("username");
        String password = prop.getProperty("password");

        System.out.println(username);
        System.out.println(password);

        System.out.println("--------------------------");

        Set<String> keySet = prop.stringPropertyNames();

        for (String key : keySet) {
            System.out.println(key + "---" + prop.getProperty(key));
        }
    }
}
