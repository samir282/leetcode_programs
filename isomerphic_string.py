# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         char_dict = {}
#         for schar, tchar in zip(s, t):
#             if schar not in char_dict:
#                 char_dict[schar] = tchar
#             else:
#                 if tchar != char_dict[schar]
#                     return False
#         return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        for schar, tchar in zip(s, t):
            if tchar not in char_dict:
                if schar in char_dict and char_dict[schar] == schar:
                    return False
                char_dict[tchar] = schar
            else:
                if schar != char_dict[tchar]:
                    return False
        return True