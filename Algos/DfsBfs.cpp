#include <iostream>
#include <vector>
#include <string>

using namespace std;

//
// Path Existence Check:
//
// Using DFS: Implement a depth-first search algorithm to explore the maze and determine whether any path exists from the start to the destination. 
// DFS does not guarantee the shortest path but can be used to simply check for connectivity.
//
// Shortest Path Calculation:
//
// Using BFS: Implement a breadth-first search algorithm to find the shortest path (measured by the number of moves) from the start to the destination. BFS is ideal here because it explores level-by-level, ensuring that the first time the destination is reached, the path is the shortest.
// typedef vector<int> Vector1D;
//
typedef vector<int> Vector1D;
typedef vector<Vector1D> Matrix2D;

Matrix2D maze = {
    {0, 1, 0, 0, 0},
    {0, 1, 0, 1, 0},
    {0, 0, 0, 1, 0},
    {1, 1, 0, 1, 0},
    {0, 0, 0, 0, 0}
};

Vector1D Start = {0, 0};
Vector1D End = {4, 4};

void ExploreMaze (Matrix2D& Maze, auto Start, auto End) {


}

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}



