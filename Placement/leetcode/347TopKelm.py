def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    from collections import Counter

    return [i[0] for i in Counter(nums).most_common(k)]
