package Java;

import java.util.HashMap;
import java.util.Map;


public class MyMap{
    public static void main(String[] args){
        Map<String, Integer> myMap = new HashMap<>();

        myMap.put("First", 2);
        myMap.put("Second", 523);
        myMap.put("Other", 243);

        System.out.println(myMap);
    }
}