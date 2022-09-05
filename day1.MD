# 第一天作业
## 吕澎

### 笔记
branch dev创建
checkout dev/master
merge dev合并
cat filename
ssh -T git@giyhub.com
git config --global user.name "Your Name"账号
git config --global user.email "email@example.com"
cd打开
1.pull
2.vim filename
3.add .
4.commit
5.push(交作业

### 心得
没有及时问，想自己看教程结果看到奇怪的地方，有点浪费精力，如果纯粹git只是工具把代码背下来就好了。有点浪费时间，好困，对不起。



<<<<<<< HEAD
<<<<<<< HEAD
##王乐怡 

### 笔记
HTML:
<!DOCTYPE html> 声明为 HTML5 文档
<html></html> 元素是 HTML 页面的根元素
<head></head> 元素包含了文档的元数据
<title></title> 元素描述了文档的标题
<body></body> 元素包含了可见的页面内容
<h1></h1> 元素定义一个大标题
<p></p> 元素定义一个段落
使用时嵌套的,元素尽量使用小写

HTML 标题是通过<h1>(</h1>) - <h6>(</h6>) 标签来定义的
HTML 段落是通过标签 <p> 来定义的
HTML 链接是通过标签 <a> 来定义的
HTML 图像是通过标签 <img> 来定义的

HTML 元素以开始标签起始,以结束标签终止,e.g.<p>XXXXX</p>,成对，斜杠在结束的的前面，元素的内容是开始标签与结束标签之间的内容（XXXXX）
不过，某些 HTML 元素具有空内容，空元素在开始标签中进行关闭（以开始标签的结束而结束），e.g.<br />自带斜杠，在后面

Git:
git init
master//主分支
git branch
git checkout//切换分支
git merge//迁移
git commit -m XXX//备注
git add .//提交一个版本
git clone
git pull
git push
ssh -T git@github.com
dd//删整行
esc-->:-->wq//保存并退出    q//退出
cd ..//删除库
re -rf //换文件夹
合并冲突
    git pull
    vim README.MD
    git add .
    git commit -m XXX
    git push


=======
## 方芬琦

### 笔记
=======
## 方芬琦

### 笔记
>>>>>>> 3e82a67f14181b6505078f1405e069728aefa311
- 在本地情况下，master是主分支，还有dev分支
- git branch
- git checkout dev
- git commit
- 合并冲突：git pull;git add .;git commit -m hiahiahia;git push
- 如何退出修改页面：esc;wq
- 如何修改：i可移动i；按esc,再按dd可删除
- 如何push:git pull;vim (文件）.MD;git add .;git commit -m 随便打打；git push
- 如果无法push，则需重新pull
<<<<<<< HEAD
>>>>>>> 3e82a67f14181b6505078f1405e069728aefa311

### 心得
-今天是军训第一天，除了训练之外，还学了git,虽然有点难，一开始没跟上，不过还是学会了，开心！希望剩下十五天好好训练，认真向师兄师姐学习，学到更多知识，好好跟搭档合作，早点能干活天

<<<<<<< HEAD
今天教学了GIT,
虽然一开始没跟上，但在教练的耐心教导下，逐渐上手，收获颇丰，学会了很多知识，仍有不太熟练的地方，但在之后的不断训练下，一定会越来越好！
=======
----------------
## 陈思铭
### 笔记
	1.html
		<!DOCTYPE html>  <html></html> <body></body><img scr="图片目录"  alt="图片名" width="宽度" height="高度">
		css<style =
	2.git
		mkdir +文件名 创建文件夹
		ls            看列表
		pwd        看目录
		cd ..		返回上级
		git add .  添加修改
		git commit -m '信息'   提交修改
		git pull 拉取 
		git push 提交
		vim +文件  打开文件
		esc + wq 保存并退出
		git branch 分支 
		git checkout 切换分支 
### 心得 
	1.要记笔记，特别是学长讲重点的时候	2.不懂多问

## 陈宇翔

### 笔记
- 1. html : 有终止的例 <html> 后接 </html> 自终止的 <br/>
- 2. git： 1. mkdir 创建文件夹 vim 创建或打开文件
           2. ls 查看列表 pwd查看目录 cd . 进入下一级 cd .. 进入上一级
           3. git add . 将当前目录下修改的所有代码从工作区添加到暂存区 . 代表当前目录
              git status 查看工作区代码相对于暂存区的差别
              git commit -m ‘注释’ 将缓存区内容添加到本地仓库
### 心得
- 好难 我已经寄了


----------------------
## 王凯韬

### 笔记
- git branch dev #新建分支
- git checkout dev#跳转分支
- git commit -m 'first'
- git merge dev 合并
- vim 文件名#更改
- cat 文件名#显示
- git add.#保存更改
- git clone git@github.com 加仓库地址

ssh -T git@github.com

vim界面内
I 进入操作界面
esc :wq 退出操作界面

第二点：
对flex布局有初步了解

###心得
学会了gitbase的基本用法，半只脚踏入了编程的大门，HTML和CSS的操作也通过青蛙游戏有了部分了解，开始逐渐上手。


## 刘一凡

### 笔记

#### Git
Git是一个分布式版本管理工具

git init 初始化

git add 添加到暂存区

git commit 提交到仓库

git branch 创建分支

git chechout 切换分支

git merge 合并分支

git clone 克隆仓库

git pull 拉取仓库

git push 推送仓库

git log git日志

#### html
html是一个标记语言

html 根元素

head 文件头

title 标题

body 页面内容

h1 大标题

p 段落

如果浏览器不支持js，那么注释中的脚本就会当成注释的一部分不会执行，反之则可以执行。

### 心得
平静的一天，基本上都是一些背诵内容。

=======

### 心得
-今天是军训第一天，除了训练之外，还学了git,虽然有点难，一开始没跟上，不过还是学会了，开心！希望剩下十五天好好训练，认真向师兄师姐学习，学到更多知识，好好跟搭档合作，早点能干活天

----------------
## 陈思铭
### 笔记
	1.html
		<!DOCTYPE html>  <html></html> <body></body><img scr="图片目录"  alt="图片名" width="宽度" height="高度">
		css<style =
	2.git
		mkdir +文件名 创建文件夹
		ls            看列表
		pwd        看目录
		cd ..		返回上级
		git add .  添加修改
		git commit -m '信息'   提交修改
		git pull 拉取 
		git push 提交
		vim +文件  打开文件
		esc + wq 保存并退出
		git branch 分支 
		git checkout 切换分支 
### 心得 
	1.要记笔记，特别是学长讲重点的时候	2.不懂多问
>>>>>>> 3e82a67f14181b6505078f1405e069728aefa311

## 陈宇翔

### 笔记
- 1. html : 有终止的例 <html> 后接 </html> 自终止的 <br/>
- 2. git： 1. mkdir 创建文件夹 vim 创建或打开文件
           2. ls 查看列表 pwd查看目录 cd . 进入下一级 cd .. 进入上一级
           3. git add . 将当前目录下修改的所有代码从工作区添加到暂存区 . 代表当前目录
              git status 查看工作区代码相对于暂存区的差别
              git commit -m ‘注释’ 将缓存区内容添加到本地仓库
### 心得
- 好难 我已经寄了


----------------------
## 王凯韬

### 笔记
- git branch dev #新建分支
- git checkout dev#跳转分支
- git commit -m 'first'
- git merge dev 合并
- vim 文件名#更改
- cat 文件名#显示
- git add.#保存更改
- git clone git@github.com 加仓库地址

ssh -T git@github.com

vim界面内
I 进入操作界面
esc :wq 退出操作界面

第二点：
对flex布局有初步了解

###心得
学会了gitbase的基本用法，半只脚踏入了编程的大门，HTML和CSS的操作也通过青蛙游戏有了部分了解，开始逐渐上手。


## 刘一凡

### 笔记

#### Git
Git是一个分布式版本管理工具

git init 初始化

git add 添加到暂存区

git commit 提交到仓库

git branch 创建分支

git chechout 切换分支

git merge 合并分支

git clone 克隆仓库

git pull 拉取仓库

git push 推送仓库

git log git日志

#### html
html是一个标记语言

html 根元素

head 文件头

title 标题

body 页面内容

h1 大标题

p 段落

如果浏览器不支持js，那么注释中的脚本就会当成注释的一部分不会执行，反之则可以执行。

### 心得
平静的一天，基本上都是一些背诵内容。
