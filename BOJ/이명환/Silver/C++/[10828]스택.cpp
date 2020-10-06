// 10828 - 스택 

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(){
    int N; cin >> N;
    stack <int> s;
    while(N--){
        string command; cin >> command;
        if(command == "push"){
            int X; cin >> X;
            s.push(X);
        }
        else if(command == "pop"){
            if(s.empty()){
                cout << "-1\n";
            }
            else {
                cout << s.top() << '\n';
                s.pop();
            }
        }
        else if(command == "size"){
            cout << s.size() << '\n';
        }
        else if(command == "empty"){
            cout << s.empty() << '\n';
        }
        else if(command == "top"){
            if(s.empty()) cout << "-1\n";
            else {
                cout << s.top() << '\n';
            }
        }
    }
}