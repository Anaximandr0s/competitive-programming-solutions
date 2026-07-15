class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        new_var = 0
        for operation in operations:
            if operation == "+":
                new_var = ans[-1] + ans[-2]
                ans.append(new_var)
            elif operation == "C":
                ans.pop()
            elif operation == "D":
                new_var = ans[-1] * 2
                ans.append(new_var)
            else:
                ans.append(int(operation))
        return sum(ans)
