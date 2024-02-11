class Solution:
    def get_neigbours(self, p, n):
        moves = [(0, 1), (1, 0)]
        neigbours = []
        for move in moves:
            neigbour = tuple(p[i] + move[i] for i in range(2))
            if max(neigbour) < n and min(neigbour) >= 0:
                neigbours.append(neigbour)
        return neigbours

    def numberOfPath(self, n, k, arr):
        count = 0
        stack = [[[arr[0][0]], (0, 0)]]
        while stack:
            current_node = stack.pop()
            neigbours = self.get_neigbours(current_node[1], n)
            for neigbour in neigbours:
                new_node = [[*current_node[0], arr[neigbour[0]][neigbour[1]]], neigbour]
                if sum(new_node[0]) < k:
                    stack.append(new_node)
                elif sum(new_node[0]) == k and neigbour[0] == neigbour[1] == n - 1:
                    count += 1
        return count


solution = Solution()
## Example set 1
k = 12
n = 3
arr = [[1, 2, 3], [4, 6, 5], [3, 2, 1]]
assert solution.numberOfPath(n, k, arr) == 2
## Example set 2
k = 16
n = 3
arr = [[1, 2, 3], [4, 6, 5], [9, 8, 7]]
assert solution.numberOfPath(n, k, arr) == 0
