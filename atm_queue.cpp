#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Person {
  public:
    int num;
    int amount;

    Person(int n, int a) {
      num = n;
      amount = a;
    }
};

string getAns(vector<Person> q) {
  string ans = "";
  for (int i = 0; i < q.size(); i++) {
    ans += to_string(q[i].num);
    ans += " ";
  }
  return ans;
}

bool comparator(Person p1, Person p2) {
  if (p1.amount < p2.amount) {
    return true;
  }
  if (p1.amount == p2.amount && p1.num < p2.num) {
    return true;
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int N, X, a;
    cin >> N >> X;
    vector<Person> people;
    for (int j = 1; j <= N; j++) {
      cin >> a;
      Person temp(j, (int)ceil((a+0.0)/(X+0.0)));
      people.push_back(temp);
    }
    sort(people.begin(), people.end(), comparator);
    cout << "Case #" << i << ": " << getAns(people) << endl;
  }
  return 0;
}
