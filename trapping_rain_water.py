"""
接雨水 - Trapping Rain Water (LeetCode 42)

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
计算按此排列的柱子，下雨之后能接多少雨水。

示例:
    输入: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
    解释: 数组表示的高度图中，可以接 6 个单位的雨水。
"""

from __future__ import annotations


def _compute_water_level(height: list[int]) -> list[int]:
    """复用：计算每个位置的水位高度（min 左 max, 右 max）"""
    n = len(height)
    if n == 0:
        return []

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    return [min(left_max[i], right_max[i]) - height[i] for i in range(n)]


def trap_brute_force(height: list[int]) -> int:
    """暴力解法 O(n^2) — 对每根柱子找左右最大高度（避免 O(n) 切片）"""
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i + 1])
        right_max = max(height[i:])
        total += min(left_max, right_max) - height[i]
    return total


def trap_brute_force_opt(height: list[int]) -> int:
    """暴力解法优化版 — 增量计算左 max，减少切片开销"""
    n = len(height)
    total = 0
    left_max_sofar = 0
    right_max_all = [0] * n  # 后缀最大值缓存
    cur = 0
    for i in range(n - 1, -1, -1):
        cur = max(cur, height[i])
        right_max_all[i] = cur

    for i in range(n):
        left_max_sofar = max(left_max_sofar, height[i])
        total += min(left_max_sofar, right_max_all[i]) - height[i]
    return total


def trap_dp(height: list[int]) -> int:
    """动态规划 O(n) O(n) — 预处理左右最大高度数组"""
    if not height:
        return 0
    return sum(_compute_water_level(height))


def trap_two_pointer(height: list[int]) -> int:
    """双指针 O(n) O(1) — 最优解法

    用 left / right 两头向中间靠拢，
    哪一端的 max 更小，就移动哪一侧的指针。
    """
    left, right = 0, len(height) - 1
    left_max = right_max = total = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total += right_max - height[right]
            right -= 1
    return total


def trap_monotonic_stack(height: list[int]) -> int:
    """单调栈 O(n) O(n) — 用栈维护递减的高度索引"""
    stack: list[int] = []
    total = 0

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = i - left - 1
            depth = min(height[left], h) - height[top]
            total += width * depth
        stack.append(i)
    return total


# ===== 可视化 =====

def visualize(height: list[int]) -> None:
    """绘制柱状图与雨水分布"""
    if not height:
        print("(空数组)")
        return

    max_h = max(height)
    water_volume = _compute_water_level(height)
    water_level = [height[i] + water_volume[i] for i in range(len(height))]
    n = len(height)

    for level in range(max_h, 0, -1):
        parts: list[str] = []
        for i in range(n):
            if height[i] >= level:
                parts.append(" # ")
            elif water_level[i] >= level:
                parts.append(" ~ ")
            else:
                parts.append("   ")
        parts.append(f"  {level}")
        print("".join(parts))

    print("---" * n)
    print("".join(f"{i:3}" for i in range(n)))
    print(f"\n接水量: {sum(water_volume)}")


# ===== 测试 =====

TEST_CASES: list[tuple[list[int], int]] = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([1, 0, 1], 1),
    ([], 0),
    ([1], 0),
    ([5, 4, 3, 2, 1], 0),
    ([3, 0, 0, 2, 0, 4], 10),
]

METHODS: list[tuple[str, callable]] = [
    ("暴力法", trap_brute_force),
    ("暴力法优化", trap_brute_force_opt),
    ("动态规划", trap_dp),
    ("双指针", trap_two_pointer),
    ("单调栈", trap_monotonic_stack),
]


def test() -> bool:
    """运行所有测试，返回是否全部通过"""
    all_passed = True
    for name, func in METHODS:
        passed = 0
        for heights, expected in TEST_CASES:
            result = func(heights)
            if result == expected:
                passed += 1
            else:
                print(f"  ❌ [{name}] {heights} -> {result} (expected {expected})")
                all_passed = False
        print(f"[{name}] 通过 {passed}/{len(TEST_CASES)}")
    return all_passed


if __name__ == "__main__":
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"输入: {h}")
    print(f"接水量（双指针）: {trap_two_pointer(h)}")
    print()

    print("雨水分布图（#=柱子, ~=雨水）:")
    visualize(h)

    print("\n运行测试:")
    test()
