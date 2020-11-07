#include <iostream>
#include <queue>
#include <string>
using namespace std;

queue<int> que;


int main() {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		que.push(i);
	}
	
	while (que.size() != 1) {
		que.pop();
		int tmp = que.front();
		que.pop();
		que.push(tmp);	
	}
	cout << que.front() << endl;
}