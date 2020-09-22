#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	while (true) {
		string a;
		getline(cin, a);
		if (a == "END") {
			break;
		}
		reverse(a.begin(), a.end());
		cout << a << endl;
	}
	
}
