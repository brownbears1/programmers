"""
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

"""


import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if scoville[0] >= K:
            return cnt

        if len(scoville) == 1:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        mixin = first + (second * 2)
        heapq.heappush(scoville, mixin)

        cnt += 1
