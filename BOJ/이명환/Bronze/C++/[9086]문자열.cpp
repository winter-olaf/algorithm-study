#include <iostream>
#include <string>
using namespace std;
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int T; std::cin >> T;
	string a;
	for (int i = 0; i < T; i++) {
		cin >> a;
		cout << a[0] << a[a.size() - 1] << '\n';

	}
	
}
