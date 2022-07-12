import atexit
import sys
import io


class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array

    def merge(self, arr, s, m, e):
        i, j = s, m
        inv_cnt = 0
        tmp = []
        while i < m and j <= e:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                inv_cnt += (m-i)
                j += 1
        while i < m:
            tmp.append(arr[i])
            i += 1
        while j <= e:
            tmp.append(arr[j])
            j += 1
        j = 0
        for i in range(s, e+1):
            arr[i] = tmp[j]
            j += 1
        return inv_cnt

    def mergeSort(self, arr, s, e):
        inv_cnt = 0
        if s < e:
            mid = (s+e)//2
            inv_cnt += self.mergeSort(arr, s, mid)
            inv_cnt += self.mergeSort(arr, mid+1, e)
            inv_cnt += self.merge(arr, s, mid+1, e)
        return inv_cnt

    def inversionCount(self, arr, n):
        # Your Code Here
        return self.mergeSort(arr, 0, n-1)
# {
#  Driver Code Starts
# Initial Template for Python 3


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a, n))
# } Driver Code Ends
