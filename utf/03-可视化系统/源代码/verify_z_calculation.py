G = 6.674300e-11  # m³·kg⁻¹·s⁻²
c = 299792458     # m·s⁻¹

# 按照公式 Z = (G * c) / 2 计算Z值
Z_calculated = (G * c) / 2

print(f'根据公式 Z = (G * c) / 2 计算得到的Z值为: {Z_calculated}')
print(f'用户提供的Z值为: 0.010004524012147')
print(f'两者差值为: {abs(Z_calculated - 0.010004524012147)}')