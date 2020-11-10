//2644 - recursion
#include <queue>
#include <iostream>
#include <vector>

using namespace std;

vector <vector <int> > fam(101);
int chk[101];
int start, end1;

int dfs(int person, int count){
    chk[person] = 1;
    if(person == end1) return count;
    for(int i = 0; i < fam[person].size(); i++){
        if (chk[fam[person][i]] == false){
            return dfs(fam[person][i], count+1);
        }
    }
    return 0;
}

int main(){
    int N; cin >> N;
    cin >> start >> end1;
    int m; cin >> m;
    for(int i = 0; i < m; i++){
        int x, y; cin >> x >> y;
        fam[x].push_back(y); fam[y].push_back(x);
    }
    
    int ans = dfs(start, 0);
    
    if(ans== 0) cout << "-1\n";
    else cout << ans << '\n';
}