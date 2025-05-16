#ifndef UTILS_H
#define UTILS_H

#include <iostream>
using namespace std;

void displayArray(int arr[], int n) {
    cout << "Current Array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}

#endif
