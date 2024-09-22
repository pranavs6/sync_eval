#include<iostream>
using namespace std;


int sumarr(int arr[]){
  int res = 0;
  for(int itr = 0; itr < arr.length(); itr++){
    res = res + arr[itr];
  }

  return res;
}

int check(){
  int vals;
  string dirs;
  cin >> vals;
  int nums[vals], l = 0, r = vals - 1, ans = 0;

  for(int in = 0; in < vals; in++){
    cin >> nums[in];
  }
  cin >> dirs;

  while(l<r){
    while(dirs[l]!='L' and l<r){
      l = l + 1;
    }while(dirs[r]!='R' and l<r){
      r = r - 1;
    }
    ans = ans + sumarr(nums[l::r+1]);
    
  }
  cout << ans;
  return 0;
}

int main(){
  int n;
  cin >> n;

  for(int i_i = 0; i_i < n; i_i++){
    check();
  }

  return 0;
}
