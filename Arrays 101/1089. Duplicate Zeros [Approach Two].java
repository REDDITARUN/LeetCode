class Solution {
    public void duplicateZeros(int[] arr) {

         List<Integer> list = new ArrayList<>(); // Creating a new list
        for (int i = 0; i < arr.length ; i++) {
            if (arr[i] == 0) {
                list.add(0);
                list.add(0);
            } 
            else list.add(arr[i]);
        }  // USing for loop to transfer elements to array list, for each occurrence of zero, it adds two zeros to the ArrayList. For all other elements, it simply adds the element to the ArrayList.

        for (int i = 0; i < arr.length; i++) arr[i] = list.get(i); // convert list to array
        
    }
}