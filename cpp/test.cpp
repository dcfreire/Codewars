#include <math.h>
#include <iostream>
using namespace std;
//Evaluates C(n,k) and verifies if it's greater than or equal to k
long long binomial(int x,int n,int k){

    int i;
    long long int answer=0;
    double aux=1;

    //Calculates C(n,k) using the formula: C(n,k): sum_i_0^k {(n-i+1)/i}
    for(i=1;i<=n;i++){

            aux*=(float)x+1-i;
            aux/=(float)i;
            answer+=aux;

            if(answer>k) break;
    }

    return answer;
}
int main()
{
    int n; //Number of eggs
    int k; //Number of floors

    cout<<"Egg dropping puzzle: ( O(n log k)  solution )\n\n";

    cout<<"Number of floors:";
    cin>>k;

    cout<<"\nNumber of eggs:";
    cin>>n;

    //Binary search variables:
    //Mid: middle
    //Upper: upper limit
    //Inf: inferior limit

    int mid,upper,inf;

    upper=k;
    inf=0;
    mid=(upper+inf)/2;

    //Binary search
    while(upper-inf>1){

        //Finds the middle
        mid=inf+(upper-inf)/2;

        //Define new limits
        if(binomial(mid,n,k)<k) inf=mid;
        else upper=mid;

    }

    cout << inf+1;
}
