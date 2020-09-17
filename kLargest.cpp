#include <bits/stdc++.h>
using namespace std;

vector<int> kLargest(int arr[], int n, int k) {
  priority_queue< int, vector<int>, greater<int> > minHeap;
  int i;
  for (i = 0; i < k; i++) {
    minHeap.push(arr[i]);
  }
  while (i < n) {
    if (minHeap.top() < arr[i]) {
      minHeap.pop();
      minHeap.push(arr[i]);
    }
    i++;
  }
  vector<int> larg;
  while (!minHeap.empty()) {
    larg.push_back(minHeap.top());
    minHeap.pop();
  }
  reverse(larg.begin(), larg.end());
  return larg;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n, k;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; i++) {
      cin >> arr[i];
    }
    auto ans = kLargest(arr, n, k);
    for (auto x : ans) {
      cout << x << " ";
    }
    cout << "\n";
  }
  return 0;
}
