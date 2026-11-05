class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        print(s)
        i, j = 0, 0
        res = []
        while i < len(s):
            if s[j] == '#':
                size = int(s[i:j])
                j = j + 1
                s_1 = s[j:size + j]
                print(s_1)
                res.append(s_1)
                j = j + size
                i = j
            j = j + 1

        return res