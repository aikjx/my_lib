import numpy as np


def f(x):
    return np.sin(x)  # 示例函数，可以替换为任何您需要的函数


def central_diff(f, x, h=1e-5):
    """
    使用中心差分法计算函数 f 在点 x 处的一阶导数。
    
    参数:
    f: 待求导的函数
    x: 求导点的位置
    h: 步长 (默认值 1e-5)
    
    返回:
    导数的近似值
    """
    return (f(x + h) - f(x - h)) / (2 * h)


# 示例：计算 sin(x) 在 x = π/4 处的导数
x_point = np.pi / 4
derivative_approx = central_diff(f, x_point)
true_derivative = np.cos(x_point)  # sin(x) 的导数是 cos(x)


print(f"在 x = {x_point:.3f} 处")
print(f"中心差分近似值: {derivative_approx:.8f}")
print(f"真实导数值: {true_derivative:.8f}")
print(f"绝对误差: {abs(derivative_approx - true_derivative):.8f}")
