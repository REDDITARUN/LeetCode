     
class Solution {
public int numberOfSteps(int num) {

  return helper(num,0);  //helper function to pass no. of steps as an argument
}

int helper(int num,int steps){
    if(num==0){
        return steps;    //if all the steps end and the no. finaaly becomes 0
    }

    if(num%2==0){    //for even number
        return helper(num/2,steps+1);
    }

    else{           //for odd number
        return helper(num-1,steps+1);
    }
}

}
