# 实验一 Git和Markdown基础

班级： 21计科02

学号： B20210302208

姓名： 何笔男

Github地址：<https://github.com/JingShil/python_course>

---

## 实验目的

1. Git基础，使用Git进行版本控制
2. Markdown基础，使用Markdown进行文档编辑

## 实验环境

1. Git
2. VSCode
3. VSCode插件

## 实验内容和步骤

### 第一部分 实验环境的安装

1. 安装git，从git官网下载后直接点击可以安装：[git官网地址](https://git-scm.com/)
2. 从Github克隆课程的仓库：[课程的仓库地址](https://github.com/zhoujing204/python_course)，运行git bash应用（该应用包含在git安装包内），在命令行输入下面的命令（命令运行成功后，课程仓库会默认存放在Windows的用户文件夹下）

```bash
git clone https://github.com/zhoujing204/python_course.git
```

如果你在使用`git clone`命令时遇到SSL错误，请运行下面的git命令(这里假设你的Git使用了默认安装目录)：

```bash
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

或者运行下面的命令:

```bash
git config --global http.sslVerify false
```

如果遇到错误：`error setting certificate file`，请运行下面的命令重新指定git的安全证书：

```bash
git config --global --unset http.sslCAInfo
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

该仓库的课程材料后续会有更新，如果需要更新课程材料，可以在本地课程仓库的目录下运行下面的命令：

```bash
git pull
```

3. 注册Github账号，创建一个新的仓库，用于存放实验报告和实验代码。
4. 安装VScode，下载地址：[Visual Studio Code](https://code.visualstudio.com/)
5. 安装下列VScode插件
   - GitLens
   - Git Graph
   - Git History
   - Markdown All in One
   - Markdown Preview Enhanced
   - Markdown PDF
   - Auto-Open Markdown Preview
   - Paste Image
   - markdownlint

### 第二部分 Git基础

教材《Python编程从入门到实践》P440附录D：使用Git进行版本控制，按照教材的步骤，完成Git基础的学习。

### 第三部分 learngitbranching.js.org

访问[learngitbranching.js.org](https://learngitbranching.js.org)，如下图所示完成Main部分的Introduction Sequence和Ramping Up两个小节的学习。

![Learngitbranching.js.org](/Experiments/img/2023-07-28-21-07-40.png)

上面你学习到的git命令基本上可以应付百分之九十以上的日常使用，如果你想继续深入学习git，可以：

- 继续学习[learngitbranching.js.org](https://learngitbranching.js.org)后面的几个小节（包括Main和Remote）
- 在日常的开发中使用git来管理你的代码和文档，用得越多，记得越牢
- 在git使用过程中，如果遇到任何问题，例如：错误删除了某个分支、从错误的分支拉取了内容等等，请查询[git-flight-rules](https://github.com/k88hudson/git-flight-rules)

### 第四部分 Markdown基础

查看[Markdown cheat-sheet](http://www.markdownguide.org/cheat-sheet)，学习Markdown的基础语法

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

如何将markdown文件转换为pdf格式的文件？

- 安装vscode插件Markdown PDF，安装后重启vscode，打开markdown文件，按下`Ctrl+Shift+P`，输入`Markdown PDF: Export (pdf)`，回车即可导出pdf文件。
- 使用Google Chrome浏览器，在Github网站或者Gitee网站打开你的仓库，浏览你的markdown文件，按下`Ctrl+P`，选择`打印`，选择`目标打印机`为`另存为PDF`，点击`保存`即可导出pdf文件。

## 实验过程与结果

请将实验过程中编写的代码和运行结果放在这里，注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

命令：从远程仓库拉去代码
```bash
git clone https://github.com/JingShil/python_course
```

显示效果如下：

```bash
Cloning into 'python_course'...
warning: You appear to have cloned an empty repository.
```

命令：查看本地仓库路径

```bash
git rev-parse --show-toplevel
```

显示效果如下：

```bash
D:/python实验报告/实验一/python_course
```

命令：查看远程仓库

```bash
git remote -v
```

显示效果如下：

```bash
origin  https://github.com/JingShil/python_course (fetch)
origin  https://github.com/JingShil/python_course (push)
```

命令：提交到本地仓库

```bash
git commit -m "实验一报告第一次提交"
```

显示效果如下：

```bash
[main (root-commit) cc3bcec] 实验一报告第一次提交
 1 file changed, 158 insertions(+)
 create mode 100644 experiment1.md
```

命令：提交到远程仓库

```bash
git push -u origin main
```

显示效果如下：

```bash
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 2.90 KiB | 1.45 MiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/JingShil/python_course
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'
```



**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

## 实验考查

请使用自己的语言回答下面的问题，这些问题将在实验检查时用于提问和答辩，并要求进行实际的操作。

1. 什么是版本控制？使用Git作为版本控制软件有什么优点？
   
```
   版本控制是一种记录文件内容变化，以便将来查阅特定版本的系统。它可以追踪文件的修改、删除和添加，并且可以在需要时恢复到特定的版本。
```

```
   Git作为版本控制软件具有高效、灵活、安全和强大的分支管理等优点，适用于个人开发和团队协作。
```

2. 如何使用Git撤销还没有Commit的修改？如何使用Git检出（Checkout）已经以前的Commit？（实际操作）
   
```
    撤销对文件的修改：
    git checkout -- <文件名>
```

```
    1.查看所有的commit记录：
    git log

    2.找到要检出的commit的哈希值（commit ID）。

    3.检出指定的commit：
    git checkout <commit ID>
```

3. Git中的HEAD是什么？如何让HEAD处于detached HEAD状态？（实际操作）
   
```
    在Git中，HEAD是一个指向当前所在分支或提交的指针。它可以用来表示当前工作目录中的最新提交。
```

```
    1.查看所有的commit记录：
    git log

    2.找到要进入detached HEAD状态的commit的哈希值（commit ID）。

    3.运行以下命令以进入detached HEAD状态：
    git checkout <commit ID>
```

4. 什么是分支（Branch）？如何创建分支？如何切换分支？（实际操作）

```
    分支（Branch）是Git中用于并行开发和管理代码的重要概念。它可以将代码库分割成不同的线索，每个分支都可以独立进行修改和提交，而不会影响其他分支。
```

```
    创建分支
    git branch <分支名>
```

```
    切换分支
    git checkout <分支名>
```

5. 如何合并分支？git merge和git rebase的区别在哪里？（实际操作）

```
    1.切换到目标分支：
    git checkout <目标分支>

    2.执行合并命令：
    git merge <要合并的分支>
```

6. 如何在Markdown格式的文本中使用标题、数字列表、无序列表和超链接？（实际操作）

在Markdown格式的文本中，可以使用以下语法来添加标题、数字列表、无序列表和超链接：

1. 标题：
   使用`#`符号来表示标题的级别，`#`的数量表示级别的深度。例如：
   ```
   # 一级标题
   ## 二级标题
   ### 三级标题
   ```

2. 数字列表：
   使用数字和`.`来表示有序列表。例如：
   ```
   1. 第一项
   2. 第二项
   3. 第三项
   ```

3. 无序列表：
   使用`-`、`+`或`*`符号来表示无序列表。例如：
   ```
   - 第一项
   - 第二项
   - 第三项
   ```

4. 超链接：
   使用`[链接文本](链接地址)`的格式来添加超链接。例如：
   ```
   [GitHub](https://github.com)
   ```



## 实验总结

        在本次Git实验课中，我学习了Git的基本概念和常用命令，并进行了一些 实际操作。以下是我在实验中的总结和收获：

        Git的基本概念：我了解了Git的基本概念，包括仓库（Repository）、提交（Commit）、分支（Branch）和合并（Merge）等。这些概念对于理解Git的工作原理和使用方法非常重要。

        Git的常用命令：我学习了一些常用的Git命令，包括初始化仓库（git init）、添加文件到暂存区（git add）、提交修改（git commit）、查看提交历史（git log）等。这些命令可以帮助我管理代码的版本和修改。
        创建和切换分支：我学会了如何创建新的分支，并且可以在不同的分支上进行开发和修改。同时，我也学会了如何切换分支，以及如何合并分支的修改。

        通过这次实验，我对Git的使用有了更深入的了解，并且掌握了一些常用的Git命令和操作技巧。我相信这些知识和技能将对我的日常开发工作和团队协作非常有帮助。我会继续学习和探索Git的更多功能和高级用法，以提升我的版本控制和代码管理能力。
