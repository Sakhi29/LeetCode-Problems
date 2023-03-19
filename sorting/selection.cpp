#include <iostream>
using namespace std;

int select(int arr[], int i, int n)
{
  int min = i;
  for (int j = i + 1; j < n; j++)
  {
    if (arr[min] > arr[j])
    {
      min = j;
    }
  }
  return min;
}
void selectionSort(int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    int min = select(arr, i, n);
    int temp = arr[min];
    arr[min] = arr[i];
    arr[i] = temp;
  }
}

int main()
{
  int arr[] = {1, 13, 3, 27, 7};
  selectionSort(arr, 5);
  for (int i = 0; i < 5; i++)
  {
    cout << arr[i] << " ";
  }
  return 0;
}