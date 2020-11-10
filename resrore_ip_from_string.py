import copy


class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        self.ips = []
        self.ip = []

        def solve(A):
            if len(self.ip) > 4:
                return

            if A == '' and len(self.ip) == 4:
                self.ips.append(copy.copy(self.ip))
                return

            for i in range(1, len(A) + 1):
                if A[0] == '0' and i > 1:
                    return
                else:
                    if int("".join(A[:i])) <= 255:
                        self.ip.append("".join(A[:i]))
                        solve(A[i:])
                        if self.ip:
                            self.ip.pop()

        solve(A)
        return [".".join(ip) for ip in sorted(self.ips)]

s = Solution()
print(s.restoreIpAddresses("0100100"))
