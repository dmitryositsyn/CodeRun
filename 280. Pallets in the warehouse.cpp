//  280. Поддоны на складе

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int calculate(vector<vector<int>>& pallets) {
    int temp = 0;
    for (int i = 0; i < pallets.size(); i++) {
        if (pallets[i][0] < pallets[i][1]) {
            temp = pallets[i][0];
            pallets[i][0] = pallets[i][1];
            pallets[i][1] = temp;
        }
    }
    int res = 0;
    sort(pallets.begin(), pallets.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] != b[0]) {
            return a[0] < b[0];
        }
        return b[1] < a[1];
    });
    
    vector<int> dp(pallets.size(), 0);
    int maxVal = INT_MIN;
    for (int j = pallets.size() - 1; j >= 0; j--) {
        maxVal = max(maxVal, pallets[j][1]);
        dp[j] = maxVal;
    }
    
    for (int i = 0; i < pallets.size(); i++) {
        int start = i + 1;
        int end = pallets.size() - 1;
    
        while (start <= end) {
            int middle = start + (end - start) / 2;
    
            if (pallets[middle][0] > pallets[i][0]) {
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }
    
        if (start >= dp.size() || dp[start] <= pallets[i][1]) {
            res++;
        }
    }

    return res;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> pallets(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> pallets[i][0] >> pallets[i][1];
    }
    
    cout << calculate(pallets) << endl;
    
    return 0;
}