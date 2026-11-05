class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        encoded_str = ''
        for str in strs:
            sizes.append(len(str))

        for size in sizes:
            encoded_str = f'{encoded_str}{size}#'

        encoded_str = encoded_str + '|'

        for str in strs:
            encoded_str = encoded_str + str

        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == '|':
            return []
        sizes = s[:s.find('|') - 1].split('#')
        s = s[s.find('|') + 1:]
        strs = []
        
        for size in sizes:
            size = int(size)
            strs.append(s[:size])
            s = s[size::]

        return strs