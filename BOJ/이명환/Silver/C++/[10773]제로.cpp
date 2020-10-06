#include <iostream>
#include <stack>
#include <string>
using namespace std;


stack <int> numbers;

int main() {
    int N; cin >> N;
    while (N--) {
        int temp; cin >> temp;
        if (temp == 0) {
            numbers.pop();
        }
        else {
            numbers.push(temp);
        }
    }
    int result = 0; 

    while (!numbers.empty()) {
        result += numbers.top();
        numbers.pop();
    }
    cout << result;

}