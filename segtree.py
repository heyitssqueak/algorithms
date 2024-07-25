from collections import defaultdict
import math

class SegTree:
    def __init__(self, arr):
        def build(node, start, end):
            if start == end:
                self.nums[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(node*2, start, mid)
                build(node*2+1, mid+1, end)
                self.nums[node] = min(self.nums[node*2], self.nums[node*2+1])

        self.n = len(arr)
        self.nums = [-1 for _ in range(self.n * 4)]
        build(1, 0, self.n - 1)

    def show(self):
        layers = defaultdict(list)

        def sh(node, start, end):
            if start == end:
                layers[math.floor(math.log2(node))].append([self.nums[node]])
            else:
                mid = (start + end) // 2
                sh(node*2, start, mid)
                sh(node*2+1, mid+1, end)
                layers[math.floor(math.log2(node))].append([self.nums[node]])

        sh(1, 0, self.n - 1)
        for i in sorted(layers.keys()):
            for cell in layers[i]:
                if type(cell[0]) == list:
                    print(cell[0], end="")
                else:
                    print(f'[{cell[0]}]', end="")
            print()

    def minRange(self, lo, hi):
        def helper(node, start, end, l, r):
            print(start, end, end=" ")
            if r < start or end < l:
                print("disjoint")
                return math.inf;
            if l <= start and end <= r:
                print("covered")
                return self.nums[node]
            
            print("intersect")
            mid = (start + end) // 2
            vl = helper(node*2, start, mid, l, r)
            vr = helper(node*2+1, mid+1, end, l, r)
            return min(vl, vr)
        
        return helper(1, 0, self.n - 1, lo, hi)
    
    def update(self, index, val):
        def helper(node, index, val, l, r):
            if l == r:
                self.nums[node] = val
            else:
                m = (l + r) // 2
                if index <= m:
                    helper(node*2, index, val, l, m)
                else:
                    helper(node*2+1, index, val, m+1, r)
                self.nums[node] = min(self.nums[node*2], self.nums[node*2+1])

        helper(1, index, val, 0, self.n - 1)

# tree = SegTree([1,2,3,4,5,6,7,8])
# tree.update(5, 0)
# tree.show()
# print(tree.minRange(0,3))
# print(tree.minRange(2,6))

class LazySegTree:
    def __init__(self, arr):
        def build(node, start, end):
            if start == end:
                self.nums[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(node*2, start, mid)
                build(node*2+1, mid+1, end)
                self.nums[node] = min(self.nums[node*2], self.nums[node*2+1])

        self.n = len(arr)
        self.nums = [-1 for _ in range(self.n * 4)]
        build(1, 0, self.n - 1)
