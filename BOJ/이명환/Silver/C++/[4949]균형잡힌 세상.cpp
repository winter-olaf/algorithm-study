#include <iostream>
#include <stack>
#include <string>
using namespace std;

stack<int> st;


int main() {
    string S;

    while (1) {
        getline(cin, S);
        if (S.length() == 1 && S[0] == '.') {
            break;
        }

        while (!st.empty()) {
            st.pop();
        }

        bool flag = true;
        for (int i = 0; i < S.size(); i++) {
            if (S[i] == '(') {
                st.push(1);
            }
            else if (S[i] == '[') {
                st.push(2);
            }
            else if (S[i] == ')') {
                if (!st.empty() && st.top() == 1) {
                    st.pop();
                }
                else {
                    flag = false;
                    break;
                }
            }
            else if (S[i] == ']') {
                if (!st.empty() && st.top() == 2) {
                    st.pop();
                }
                else {
                    flag = false;
                    break;
                }
            }
        }

        if (flag && st.empty()) {
            cout << "yes" << endl;
        }
        else {
            cout << "no" << endl;
        }
    }
}