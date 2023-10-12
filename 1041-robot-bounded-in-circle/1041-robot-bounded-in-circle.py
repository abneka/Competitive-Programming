class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = (0, 0)
        direction = (0, 1)
        for instruction in instructions:
            if instruction == 'R':
                direction = (direction[1], -direction[0])
                
            elif instruction == 'L':
                direction = (-direction[1], direction[0])
                
            else:
                position = (position[0] + direction[0], position[1] + direction[1])
        
        return position == (0, 0) or direction != (0, 1)