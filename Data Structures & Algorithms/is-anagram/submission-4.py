class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def createHash(chars: str) -> dict[str:int]:
            hash_map = {}
            for char in chars:
                hash_map[char] = hash_map.get(char, 0) + 1
            return hash_map

        def compare_hash(hash_1: dict[str:int], hash_2: dict[str:int]) -> bool:
            for key in hash_1:
                if hash_1.get(key) != hash_2.get(key):
                    return False
            return True
        
        s_hash = createHash(s)
        t_hash = createHash(t)
        return compare_hash(s_hash, t_hash)
        
        