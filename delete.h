#ifndef DELETE_H
#define DELETE_H

#include <iostream>
#include "search.h"
using namespace std;

void deleteElement(int arr[], int& n, int a) {
    int pos = binarySearch(arr, n, a);
    if (pos != -1) {
        for (int i = pos; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }
        n--;
    } else {
        cout << "Element doesn't exist!" << endl;
    }
}

#endif
