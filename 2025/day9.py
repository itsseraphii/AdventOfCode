from utils.aoc_utils import AOCDay

class Day9(AOCDay):
    def common(self):
        self.red = []
        for line in self.inputData:
            result = line.split(',')
            self.red.append((int(result[0]), int(result[1])))
        return 0

    def part1(self):
        maxValue = 0
        for i in range(0, len(self.red)):
            for j in range(i, len(self.red)):
                delta_x = abs(self.red[i][0] - self.red[j][0]) + 1
                delta_y = abs(self.red[i][1] - self.red[j][1]) + 1
                area = delta_x * delta_y
                #print(delta_x, delta_y)
                #print("i ", i, "j ", j, "area ", area)
                if area > maxValue:
                    maxValue = area

        return maxValue

    def part2(self):
        return 0
