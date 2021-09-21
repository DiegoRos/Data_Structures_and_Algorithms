package Java;

import java.util.HashSet;
import java.util.Set;

public class MySet {

    public static void main(String[] args){
        Set<Integer> mySet = new HashSet<Integer>();

        mySet.add(2);
        mySet.add(523);
        mySet.add(243);

        System.out.println(mySet);
    }
}
