import scipy.signal as signal
import numpy as np
import pylab as pl


# 滑动平均滤波算法实现
def sliding_average(inputs, per):
    if np.shape(inputs)[0] % per != 0:
        length = np.shape(inputs)[0] / per
        for x in range(int(np.shape(inputs)[0]), int(length + 1) * per):
            inputs = np.append(inputs, inputs[np.shape(inputs)[0] - 1])
    inputs = inputs.reshape((-1, per))
    temp_mean = inputs[0].mean()
    mean = []
    for tmp in inputs:
        mean.append((temp_mean + tmp.mean()) / 2)
        temp_mean = tmp.mean()
    return mean


T = np.arange(0, 0.5, 1 / 4410.0)
# 得到一组随机信号
num = signal.chirp(T, f0=10, t1=0.5, f1=1000.0)
# 利用滑动平均算法滤波
result = sliding_average(num.copy(), 30)

# 绘图对比
pl.subplot(2, 1, 1)
pl.plot(num)
pl.subplot(2, 1, 2)
pl.plot(result, color='red')
pl.show()
