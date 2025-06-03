class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'} 

        for el in s:
            if el in brackets: # It's an open bracket
                stack.append(el)
            else:
                if not stack:
                    return False

                last_el_stack = stack.pop()
                if brackets[last_el_stack] != el:
                    return False
        
        return not stack

# Time Complexity: O(n)
# Space Complexity: O(n) # We store brackets on stack. Worst case, all opening, stack hold up to n elements