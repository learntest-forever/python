import heapq
from collections import defaultdict

class FlexibleHexMap:
    def __init__(self, min_x, min_y, max_x, max_y):
        """
        初始化自定义坐标范围的六边形地图
        
        参数:
            min_x, min_y: 地图左上角最小坐标
            max_x, max_y: 地图右下角最大坐标
        """
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.grid = {}  # 存储地块数据
        self.special_tiles = set()  # 特殊地块集合
        
        # 验证坐标范围有效性
        if max_x <= min_x or max_y <= min_y:
            raise ValueError("无效的坐标范围")
    
    def is_valid_coord(self, x, y):
        """检查坐标是否在地图范围内"""
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y
    
    def set_tile(self, x, y, terrain='normal', distance=1, properties=None):
        """
        设置单个地块属性
        
        参数:
            x, y: 地块坐标
            terrain: 地形类型
            distance: 移动成本
            properties: 额外属性字典
        """
        if not self.is_valid_coord(x, y):
            raise ValueError(f"坐标 ({x}, {y}) 超出地图范围")
            
        self.grid[(x, y)] = {
            'terrain': terrain,
            'distance': distance,
            'properties': properties or {}
        }
        
        # 如果是特殊地块(高成本)
        if distance >= 999:
            self.special_tiles.add((x, y))
    
    def get_neighbors(self, x, y):
        """获取六边形相邻地块坐标(odd-r偏移)"""
        neighbors = []
        # 奇数行偏移的相邻方向
        directions = [
            (+1,  0), (+1, -1), ( 0, -1),
            (-1,  0), (-1, +1), ( 0, +1)
        ] if y % 2 == 1 else [
            (+1, +1), (+1,  0), ( 0, -1),
            (-1,  0), (-1, -1), ( 0, +1)
        ]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid_coord(nx, ny):
                neighbors.append((nx, ny))
        
        return neighbors
    
    def build_graph(self):
        """构建路径查找用的邻接图"""
        graph = defaultdict(dict)
        
        for (x, y), tile in self.grid.items():
            for nx, ny in self.get_neighbors(x, y):
                if (nx, ny) in self.grid:
                    # 取两个地块中较大的距离值
                    neighbor_tile = self.grid[(nx, ny)]
                    cost = max(tile['distance'], neighbor_tile['distance'])
                    graph[(x, y)][(nx, ny)] = cost
        
        return graph
    
    def find_path(self, start, end):
        """
        使用Dijkstra算法查找最短路径
        
        参数:
            start: 起点坐标 (x, y)
            end: 终点坐标 (x, y)
        
        返回:
            tuple: (总距离, 路径列表) 或 (None, None) 如果不可达
        """
        if not (self.is_valid_coord(*start) and self.is_valid_coord(*end)):
            return None, None
            
        graph = self.build_graph()
        
        # Dijkstra算法实现
        distances = {coord: float('infinity') for coord in graph}
        distances[start] = 0
        previous = {coord: None for coord in graph}
        
        heap = [(0, start)]
        
        while heap:
            current_dist, current_coord = heapq.heappop(heap)
            
            if current_coord == end:
                break
                
            if current_dist > distances[current_coord]:
                continue
                
            for neighbor, weight in graph[current_coord].items():
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_coord
                    heapq.heappush(heap, (distance, neighbor))
        
        # 重建路径
        path = []
        current = end
        
        while previous.get(current) is not None:
            path.append(current)
            current = previous[current]
        
        if path or start == end:
            path.append(start)
            path.reverse()
            return distances[end], path
        else:
            return None, None
    
    def print_map(self, path=None, start=None, end=None):
        """简单文本可视化地图"""
        if path is None:
            path = set()
        else:
            path = set(path)
            
        if start:
            path.add(start)
        if end:
            path.add(end)
        
        for y in range(self.min_y, self.max_y + 1):
            # 奇数行缩进
            print("  " if y % 2 else "", end="")
            
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) == start:
                    print("[S]", end="")
                elif (x, y) == end:
                    print("[E]", end="")
                elif (x, y) in path:
                    print("[*]", end="")
                elif (x, y) in self.special_tiles:
                    print("[X]", end="")
                elif (x, y) in self.grid:
                    print("[ ]", end="")
                else:
                    print("[?]", end="")  # 未定义的地块
            print()

# 示例使用
if __name__ == "__main__":
    # 创建自定义坐标范围的地图 (555-557列, 809-812行)
    hex_map = FlexibleHexMap(555, 809, 557, 812)
    
    # 设置一些地块
    # hex_map.set_tile(100, 100, terrain='normal')  # 普通地块
    # hex_map.set_tile(105, 115, terrain='normal')  # 普通地块
    # hex_map.set_tile(106, 155, terrain='river', distance=999)  # 河流障碍
    # hex_map.set_tile(107, 155, terrain='mountain', distance=999)

    for x in range(555, 557):
        for y in range(809, 813):
            hex_map.set_tile(x, y, terrain='normal')    

    print("地图布局(R=河流/障碍):")
    hex_map.print_map()

    # 批量设置一个区域
    # for x in range(105, 115):
    #     for y in range(105, 115):
    #         hex_map.set_tile(x, y, terrain='forest', distance=2)

    # 设置起点和终点
    start = (555, 809)
    end = (556, 812)
    
    # 查找路径
    distance, path = hex_map.find_path(start, end)
    
    print(f"从 {start} 到 {end} 的路径查找结果:")
    if distance is not None:
        print(f"最短距离: {distance}")
        print(f"路径经过: {path}")
        
        print("\n地图可视化 (S=起点, E=终点, *=路径, X=障碍):")
        hex_map.print_map(path, start, end)
    else:
        print("无法到达目标点")