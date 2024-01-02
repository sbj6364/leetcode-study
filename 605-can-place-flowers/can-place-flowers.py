class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_string = list(map(str, flowerbed))
        word = '0' + ''.join(flowerbed_string) + '0'
        empties = list(filter(bool, word.split('1')))

        lst = []
        
        if empties == None:
            maxlen = 0
        else:
            for i in range(len(empties)):
                lst.append((len(empties[i])-1)//2)
            maxlen = sum(lst)

        result = maxlen >= n

        return result
        