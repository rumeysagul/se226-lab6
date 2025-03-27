#include <iostream>
using namespace std;

int recursivesum(int n) {
    if (n == 0)
        return 0;
        return n + recursivesum(n - 1);
    }



int recursivesum() {
    int n;
    cout << "enter a number: ";
    cin >> n;
    return recursivesum(n);
}

int main() {
    cout << recursivesum() << endl;
}



