class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        queue = deque(["0000"])
        visited = set(["0000"])
        count = 0

        while queue:

            size = len(queue)
            for _ in range(size):

                combo = queue.popleft()
                if combo == target:
                    return count

                for wheel in range(8):
                    if wheel < 4:
                        next_combo = combo[:wheel] + str((int(combo[wheel]) + 1)%10) + combo[wheel+1:]
                    else:
                        next_combo = combo[:wheel-4] + str((int(combo[wheel-4]) - 1)%10) + combo[(wheel+1)-4:]

                    if next_combo not in deadends and next_combo not in visited:
                        queue.append(next_combo)
                        visited.add(next_combo)

            count += 1

        return -1