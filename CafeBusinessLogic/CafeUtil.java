import java.util.ArrayList;
import java.util.Arrays;
public class CafeUtil{
    CafeUtil(){

    }
    int getStreakGoal(int numWeeks){
        int streak = 0;
        for(int a=0; a <=numWeeks; a++){
            streak = streak + a;
        }
        return streak;
    }
    double getOrderTotal(double[] prices){
        double total= 0.0;
        for(int a=0; a < prices.length; a++){
            total = total + prices[a];
        }
        return total;
    }
    void displayMenu(ArrayList<String> menuitems){
        for(int a = 0; a < menuitems.size(); a++){
        System.out.println(a +" "+menuitems.get(a));
        }
    
    }
    void addCustomer(ArrayList<String> customers){
        System.out.println("Please enter your name:");
        String userName = System.console().readLine();
        System.out.println("hello"+userName);
        System.out.println("There are "+customers.size()+" people ahead of you!");
        customers.add(userName);
        for(int a = 0; a < customers.size(); a++){
            System.out.println(a +" "+customers.get(a));
        }
    }
    void printPriceChart(String product, double p, int maxQuantity){
        double price = p;
        System.out.println(product);
        for(int a = 1; a <=maxQuantity; a++){
            System.out.println(a+"-$"+price);
            price=price+p-.50;
        }
    }
}
