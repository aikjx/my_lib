import numpy as np

# CODATA 2018 G 值
G = 6.67430e-11  # m³·kg⁻¹·s⁻²

# 光速 c 的精确值
c = 299792458  # m·s⁻¹

# 计算 Z
Z = (G * c) / 2

print(f"G = {G:.6e} m³·kg⁻¹·s⁻²")
print(f"c = {c} m·s⁻¹")
print(f"Z = {Z}")


# 假设的 Z 的一部分或原始值
Z_part = 6.67128190396304e-9
# 假设的 c 的换算因子或另一个组成部分
c_factor = 0.0100065

# 根据公式计算 G
G_calculated = (2 * Z_part * c_factor)  # 假设 Z 乘以 c_factor 得到了 Z'
# 或者，如果公式是 G = 2 * Z / c 且 c 是已知值，那么 Z = G * c / 2

# 让我们按照你提供的文字描述来模拟，即 Z * c_factor 得到了一个中间值，然后除以 c 得到 G。
# 但你提供的文字是 G = (6.67128190396304 × 10⁻⁹) × 0.0100065 ≈ 6.67430 × 10⁻¹¹
# 这表示 G 是由 G_part1 * G_part2 得到的，而不是 G = 2Z/c 的形式。
# 看起来公式 (12-3) 可能是描述 G * c / 2 的那个 Z 的计算，或者是一个单位换算的推导。

# 让我们直接模拟你文字描述的 G 的计算：
G_part1 = 6.67128190396304e-9
G_part2 = 0.0100065

G_calculated_from_text = G_part1 * G_part2
print(f"计算得到的 G: {G_calculated_from_text}")

# 目标 G 值 (CODATA 2018)
G_codata_2018 = 6.67430e-11
print(f"CODATA 2018 G 值: {G_codata_2018}")

# 验证是否接近
print(f"近似相等: {abs(G_calculated_from_text - G_codata_2018) < 1e-15}") # 使用一个很小的容差来比较浮点数