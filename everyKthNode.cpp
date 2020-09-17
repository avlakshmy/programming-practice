#include <iostream>
using namespace std;

struct Node {
  int data;
  struct Node* next;

  Node(int x){
    data = x;
    next = NULL;
  }
};

void append(struct Node** head_ref, struct Node **tail_ref, int new_data) {
  struct Node* new_node = new Node(new_data);

  if (*head_ref == NULL) {
    *head_ref = new_node;
  }
  else {
    (*tail_ref)->next = new_node;
  }

  *tail_ref = new_node;
}

Node* deleteK(Node *head,int K) {
  if (K == 1) {
    return NULL;
  }
  if (head == NULL) {
    return NULL;
  }
  if (head->next == NULL) {
    return head;
  }
  int i;
  Node* temp;
  Node* temp1;
  temp = head;
  while (temp) {
    i = 1;
    while (temp && i < K) {
      temp = temp->next;
      i = i+1;
    }
    if (temp) {
      temp1 = temp->next;
      if (temp1) {
        temp->data = temp1->data;
        temp->next = temp1->next;
      }
      else {
        temp = head;
        while (temp->next->next) {
            temp = temp->next;
        }
        temp->next = NULL;
      }
    }
  }
  return head;
}

int main() {
  int T, i, n, l;
  cin >> T;
  while (T--) {
    struct Node *head = NULL, *tail = NULL;
    cin >> n;
    for (i = 1; i <= n; i++) {
      cin >> l;
      append(&head, &tail, l);
    }
    int K;
    cin >> K;
    Node *res = deleteK(head, K);
    Node *temp = res;
    while (temp != NULL) {
      cout << temp->data << " ";
      temp = temp->next;
    }
    cout << endl;
  }
  return 0;
}
