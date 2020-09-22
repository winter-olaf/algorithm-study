#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int T; cin >> T;
	cin.ignore();
	while (T--) {
		string a;
		getline(cin, a);
		a[0] = toupper(a[0]);
		cout << a << endl;
	}
	
}
