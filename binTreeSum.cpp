#include <bits/stdc++.h>

using namespace std;

struct Node {
  int data;
  Node *left;
  Node *right;

  Node(int val) {
    data = val;
    left = right = NULL;
  }
};

Node *buildTree(string str) {
  if (str.length() == 0 || str[0] == 'N') {
    return NULL;
  }

  vector<string> ip;

  istringstream iss(str);
  for (string str; iss >> str;) {
    ip.push_back(str);
  }

  Node *root = new Node(stoi(ip[0]));

  queue<Node *> queue;
  queue.push(root);

  int i = 1;
  while (!queue.empty() && i < ip.size()) {
    Node *currNode = queue.front();
    queue.pop();

    string currVal = ip[i];

    if (currVal != "N") {
      currNode->left = new Node(stoi(currVal));
      queue.push(currNode->left);
    }

    i++;

    if (i >= ip.size()) {
      break;
    }
    currVal = ip[i];

    if (currVal != "N") {
      currNode->right = new Node(stoi(currVal));
      queue.push(currNode->right);
    }
    i++;
  }

  return root;
}

bool hasPathSum(Node *node, int sum) {
  Node* temp;
  temp = node;
  if (temp != NULL) {
    if (temp->left != NULL && temp->right != NULL) {
      temp->left->data = temp->left->data + temp->data;
      temp->right->data = temp->right->data + temp->data;
      return hasPathSum(temp->left, sum) || hasPathSum(temp->right, sum);
    }
    if (temp->left != NULL) {
      temp->left->data = temp->left->data + temp->data;
      return hasPathSum(temp->left, sum);
    }
    if (temp->right != NULL) {
      temp->right->data = temp->right->data + temp->data;
      return hasPathSum(temp->right, sum);
    }
    return (temp->data == sum);
  }
  return 0;
}

int main() {
  int tc;
  scanf("%d ", &tc);
  while (tc--) {
    string treeString;
    getline(cin, treeString);
    Node *root = buildTree(treeString);
    int sum;
    scanf("%d", &sum);
    cout << hasPathSum(root, sum) << "\n";
  }
  return 0;
}
