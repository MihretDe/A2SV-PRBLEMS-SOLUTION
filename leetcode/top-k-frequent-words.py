class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        l1 = []
        d1 = defaultdict(list)
        for key , v in count.items():
            d1[v] .append(key)
        l1 = []
        for key , v in d1.items():
            so = sorted(v)
            l1.append([key , so])
        
        l1 . sort(reverse = True)
        print(l1)
        answer = []
        for i in range(len(l1)):
            n = len(l1[i][1])
            j = 0
            while k and j<n:
                answer.append(l1[i][1][j])
                j +=1
                k -= 1
        return answer
                

        