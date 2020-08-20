#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<numeric>

using namespace std;

class Person {
    protected:
        string name;
        int age;

    public:
        virtual void putdata(){}
        virtual void getdata(){}
};

class Professor : public Person {
    private:
        int publications;
        int cur_id;
        
    public:
        static int count;

        Professor() {
            count += 1;
            cur_id = count;
        }

        void getdata() {
            cin >> name;
            cin >> age;
            cin >> publications;
        }

        void putdata() {
            cout << name << " " << age << " " << publications << " " << cur_id << endl;
        }
};

class Student : public Person {
    private:
        vector<int> marks;
        int cur_id;

    public:
        static int count;

        Student() {
            for (int i = 0; i < 6; i++) {
                marks.push_back(0);
            }
            count += 1;
            cur_id = count;
        }

        void getdata() {
            cin >> name;
            cin >> age;
            cin >> marks[0] >> marks[1] >> marks[2] >> marks[3] >> marks[4] >> marks[5];
        }

        void putdata() {
            cout << name << " " << age << " " << accumulate(marks.begin(), marks.end(), 0) << " " << cur_id << endl;
        }
};

int Student::count = 0;
int Professor::count = 0;

int main() {
    int n, val;
    cin >> n; // The number of objects that is going to be created.
    Person *per[n];

    for (int i = 0; i < n; i++) {
        cin >> val;
        
        if (val == 1)
            per[i] = new Professor; // If val is 1 current object is of type Professor
        else 
            per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user
    }

    for (int i = 0; i < n; i++)
        per[i]->putdata(); // Print the required output for each object

    return 0;
}
