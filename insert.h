#ifndef INSERT_H
#define INSERT_H

void insert(int arr[], int& n, int a) {
    int i = n - 1;
    while (i >= 0 && arr[i] > a) {
        arr[i + 1] = arr[i];
        i--;
    }
    arr[i + 1] = a;
    n++;
}

#endif
