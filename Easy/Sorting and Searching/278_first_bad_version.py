# First Bad Version

#  You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version,
# all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def rec_func(left, right):
            middle = int((left + right) / 2)
            if left == right:
                return left
            if isBadVersion(middle):
                right = middle
            else:
                left = middle+1
            return rec_func(left, right)

        left, right = 0, n
        index = rec_func(left, right)
        return index + int(not isBadVersion(index))
