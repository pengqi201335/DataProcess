from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

problem = {
  'num_vars': 3,
  'names': ['x1', 'x2', 'x3'],
  'bounds': [[-np.pi, np.pi]]*3
}

# 在给定区间采样
param_values = saltelli.sample(problem, 1000)

# 根据采样计算输出
Y = Ishigami.evaluate(param_values)

# 执行分析
Si = sobol.analyze(problem, Y, print_to_console=True)
