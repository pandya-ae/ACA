#include <iostream>
#include <stdlib.h>
#include <bits/stdc++.h> 
using namespace std; 

// To heapify a subtree rooted with node i which is an index in arr[]. n is size of heap 
void heapify(int arr[], int n, int i) 
{ 
	int largest = i; // Initialize largest as root 
	int l = 2*i + 1; // left = 2*i + 1 
	int r = 2*i + 2; // right = 2*i + 2 
	// If left child is larger than root 
	if (l < n && arr[l] > arr[largest]) 
		largest = l; 
	// If right child is larger than largest so far 
	if (r < n && arr[r] > arr[largest]) 
		largest = r; 
	// If largest is not root 
	if (largest != i) 
	{ 
		swap(arr[i], arr[largest]); 
		// Recursively heapify the affected sub-tree 
		heapify(arr, n, largest); 
	} 
} 

// Main function to do heap sort 
void heapSort(int arr[], int n) 
{ 
	// Build heap (rearrange array) 
	for (int i = n / 2 - 1; i >= 0; i--) 
		heapify(arr, n, i); 
	// One by one extract an element from heap 
	for (int i = n - 1; i > 0; i--) 
	{ 
		// Move current root to end 
		swap (arr[0], arr[i]); 
		// Call max heapify on the reduced heap 
		heapify(arr, i, 0); 
	} 
} 

// Driver program to test above functions 
int main() 
{ 
	time_t start, end;
	time(&start);
	srand (time(0));	
	int n = 250000;
	int arr[n];
	for (int i = 0; i < n; i++)
		arr[i] = rand()%1000000;
	// Function call
	heapSort (arr, n); 
	time(&end);
	double time_taken = double(end - start); 
    cout << "Time taken by program is : " << fixed << time_taken << setprecision(5); 
    cout << " sec " << endl;  
	return 0; 
} 
