#include <iostream>
#include <cmath>
using namespace std;

int min_jumps(int x, int y, int k) {
    int required_x = (x + k - 1) / k;  
    int required_y = (y + k - 1) / k;      
    int moves = 0;
    int current_x = 0, current_y = 0;
    while (required_x > 0 || required_y > 0) {
        if (moves % 2 == 0) {  
            if (required_x > 0) {
                current_x += k;
                required_x -= 1;
            }
        } else {  
            if (required_y > 0) {
                current_y += k;
                required_y -= 1;
            }
        }
        moves += 1;
    }
    
    return moves;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int x, y, k;
        cin >> x >> y >> k;
        cout << min_jumps(x, y, k) << endl;
    }
    return 0;
}

