# 合并两个PDF文件
## 一、问题描述：
当前的大部分扫描仪是不支持双面扫描的，因此只能把一个双面的纸质版文件分别进行正面扫描和反面扫描，然后再把扫描后的两个PDF文件进行合并。如下图所示：  

![image_1](https://github.com/MaoningGuan/pdf-merging/blob/master/test1/example1.png)  

其中1800271039-1.pdf是双面的纸质版文件正面扫描后的PDF，1800271039-2.pdf是双面的纸质版文件反面扫描后的PDF，而且1800271039-2.pdf的页面顺序跟原来的纸质版文件的反面的页面顺序是相反的，
因为我们是直接把纸质版文件翻过来扫描，所以页面顺序相反了（如果你是实操过的，应该可以理解）。

## 二、实现方法：
**安装依赖：**
```python
pip install -r requirements.txt
```
**使用例子：**
```python
python example1.py
```
实现过程请查看代码中的注释。
