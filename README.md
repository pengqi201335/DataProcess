几种数据处理方法的python实现
=================
1.滑动平均滤波算法
-------------
#### __第三方依赖库__
    numpy
    scipy
    matplotlib
2.主成分分析算法
------------
#### __第三方依赖库__
    numpy
    pandas
    matplotlib
3.灵敏度分析--Sobol算法
------------------
#### __第三方依赖库__
    numpy
    SALib   conda install -c conda-forge salib
#### __分析对象__
    y = sin(x1) + 7(sinx2)^2 + 0.1(sin(x1))(x3)^4
#### __计算结果__
##### __(s2>s1>s3，参数敏感性依次递减)__
    s1 = 0.3139
    s2 = 0.4424
    s3 = 0.0
