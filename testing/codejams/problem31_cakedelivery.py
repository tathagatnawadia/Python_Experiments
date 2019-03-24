cakes = [12, 2, 15, 9]

def isFine(list_of_cakes, remaining):
	if remaining == 0:
		return True
	if len(list_of_cakes) == 0:
		return False
	for cake in list_of_cakes:
		new_list = list_of_cakes[:]
		new_list.remove(cake)
		if cake == remaining:
			return True
		if cake < remaining and isFine(new_list, remaining-cake):
			return True
	return False

print(isFine(cakes, 100))

'''

import java.util.Scanner;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.stream.IntStream;

public class solution
{
    public Boolean canItBeDelivered(int[] listOfCakes, int goal)
	{
		Boolean[][] arr = new Boolean[2][goal+1];
		int i,j;
		for (j = 1; j <= goal; j++)
		{
            if(listOfCakes[1] == j-1)
                arr[0][j] = true;
            else
                arr[0][j] = false;
        }
		
		for (i = 2; i < listOfCakes.length; i++)
		{
	        for (j = 1; j <= goal; j++)
	        {
	            arr[1][j] = arr[0][j];
	            
	            if(listOfCakes[i] == j-1)
	                arr[1][j] = true;

	            if (arr[0][j] == false && listOfCakes[i] < j)
	            {
	                int col_search = j - listOfCakes[i];
	                if(arr[0][col_search] == true)
	                    arr[1][j] = true;
	            }
	        }
		        
	        for (j = 1; j <= goal; j++){
	            arr[0][j] = arr[1][j];
	        }
		}

		if(listOfCakes.length-1 == 1)
			return arr[0][goal];
		return arr[1][goal];
	}

	public Boolean canItBeDeliveredByRecursion(List<Integer> listOfCakes, int goal)
	{
		if(goal == 0)
			return true;
		if(listOfCakes.size() == 0)
			return false;
		for(int i=0; i<listOfCakes.size(); i++){
			if(listOfCakes.get(i) == goal)
				return true;
			List<Integer> newList = new ArrayList<>(listOfCakes);
			newList.remove(i);
			if(listOfCakes.get(i) < goal && canItBeDeliveredByRecursion(newList, goal-listOfCakes.get(i)))
				return true;
		}
			
		return false;
	}
	public static void main(String[] args) {
		// System.out.println("Hello World");
		solution myCakeShop = new solution();

	    Scanner scanner = new Scanner(System.in).useDelimiter("\n");;
		int numberOfDays = Integer.parseInt(scanner.next());
		List<Boolean> results = new ArrayList<Boolean>();

		for (int i=0; i < numberOfDays; i++)
		{
			String cakesList = scanner.next();
			String[] splited = cakesList.split(" ");
			// System.out.println(" DING DONG " + splited);
			int[] listOfCakes = Arrays.stream(splited).mapToInt(Integer::parseInt).toArray();
			int goal = Integer.parseInt(scanner.next())+1;

			int sum = IntStream.of(listOfCakes).sum();
			if(sum < goal)
				results.add(false);
			else if(sum == goal)
				results.add(true);
			else{
				if(goal <= 13){
					results.add(myCakeShop.canItBeDelivered(listOfCakes, goal));
				}
				else{
					ArrayList<Integer> newListOfCakes = new ArrayList<Integer>();
					for(int j = 1; j < listOfCakes.length; j++)
						newListOfCakes.add(listOfCakes[j]);
					results.add(myCakeShop.canItBeDeliveredByRecursion(newListOfCakes, goal-1));
				}
			}
		}

		for(int i=0; i<results.size(); i++)
		{
			if(results.get(i) == true)
				System.out.println("YES");
			else
				System.out.println("NO");
		}
	}

	
}
