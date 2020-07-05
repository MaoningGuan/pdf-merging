# 合并两个PDF文件
## 一、问题描述：
当前的大部分扫描仪是不支持双面扫描的，因此只能把一个双面的纸质版文件分别进行正面扫描和反面扫描，然后再把扫描后的两个PDF文件进行合并。如下图所示：  

![image_1](https://github.com/MaoningGuan/pdf-merging/blob/master/test1/example1.png)  

其中1800271039-1.pdf是双面的纸质版文件正面扫描后的PDF，1800271039-2.pdf是双面的纸质版文件反面扫描后的PDF，而且1800271039-2.pdf的页面顺序跟原来的纸质版文件的反面的页面顺序是相反的，
因为我们是直接把纸质版文件翻过来扫描，所以页面顺序相反了（如果你是实操过的，应该可以理解）。

## 二、实现方法：
**（1）安装依赖：**
```python
pip install -r requirements.txt
```
> 注意事项：  
Windows用户若是在安装fitz的过程中，提示以下错误：  
**building 'traits.ctraits' extension  
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"**  
可以到:  
[Traits: optional type-checking, data dependencies, and event notifications.
Part of the Enthought Tool Suite.](https://www.lfd.uci.edu/~gohlke/pythonlibs/#traits)  
下载与Python版本对应的.whl文件来安装traits，如对应于windows 64bit和python3.7的.whl文件：**traits‑6.1.0‑cp37‑cp37m‑win_amd64.whl**  
然后使用**pip install traits‑6.1.0‑cp37‑cp37m‑win_amd64.whl**来进行安装。

**（2）使用例子：**
```python
python example1.py
```
**（3）运行结果：**

![image_1](https://github.com/MaoningGuan/pdf-merging/blob/master/test2/example1.png)  

实现过程请查看代码中的注释。
