class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string>ans(n);
        int k=1;
       while(n>=k){
           if(k%3==0&&k%5==0)ans[k-1]="FizzBuzz";
           else if(k%3==0)ans[k-1]="Fizz";
           else if(k%5==0)ans[k-1]="Buzz";
           else{
              ans[k-1]=to_string(k);
           }
           k++;
       } 
       return ans;
    }
};