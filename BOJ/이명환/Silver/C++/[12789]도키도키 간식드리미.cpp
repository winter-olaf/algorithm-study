#include <iostream>
#include <stack>
#include <queue>
#include <string>
using namespace std;

queue<int> line;
stack<int> wait;
int n;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
	cin >> n;

	for (int i = 0; i < n; i++) {
		int people;
		cin >> people;
		line.push(people);
	}


	int	order = 1;
	while (!line.empty()) {
		int num;
		if (!wait.empty()) {
			num = wait.top();
			if (num == order) {
				order += 1;
				wait.pop();
				continue;
			}
		}

		num = line.front();
		line.pop();
		if (num == order) {
			order += 1;
		}
		else {
			wait.push(num);
		}
	}
	bool answer = true;
	while (!wait.empty()) {
		int last;
		last = wait.top();
		wait.pop();
		if (last == order) {
			order += 1;
		}
		else {
			answer = false;
			break;
		}
	}

	if (answer) {
		cout << "Nice" << endl;
	}
	else {
		cout << "Sad" << endl;
	}


	
}