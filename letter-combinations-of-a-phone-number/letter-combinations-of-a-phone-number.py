class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_chat = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k", "l"],
            "6": ["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9": ["w","x","y","z"]
        }
        res = []
        def backtrack(i, stack):
            if i == len(digits):
                if stack:
                    res.append("".join(stack[:]))
                return 
            
            for c in digit_to_chat[digits[i]]:
                stack.append(c)
                backtrack(i + 1, stack)
                stack.pop()
        backtrack(0,[])
        return res