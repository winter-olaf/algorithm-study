#include <iostream>
#include <queue>
#include <string>
using namespace std;


queue <int> q;

int main() {
    int N;
    cin >> N;
    while (true) {
        int temp;  cin >> temp;
        if (temp == -1) {
            if (q.empty()) {
                cout << "empty\n";
            }
            else {
                while (!q.empty())
                {
                    cout << q.front() << " ";
                    q.pop();
                }
                cout << '\n';
            }
            return 0;
        }
        else if (temp == 0) {
            q.pop();
        }
        else if (q.size() != N) {
            q.push(temp);
        }
    }
}