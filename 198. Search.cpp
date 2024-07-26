//  198. Поиск

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using Lint = long long int;

int main() {
    Lint t;
    cin >> t;
    vector<Lint> ans;
    
    for (Lint i = 0; i < t; i++) {
        Lint n, k;
        cin >> n >> k;
        vector<Lint> mas(n);
        
        for (Lint j = 0; j < n; j++) {
            cin >> mas[j];
        }
        
        Lint m = *max_element(mas.begin(), mas.end());
        if (m <= 0) {
            ans.push_back(m);
        } else {
            Lint ans1 = 0;
            vector<vector<Lint>> dp_1_i(n+2, vector<Lint>(k+1, 0));
            
            for (Lint i = 1; i <= n; i++) {
                dp_1_i[i][0] = dp_1_i[i-1][0] + mas[i-1];
                ans1 = max(ans1, dp_1_i[i][0]);
            }
            
            for (Lint i = 1; i <= n; i++) {
                for (Lint j = 1; j <= k; j++) {
                    dp_1_i[i][j] = max(dp_1_i[i-1][j] + mas[i-1], dp_1_i[i-1][j-1]);
                    ans1 = max(ans1, dp_1_i[i][j]);
                }
            }
            
            for (Lint i = 1; i <= n; i++) {
                for (Lint j = 0; j <= k; j++) {
                    if (i > 1)
                        dp_1_i[i][j] = max(dp_1_i[i][j], dp_1_i[i-1][j]);
                    if (j > 0)
                        dp_1_i[i][j] = max(dp_1_i[i][j], dp_1_i[i][j-1]);
                }
            }
            
            vector<vector<Lint>> dp_i_n(n+2, vector<Lint>(k+1, 0));
            
            for (Lint i = n; i >= 1; i--) {
                dp_i_n[i][0] = dp_i_n[i+1][0] + mas[i-1];
                ans1 = max(ans1, dp_i_n[i][0]);
            }
            
            for (Lint i = n; i >= 1; i--) {
                for (Lint j = 1; j <= k; j++) {
                    dp_i_n[i][j] = max(dp_i_n[i+1][j] + mas[i-1], dp_i_n[i+1][j-1]);
                    ans1 = max(ans1, dp_i_n[i][j]);
                }
            }
            
            for (Lint i = n; i >= 1; i--) {
                for (Lint j = 0; j <= k; j++) {
                    if (i < n)
                        dp_i_n[i][j] = max(dp_i_n[i][j], dp_i_n[i+1][j]);
                    if (j > 0)
                        dp_i_n[i][j] = max(dp_i_n[i][j], dp_i_n[i][j-1]);
                }
            }
            
            for (Lint i = 1; i < n; i++) {
                for (Lint j = 0; j <= k; j++) {
                    ans1 = max(ans1, dp_1_i[i][j] + dp_i_n[i+1][k-j]);
                }
            }
            
            vector<vector<Lint>> dp(n+1, vector<Lint>(k+1, 0));
            Lint ans2 = 0;
            
            for (Lint i = 1; i <= n; i++) {
                dp[i][0] = max(dp[i-1][0] + mas[i-1], Lint(0));
                ans2 = max(ans2, dp[i][0]);
            }
            
            for (Lint i = 1; i <= n; i++) {
                for (Lint j = 1; j <= k; j++) {
                    dp[i][j] = max({ dp[i-1][j] + mas[i-1], dp[i-1][j-1], Lint(0) });
                    ans2 = max(ans2, dp[i][j]);
                }
            }
            
            ans.push_back(max({ m, ans1, ans2 }));
        }
    }
    
    for (Lint i : ans) {
        cout << i << endl;
    }
    
    return 0;
}