from utils.aoc_utils import AOCDay

class Day1(AOCDay):
    # (Direction [-1, 1], value [int])
    def common(self):
        self.moves = []
        for action in self.inputData:
            self.moves.append((1 if action[0] == 'R' else -1, int(action[1:])))
        return 0
    
    def part1(self):
        dailPos = 50
        directZeroes = 0
        for action in self.moves: 
            dailPos += action[1] * action[0]
            if not dailPos % 100:
                directZeroes += 1

        return directZeroes
    

    def part2(self):
        dailPos = 50
        indirectZeroes = 0
        for action in self.moves: 
            # Full turns
            indirectZeroes += action[1]//100

            # Crossed zero
            newPos = dailPos + (action[1] % 100) * action[0]

            if (newPos < 1 and dailPos != 0 or newPos > 99):
                indirectZeroes += 1
            
            dailPos = (100 + newPos) % 100
            #print("Move ", action[1], " to ", dailPos, " tick ", indirectZeroes, "newpos", newPos)

        return indirectZeroes
