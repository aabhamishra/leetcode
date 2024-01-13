class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = []
        times = []

        for i in range(len(position)):
            data.append([position[i], speed[i]])
        
        data = sorted(data, key=lambda x: x[0], reverse = True)

        for p, s in data:
            time = (target-p) / s
            
            if not times or times[-1] < time:
                times.append(time)
        
        return len(times)