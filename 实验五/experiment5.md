# 实验五 Python数据结构与数据模型

班级： 21 计科 2

学号： B20210302208

姓名： 何笔男

Github 地址：<https://github.com/JingShil/python_course>

CodeWars 地址：<https://www.codewars.com/users/JingShil>

---

## 实验目的

1. 学习Python数据结构的高级用法
2. 学习Python的数据模型

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：停止逆转我的单词

难度： 6kyu

编写一个函数，接收一个或多个单词的字符串，并返回相同的字符串，但所有5个或更多的字母单词都是相反的（就像这个Kata的名字一样）。传入的字符串将只由字母和空格组成。只有当出现一个以上的单词时，才会包括空格。
例如：

```python
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
```

代码提交地址：
<https://www.codewars.com/kata/5264d2b162488dc400000001>

提示：

- 利用str的split方法可以将字符串分为单词列表
例如：

```python
words = "hey fellow warrior".split()
# words should be ['hey', 'fellow', 'warrior']
```

- 利用列表推导将长度大于等于5的单词反转(利用切片word[::-1])
- 最后使用str的join方法连结列表中的单词。

---

#### 第二题： 发现离群的数(Find The Parity Outlier)

难度：6kyu

给你一个包含整数的数组（其长度至少为3，但可能非常大）。该数组要么完全由奇数组成，要么完全由偶数组成，除了一个整数N。请写一个方法，以该数组为参数，返回这个 "离群 "的N。

例如：

```python
[2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
```

代码提交地址：
<https://www.codewars.com/kata/5526fc09a1bbd946250002dc>

---

#### 第三题： 检测Pangram

难度：6kyu

pangram是一个至少包含每个字母一次的句子。例如，"The quick brown fox jumps over the lazy dog "这个句子就是一个pangram，因为它至少使用了一次字母A-Z（大小写不相关）。

给定一个字符串，检测它是否是一个pangram。如果是则返回`True`，如果不是则返回`False`。忽略数字和标点符号。
代码提交地址：
<https://www.codewars.com/kata/545cedaa9943f7fe7b000048>

---

#### 第四题： 数独解决方案验证

难度：6kyu

数独背景

数独是一种在 9x9 网格上进行的游戏。游戏的目标是用 1 到 9 的数字填充网格的所有单元格，以便每一列、每一行和九个 3x3 子网格（也称为块）中的都包含数字 1 到 9。更多信息请访问：<http://en.wikipedia.org/wiki/Sudoku>

编写一个函数接受一个代表数独板的二维数组，如果它是一个有效的解决方案则返回 true，否则返回 false。数独板的单元格也可能包含 0，这将代表空单元格。包含一个或多个零的棋盘被认为是无效的解决方案。棋盘总是 9 x 9 格，每个格只包含 0 到 9 之间的整数。

代码提交地址：
<https://www.codewars.com/kata/63d1bac72de941033dbf87ae>

---

#### 第五题： 疯狂的彩色三角形

难度： 2kyu

一个彩色的三角形是由一排颜色组成的，每一排都是红色、绿色或蓝色。连续的几行，每一行都比上一行少一种颜色，是通过考虑前一行中的两个相接触的颜色而产生的。如果这些颜色是相同的，那么新的一行就使用相同的颜色。如果它们不同，则在新的一行中使用缺失的颜色。这个过程一直持续到最后一行，只有一种颜色被生成。

例如：
```python
Colour here:            G G        B G        R G        B R
Becomes colour here:     G          R          B          G
```


一个更大的三角形例子：

```python
R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
```

你将得到三角形的第一行字符串，你的工作是返回最后的颜色，这将出现在最下面一行的字符串。在上面的例子中，你将得到 "RRGBRGBB"，你应该返回 "G"。
限制条件： 1 <= length(row) <= 10 ** 5
输入的字符串将只包含大写字母'B'、'G'或'R'。

例如：

```python
triangle('B') == 'B'
triangle('GB') == 'R'
triangle('RRR') == 'R'
triangle('RGBG') == 'B'
triangle('RBRGBRB') == 'G'
triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
```

代码提交地址：
<https://www.codewars.com/kata/5a331ea7ee1aae8f24000175>

提示：请参考下面的链接，利用三进制的特点来进行计算。
<https://stackoverflow.com/questions/53585022/three-colors-triangles>

---

### 第二部分

使用Mermaid绘制程序流程图

安装VSCode插件：

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

#### 代码

