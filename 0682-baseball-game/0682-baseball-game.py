class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        new_var = 0
        for operation in operations:
            if operation == "+":
                new_var = int(ans[-1]) + int(ans[-2])
                ans.append(new_var)
            elif operation == "C":
                ans.pop()
            elif operation == "D":
                new_var = int(ans[-1]) * 2
                ans.append(new_var)
            else:
                ans.append(operation)
        return sum(map(int, ans))
