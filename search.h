#ifndef SEARCH_H
#define SEARCH_H

int binarySearch(int arr[], int n, int a) {
    int first = 0, last = n - 1;
    while (first <= last) {
        int mid = (first + last) / 2;
        if (arr[mid] == a) return mid;
        else if (arr[mid] < a) first = mid + 1;
        else last = mid - 1;
    }
    return -1;
}

#endif