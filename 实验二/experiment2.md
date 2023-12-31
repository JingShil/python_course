# 实验二 Python变量、简单数据类型

班级： 21计科2班

学号： B20210302208

姓名： 何笔男

Github地址：<https://github.com/JingShil/python_course>

CodeWars地址：<https://www.codewars.com/users/JingShil>

---

## 实验目的

1. 使用VSCode编写和运行Python程序
2. 学习Python变量和简单数据类型

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

实验环境的安装

1. 安装Python，从Python官网下载Python 3.10安装包，下载后直接点击可以安装：[Python官网地址](https://www.python.org/downloads/)
2. 为了在VSCode集成环境下编写和运行Python程序，安装下列VScode插件
   - Python
   - Python Environment Manager
   - Python Indent
   - Python Extended
   - Python Docstring Generator
   - Jupyter
   - indent-rainbow
   - Jinja

---

### 第二部分

Python变量、简单数据类型和列表简介

完成教材《Python编程从入门到实践》下列章节的练习：

- 第2章 变量和简单数据类型

---

### 第三部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第1题：求离整数n最近的平方数（Find Nearest square number）

难度：8kyu

你的任务是找到一个正整数n的最近的平方数
例如，如果n=111，那么nearest_sq(n)（nearestSq(n)）等于121，因为111比100（10的平方）更接近121（11的平方）。
如果n已经是完全平方（例如n=144，n=81，等等），你需要直接返回n。
代码提交地址
<https://www.codewars.com/kata/5a805d8cafa10f8b930005ba>

---

#### 第2题：弹跳的球（Bouncing Balls）

难度：6kyu

一个孩子在一栋高楼的第N层玩球。这层楼离地面的高度h是已知的。他把球从窗口扔出去。球弹了起来,  例如:弹到其高度的三分之二（弹力为0.66）。他的母亲从离地面w米的窗户向外看,母亲会看到球在她的窗前经过多少次（包括球下落和反弹的时候）？

一个有效的实验必须满足三个条件：

- 参数 "h"（米）必须大于0
- 参数 "bounce "必须大于0且小于1
- 参数 “window "必须小于h。

如果以上三个条件都满足，返回一个正整数，否则返回-1。
**注意:只有当反弹球的高度严格大于窗口参数时，才能看到球。**
代码提交地址
<https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python>

---

#### 第3题： 元音统计(Vowel Count)

难度： 7kyu

返回给定字符串中元音的数量（计数）。对于这个Kata，我们将考虑a、e、i、o、u作为元音（但不包括y）。输入的字符串将只由小写字母和/或空格组成。

代码提交地址：
<https://www.codewars.com/kata/54ff3102c1bad923760001f3>

---

#### 第4题：偶数或者奇数（Even or Odd）

难度：8kyu

创建一个函数接收一个整数作为参数，当整数为偶数时返回”Even”当整数位奇数时返回”Odd”。
代码提交地址：
<https://www.codewars.com/kata/53da3dbb4a5168369a0000fe>

### 第四部分

使用Mermaid绘制程序流程图

安装Mermaid的VSCode插件：

- Markdown Preview Mermaid Support
- Mermaid Markdown Syntax Highlighting

使用Markdown语法绘制你的程序绘制程序流程图（至少一个），Markdown代码如下：

![程序流程图](/Experiments/img/2023-08-05-22-00-00.png)

显示效果如下：

```mermaid
flowchart LR
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```

查看Mermaid流程图语法-->[点击这里](https://mermaid.js.org/syntax/flowchart.html)

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果

### 题目一

代码
```python
import math

def nearest_sq(n):
    sqrt_n = int(math.sqrt(n))  
    if sqrt_n * sqrt_n == n: 
        return n
    else:
        lower_sq = sqrt_n * sqrt_n  
        upper_sq = (sqrt_n + 1) * (sqrt_n + 1)  
        if n - lower_sq < upper_sq - n:  
            return lower_sq
        else:
            return upper_sq
```

程序流程图

```mermaid
flowchart TB
    A[start] --> B["sqrt_n = int(math.sqrt(n)) "]
    B --> C{Is sqrt_n * sqrt_n == n}
    C --> |Yes| D[return n]
    D --> E[end]
    C --> |No| F[lower_sq = sqrt_n * sqrt_n]
    F --> G["upper_sq = (sqrt_n + 1) * (sqrt_n + 1)"]
    G --> H{Is n - lower_sq < upper_sq - n}
    H --> |Yes| I[return lower_sq]
    I --> E
    H --> |No| J[return upper_sq]
    J --> E

```


### 题目二

代码
```python
def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    if not 0 < window < h: return -1
    count = 1
    while h * bounce > window:
        h *= bounce
        count += 2
    return count
```

程序流程图

```mermaid
flowchart TB
    A[Start] --> B{"Is not 0 < bounce < 1: return -1"}
    B --> |Yes| C{"not 0 < window < h: return -1"}
    C --> |Yes| D[count = 1]
    B --> |No| E{"h * bounce > window"}
    C --> |No| E
    D --> E
    E --> |Yes| F[h *= bounce count += 2]
    F --> E
    E --> |No| G[return count]
    G --> H[end]
```

### 题目三

代码
```python
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiou":
            num_vowels += 1
    return num_vowels
```

程序流程图

```mermaid
flowchart TB
    A[Start] --> B[num_vowels = 0]
    B --> C{"num >= inputStr && char = inputStr[num]"}
    C --> |Yes| D{"char in 'aeiou'"}
    D --> |Yes| F[num_vowels += 1]
    D --> |No| C
    F --> C
    C --> |No| G[return num_vowels]
    G --> H[end]
```

### 题目四

代码
```python
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

程序流程图

```mermaid
flowchart TB
    A[Start] --> B{Is number % 2 == 0}
    B --> |Yes| C["return 'Even'"]
    B --> |No| D[return 'Odd']
    C --> E[end]
    D --> E[end]
```

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

##### 1. Python中的简单数据类型有那些？我们可以对这些数据类型做哪些操作？

Python中的简单数据类型包括整数（int）、浮点数（float）、布尔值（bool）、字符串（str）和空值（None）。我们可以对这些数据类型进行各种操作，例如数学运算、逻辑运算、字符串拼接等。

##### 2. 为什么说Python中的变量都是标签？

在Python中，变量被称为标签，是因为变量实际上是指向内存中对象的引用。当我们给变量赋值时，实际上是将变量标签指向了一个对象。这意味着变量可以随时指向不同的对象，而不需要事先声明类型。

##### 3. 有哪些方法可以提高Python代码的可读性？

有几种方法可以提高Python代码的可读性。首先是使用有意义的变量名和函数名，以便于理解代码的含义。其次是使用注释来解释代码的逻辑和目的。另外，适当的缩进和空行可以使代码结构清晰易读。还可以使用空格和换行符来分隔代码块，使代码更易于阅读。最后，遵循PEP 8编码规范可以提高代码的一致性和可读性。

## 实验总结

在这次实验中，我学习和使用了以下知识：

1. 编程工具的使用：我使用了Python作为编程语言，并使用了vscode来编写和运行代码。

2. 数据结构：我学习了Python中的简单数据类型，包括整数、浮点数、布尔值、字符串和空值。我了解了这些数据类型的特点和用法。

3. 程序语言的语法：我学习了Python的基本语法，包括变量的声明和赋值、条件语句、循环语句、函数的定义和调用等。

4. 算法：虽然这次实验没有涉及复杂的算法，但我学习了一些基本的算法思想，例如数学运算和逻辑运算。

5. 编程技巧：我学习了一些提高代码可读性和可维护性的编程技巧，例如使用有意义的变量名和函数名、添加注释、适当的缩进和空行等。

6. 编程思想：我学习了一些基本的编程思想，例如模块化思维、代码复用和抽象化等。这些思想可以帮助我更好地组织和管理代码。
