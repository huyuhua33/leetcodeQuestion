#include <iostream>
#include <string>

using namespace string;
using namespace std;

class Solution {

public:
    string customSortString(string order, string s) {
		now_index = 0;
		for (int i = 0; i < order.length(); i++) {
			for (int j = i; j < s.length(); j++) {
				if(s[j] == order[i]) {
					char TMP = s[now_index];
					s[now_index] = s[j];
					s[j] = TMP;
					now_index++;
				} 
		}
		return s;
    }

	int main() {
		string testcase1 = "cba";
		string testcase2 = "abcd"
		string ans = "";

		ans = customSortString(testcase1, testcase2);
		cout << ans << endl;

	}
};

