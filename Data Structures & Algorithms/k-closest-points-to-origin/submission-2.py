class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer = points[:k]
        maxdist = self.findmax(answer, k)
        
        for i in range(k, len(points)):
            temp = self.euc(points[i])
            if maxdist[1] > temp:
                answer[maxdist[0]] = points[i]
                maxdist = self.findmax(answer, k)
        
        return answer

    def findmax(self, arr, k):
        maxdist = [0, -1]
        for i in range(k):
            temp = self.euc(arr[i])
            if temp > maxdist[1]:
                maxdist[0] = i
                maxdist[1] = temp
        return maxdist

    def euc(self, pair):
        x, y = pair
        return (x**2 + y**2)**(1/2)
