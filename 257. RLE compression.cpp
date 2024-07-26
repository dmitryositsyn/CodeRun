//  257. RLE-сжатие

#include <iostream>
#include <vector>

using namespace std;
using Lint = long long int;

Lint counting(Lint count) {
    if (count == 1) {
        return 1;
    } 
    else {
        Lint result = 0;
        while (count > 0) {
            result += 1;
            count /= 10;
        }
        return result + 1;
    }
}

Lint binary_search(vector<Lint>& start, Lint num) {
    Lint l = 0;
    Lint r = start.size();
    while (l < r) {
        Lint cur = (l + r) / 2;
        if (start[cur] < num) {
            l = cur + 1;
        } 
        else {
            r = cur;
        }
    }
    return l;
}

int main() {
    string s;
    cin >> s;
    vector<Lint> start;
    vector<Lint> lens;
    vector<Lint> cur_rle;
    Lint count = 0;
    for (Lint i = 0; i < s.length(); i++) {
        char sym = s[i];
        if (isdigit(sym)) {
            count = count * 10 + (sym - '0');
        } 
        else {
            cur_rle.push_back(i + 1);
            if (start.empty()) {
                start.push_back(1);
            } 
            else {
                start.push_back(start.back() + lens.back());
            }
            if (count == 0) {
                lens.push_back(1);
            } 
            else {
                lens.push_back(count);
            }
            count = 0;
        }
    }

    Lint q;
    cin >> q;

    for (Lint i = 0; i < q; i++) {
        Lint l_i, r_i;
        cin >> l_i >> r_i;
        Lint a = binary_search(start, l_i);
        Lint b = binary_search(start, r_i);
        Lint ans = 0;

        if ((a < start.size() && start[a] != l_i) || a == start.size()) {
            a -= 1;
        }
        if ((b < start.size() && start[b] != r_i) || b == start.size()) {
            b -= 1;
        }

        if (a == b || (a == start.size() - 1 && b == start.size())) {
            Lint count = r_i - l_i + 1;
            cout << counting(count) << endl;
        } 
        else if (a != b) {
            Lint count1 = start[a] + lens[a] - l_i;
            Lint count2 = r_i - start[b] + 1;
            ans += counting(count1);
            ans += counting(count2);
            if (b - a > 1) {
                ans += cur_rle[b - 1] - cur_rle[a];
            }
            cout << ans << endl;
        }
    }

    return 0;
}