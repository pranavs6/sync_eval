#include<iostream>
using namespace std;

int main(){
  int n;
  cin >> n;
  while(n>0) {
    int val;
    cin >> val;
    cout << (val%10) + ((val%100)-val%10)/10 << endl;
    n = n - 1;
  }
  return 0;
}
