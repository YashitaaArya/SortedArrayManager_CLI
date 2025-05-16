# Sorted Array Manager (CLI Version)

This is a Command-Line Interface (CLI) based project written in C++ that implements core operations on a sorted array using Binary Search. It allows users to search, insert, and delete elements while ensuring the array remains sorted at all times.
The program is modularized using separate header files for each operation (binary search, insertion, deletion, and utility display), demonstrating good software design principles.

---

## Features

- Search for an element using Binary Search.
- Delete an element while maintaining the sorted order.
- Insert a new element into the array keeping it sorted.
- Interactive user prompts for easy operation (CLI-based interaction).

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YashitaaArya/SortedArrayManager_CLI.git
   cd SortedArrayManager_CLI
   ```
2. **Compile the code:**

   Make sure you have a C++ compiler installed.

   ```bash
   g++ -o BinarySearchApp main.cpp
   ```
3. **Run the executable:**
   ```bash
   ./BinarySearchApp      # On Linux/macOS
    BinarySearchApp.exe    # On Windows
   ```
4. **Follow on-screen instructions to search, insert, or delete elements.**

## Code Structure
    main.cpp : Contains the main program logic.
    Functions:
    - binarySearch() : Performs binary search on the array.
    - insert() : Inserts an element into the sorted array.
    - deleteElement() : Deletes an element from the array.

## Example
```bash
Enter the size of array: 5
Enter the elements:
1 3 5 7 9
Enter the element to be searched: 5
Element found at 3 position.
Do you wish to delete the same element? (y/n)
y
Successfully deleted!
1 3 7 9
Continue the search? (yes/no)
no
```
## Requirements
  C++ compiler (g++, clang++, or Visual Studio)
  Basic command-line environment

## License
  This project is licensed under the MIT License.
  
---

## Author
 Yashitaa Arya

