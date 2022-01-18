# def lengthOfLongestSubstring(s: str) -> int:
#     if not len(s):
#         return 0
#     table = dict()
#     max_len = 0
#     for i in range(len(s)):
#         if s[i] not in table:
#             table[s[i]] = i
#         else:
#             max_len = max(max_len, len(table))
#             delete_target = []
#             for key in table:
#                 if table[key] <= table[s[i]]:
#                     delete_target.append(key)
#             print(delete_target)
#             for target in delete_target:
#                 del table[target]
#             table[s[i]] = i
#     max_len = max(max_len, len(table))
#     return max_len
#
# print(lengthOfLongestSubstring('abcdaefgh'))

a = [1, 2, 3, 4]

print(a is )
