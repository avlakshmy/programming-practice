#include<iostream>

using namespace std;

class A
{
    public:
        A(){
            callA = 0;
        }
    private:
        int callA;
        void inc(){
            callA++;
        }

    protected:
        void func(int & a)
        {
            a = a * 2;
            inc();
        }
    public:
        int getA(){
            return callA;
        }
};

class B
{
    public:
        B(){
            callB = 0;
        }
    private:
        int callB;
        void inc(){
            callB++;
        }
    protected:
        void func(int & a)
        {
            a = a * 3;
            inc();
        }
    public:
        int getB(){
            return callB;
        }
};

class C
{
    public:
        C(){
            callC = 0;
        }
    private:
        int callC;
        void inc(){
            callC++;
        }
    protected:
        void func(int & a)
        {
            a = a * 5;
            inc();
        }
    public:
        int getC(){
            return callC;
        }
};

class D : public A, B, C
{

	int val;
	public:
		//Initially val is 1
		 D()
		 {
		 	val = 1;
		 }


		 //Implement this function
		 void update_val(int new_val)
		 {
            int a, b, c;
            a = 0;
            b = 0;
            c = 0;
            while (new_val % 2 == 0) {
                a += 1;
                new_val /= 2;
            }
            while (new_val % 3 == 0) {
                b += 1;
                new_val /= 3;
            }
            while (new_val % 5 == 0) {
                c += 1;
                new_val /= 5;
            }

            for (int i = 0; i < a; i++) {
                A::func(val);
            }
            for (int i = 0; i < b; i++) {
                B::func(val);
            }
            for (int i = 0; i < c; i++) {
                C::func(val);
            }
			
		 }
		 //For Checking Purpose
		 void check(int); //Do not delete this line.
};

