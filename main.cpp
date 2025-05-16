#include <iostream>
#include <string>
#include "search.h"
#include "insert.h"
#include "delete.h"
#include "utils.h"

using namespace std;

int main() {
    int n;
    cout << "Enter the size of array: ";
    cin >> n;
    int arr[100];  // Support for up to 100 elements
    cout << "Enter the sorted elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    while (true) {
        int searchItem;
        string ans;
        cout << "\nEnter element to search: ";
        cin >> searchItem;

        int pos = binarySearch(arr, n, searchItem);
        if (pos != -1) {
            cout << "Element found at position " << pos + 1 << ".\n";
            cout << "Delete this element? (y/n): ";
            cin >> ans;
            if (ans == "y") {
                deleteElement(arr, n, searchItem);
                cout << "Element deleted.\n";
                displayArray(arr, n);
            }
        } else {
            cout << "Element not found.\n";
            cout << "Insert this element? (y/n): ";
            cin >> ans;
            if (ans == "y") {
                insert(arr, n, searchItem);
                cout << "Element inserted.\n";
                displayArray(arr, n);
            }
        }

        cout << "Continue? (yes/no): ";
        cin >> ans;
        if (ans == "no") break;
    }

    return 0;
}