```python
def spinWords(words):
    word_list = words.split()
    for i in range(len(word_list)):
        if len(word_list[i]) >= 5:
            word_list[i] = word_list[i][::-1]
    return ' '.join(word_list)
```

#### 程序流程图

```mermaid
graph TB
A[spinWords] --> B["words.split()"]
B --> C["for i in range(len(word_list))"]
C --> D["if len(word_list[i]) >= 5"]
D --> E["word_list[i] = word_list[i][::-1]"]
E --> F["' '.join(word_list)"]
F --> G[return]
```

### 题目二

#### 代码

```python
def find_outlier(arr):
    odd_count = 0
    even_count = 0
    odd_num = 0
    even_num = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
            even_num = num
        else:
            odd_count += 1
            odd_num = num
    if odd_count > 1:
        return even_num
    else:
        return odd_num
```


### 题目三

#### 代码

```python
def is_pangram(sentence):
    # 将字符串转换为小写，并去除数字和标点符号
    sentence = ''.join(c.lower() for c in sentence if c.isalpha())
    # 使用set()函数获取唯一字母集合，并检查数量是否等于26
    return len(set(sentence)) == 26
```

### 题目四

#### 代码

```python

def validate_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False
    
    # Check blocks
    for block_row in range(3):
        for block_col in range(3):
            block = [board[row][col] for row in range(block_row*3, block_row*3+3) for col in range(block_col*3, block_col*3+3)]
            if not is_valid_set(block):
                return False
    
    return True

def is_valid_set(nums):
    nums = [num for num in nums if num != 0]
    return len(set(nums)) == len(nums)
```

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. 集合（set）类型有什么特点？它和列表（list）类型有什么区别？
2. 集合（set）类型主要有那些操作？
3. 使用`*`操作符作用到列表上会产生什么效果？为什么不能使用`*`操作符作用到嵌套的列表上？使用简单的代码示例说明。
4. 总结列表,集合，字典的解析（comprehension）的使用方法。使用简单的代码示例说明。


1. 集合（set）类型的特点是无序、不重复的元素集合。与列表（list）类型的区别在于，列表可以包含重复的元素并且有序，而集合不允许重复的元素且无序。

2. 集合（set）类型主要有以下操作：
   - 添加元素：使用`add()`方法向集合中添加元素。
   - 删除元素：使用`remove()`方法删除集合中的元素。
   - 判断元素是否存在：使用`in`关键字判断元素是否存在于集合中。
   - 集合运算：包括并集、交集、差集等操作。

3. 使用`*`操作符作用到列表上会将列表重复指定的次数。但是不能使用`*`操作符作用到嵌套的列表上，因为`*`操作符只能用于可重复的对象，而嵌套的列表是不可重复的对象。下面是一个简单的代码示例：

```python
# 使用*操作符作用到列表上
list1 = [1, 2, 3]
list2 = list1 * 3
print(list2)  # 输出：[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 使用*操作符作用到嵌套的列表上
nested_list1 = [[1, 2], [3, 4]]
nested_list2 = nested_list1 * 3
print(nested_list2)  # 报错：TypeError: can't multiply sequence by non-int of type 'list'
```

4. 列表、集合和字典的解析（comprehension）是一种简洁的创建和操作这些数据结构的方法。

- 列表解析：用于创建新的列表，语法为`[expression for item in iterable if condition]`。下面是一个示例：

```python
# 创建一个包含1到10的平方的列表
squares = [x**2 for x in range(1, 11)]
print(squares)  # 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

- 集合解析：用于创建新的集合，语法为`{expression for item in iterable if condition}`。下面是一个示例：

```python
# 创建一个包含1到10的平方的集合
squares_set = {x**2 for x in range(1, 11)}
print(squares_set)  # 输出：{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
```

- 字典解析：用于创建新的字典，语法为`{key_expression: value_expression for item in iterable if condition}`。下面是一个示例：

```python
# 创建一个包含1到10的平方的字典，键为数字，值为平方
squares_dict = {x: x**2 for x in range(1, 11)}
print(squares_dict)  # 输出：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```
## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。

通过本次实验，我学习到了以下内容：

1. 集合（set）类型是一种无序、不重复的元素集合，与列表（list）类型的区别在于集合不允许重复的元素且无序。
2. 集合类型主要有添加元素、删除元素、判断元素是否存在以及集合运算等操作。
3. 使用`*`操作符作用到列表上会将列表重复指定的次数，但不能作用到嵌套的列表上。
4. 列表、集合和字典的解析（comprehension）是一种简洁的创建和操作这些数据结构的方法，可以根据特定的条件生成新的列表、集合或字典。
