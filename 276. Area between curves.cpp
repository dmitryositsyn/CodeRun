//  276. Площадь между кривыми

#include <iostream>
#include <vector>
#include <cmath>

using Lint = long long int;

double integrate_abs_polynomial(double a, double b, double A, double B, double C) {
    if (A==0) {
        if (B==0) {
            return (b-a)*std::abs(C);
        }
        else {
            if ((a < -C/B) && (-C/B < b)) {
                return 0.5*std::abs(B*a+C)*std::abs(-C/B - a) + 0.5*std::abs(B*b+C)*std::abs(b+C/B);
            }
            else {
                return 0.5*(b-a)*(std::abs(B*a+C) + std::abs(B*b+C));
            }
        }
    }
    else {
        double D = B*B - 4.*A*C;
        if (D<=0) {
            return std::abs((A/3.)*(b*b*b - a*a*a) + (B/2.)*(b*b - a*a) + C*(b-a));
        }
        else {
            double x1 = (-B - std::sqrt(D))/(2.*A);
            double x2 = (-B + std::sqrt(D))/(2.*A);
            if (x1 > x2){
                std::swap(x1, x2);
            }
            if ((a <= x1) && (x1 < x2) && (x2 <= b)) {
                double S1 = std::abs((A/3.)*(x1*x1*x1 - a*a*a) + (B/2.)*(x1*x1 - a*a) + C*(x1-a));
                double S2 = std::abs((A/3.)*(x2*x2*x2 - x1*x1*x1) + (B/2.)*(x2*x2 - x1*x1) + C*(x2-x1));
                double S3 = std::abs((A/3.)*(b*b*b - x2*x2*x2) + (B/2.)*(b*b - x2*x2) + C*(b-x2));
                return S1 + S2 + S3;
            }
            else if ((x1 <= a) && (a <= x2) && (x2 <= b)) { 
                double S1 = std::abs((A/3.)*(x2*x2*x2 - a*a*a) + (B/2)*(x2*x2 - a*a) + C*(x2-a));
                double S2 = std::abs((A/3.)*(b*b*b - x2*x2*x2) + (B/2)*(b*b - x2*x2) + C*(b-x2));
                return S1 + S2;
            }
            else if ((a <= x1) && (x1 <= b) && (b <= x2)) {
                double S1 = std::abs((A/3.)*(x1*x1*x1 - a*a*a) + (B/2.)*(x1*x1 - a*a) + C*(x1-a));
                double S2 = std::abs((A/3.)*(b*b*b - x1*x1*x1) + (B/2.)*(b*b - x1*x1) + C*(b-x1));
                return S1 + S2;
            }
            else {
                return std::abs((A/3.)*(b*b*b - a*a*a) + (B/2)*(b*b - a*a) + C*(b-a));
            }
        }
    }
}


int main()
{
    Lint n, m;
    std::cin >> n >> m;
    std::vector<Lint> intervals_1;
    std::vector<std::pair<Lint, std::pair<Lint, Lint>>> coefficients_1;
    
    std::vector<Lint> intervals_2;
    std::vector<std::pair<Lint, std::pair<Lint, Lint>>> coefficients_2;

    for(Lint i=0; i<=n; i++) {
        Lint temp;
        std::cin >> temp;
        intervals_1.push_back(temp);
    }
    for(Lint i=0; i<n; i++){
        Lint a, b, c;
        std::cin >> a >> b >> c;
        std::pair<Lint, Lint> p1 (b, c);
        std::pair<Lint, std::pair<Lint, Lint>> p (a, p1);
        coefficients_1.push_back(p);
    }

    for(Lint i=0; i<=m; i++){
        Lint temp;
        std::cin >>  temp;
        intervals_2.push_back(temp);
    }
    for(Lint i=0; i<m; i++){
        Lint a, b, c;
        std::cin >> a >> b >> c;
        std::pair<Lint, Lint> p1 (b, c);
        std::pair<Lint, std::pair<Lint, Lint>> p (a, p1);
        coefficients_2.push_back(p);
    }
    
    double ans = 0.0;
    Lint previous = intervals_1[0];
    Lint l = 1;
    Lint r = 1;
    
    while (previous != intervals_1[n]) {
        
        Lint A1 = coefficients_1[l-1].first;
        Lint B1 = coefficients_1[l-1].second.first;
        Lint C1 = coefficients_1[l-1].second.second;
        
        Lint A2 = coefficients_2[r-1].first;
        Lint B2 = coefficients_2[r-1].second.first;
        Lint C2 = coefficients_2[r-1].second.second;
        
        if (intervals_1[l] < intervals_2[r]) {
            ans += integrate_abs_polynomial(previous, intervals_1[l], A1-A2, B1-B2, C1-C2);
            previous = intervals_1[l];
            l += 1;
        }
        else if (intervals_1[l] > intervals_2[r]) {
            ans += integrate_abs_polynomial(previous, intervals_2[r], A1-A2, B1-B2, C1-C2);
            previous = intervals_2[r];
            r += 1;
        }
        else {
            ans += integrate_abs_polynomial(previous, intervals_1[l], A1-A2, B1-B2, C1-C2);
            previous = intervals_1[l];
            l += 1;
            r += 1;
        }
    }
    std::cout.precision(20);
    std::cout << ans;
    
    return 0;
}