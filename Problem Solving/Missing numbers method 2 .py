Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import defaultdict
... 
... class MissingNumbers:
...     def missingNumbers(self, arr, brr):
...         integerFreqMap = defaultdict(int)
...         
...         for i in brr:
...             freq = integerFreqMap[i]
...             freq += 1
...             integerFreqMap[i] = freq
...         
...         for i in arr:
...             freq = integerFreqMap[i]
...             freq -= 1
...             if freq == 0:
...                 del integerFreqMap[i]
...             else:
...                 integerFreqMap[i] = freq
...         
...         result = list(integerFreqMap.keys())
...         return result
