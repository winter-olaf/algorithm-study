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
		bool palindrome = true;
		int z=0;
		getline(cin, a);
		for (int i = a.size()-1; i >=0; i--) {
			if (toupper(a[i]) == toupper(a[z])) {}
			else {
				cout << "No" << endl;
				palindrome = false;
				break;
			}
			z++;
		}
		if (palindrome) {
			cout << "Yes" << endl;
		}
	}
	
}
