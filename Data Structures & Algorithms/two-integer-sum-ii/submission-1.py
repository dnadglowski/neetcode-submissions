class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []

        for x in range(len(numbers)):
            need = target - numbers[x]
            if need in numbers[x+1:]:
                answer.append(x + 1)
                answer.append(numbers.index(need, x+1) + 1)
                break

        return answer