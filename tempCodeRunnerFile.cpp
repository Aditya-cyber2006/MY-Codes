#include <bits/stdc++.h>
using namespace std;

int solve()
{
    int n,c=0;
    cin>>n;
    int a[2*n];
    
    for(int i=0;i<2*n;i++)
        cin>>a[i];
    for(int i=0;i<2*n ;i++){
        c=0;
        for(int j=0;j<2*n;j++){
            if(a[i]==a[j]) {
                c++;
                
            }
        if (c>2){
            // cout<<"NO"<<endl;
            
            return 0;
        }     
            
        }
    }

    // cout<<"YES"<<endl;
    return 1;
    
}
int main() {
	// your code goes here
	
    int t;
    cin>>t;
    while(t--) 
    {
        int r=solve();
        if(r==0) cout<<"NO"<<endl;
        if(r==1) cout<<"YES"<<endl;
        
    }
}
