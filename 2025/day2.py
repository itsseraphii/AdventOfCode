from utils.aoc_utils import AOCDay

class Day2(AOCDay):
    def common(self):
        self.ranges = self.inputData[0].split(',')
        return 0

    def part1(self):
        total = 0
        for nums in self.ranges:
            low = int(nums.split('-')[0])
            high = int(nums.split('-')[1])
            for num in range(low, high+1):

                if self.repeatedTwice(num):
                    total += num
        
        return total
    
    def repeatedTwice(self, num):
        val = str(num)
        if not len(val) % 2:
            maxSeqLen = len(val) // 2
            #print(val[maxSeqLen:], ' vs ', val[:maxSeqLen])
            if val[maxSeqLen:] == val[:maxSeqLen]:
                return 1

        return 0
    
    def repeatedAtLeastTwice(self, num):
        val = str(num)
        maxSeqLen = len(val) // 2

        if maxSeqLen == len(val):
            maxSeqLen = 1
        
        for i in range(1, maxSeqLen+1):
            if len(list(set(val.split(val[:i])))) == 1:
                #print("HIT", val, ':', val[:i], ' vs ', val.split(val[:i]))
                return 1
            else:
                #print(val, ':', val[:i], ' vs ', val.split(val[:i]))
                continue

        return 0
    
    def part2(self):
        total = 0
        for nums in self.ranges:
            low = int(nums.split('-')[0])
            high = int(nums.split('-')[1])
            for num in range(low, high+1):
                if self.repeatedAtLeastTwice(num):
                    total += num
        
        return total
