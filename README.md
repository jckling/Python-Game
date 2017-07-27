# Python小游戏实验报告
写的比较杂乱，图片路径请自行更改，部分歌曲体积太大就不放上来了，此为备份用<br>
用python写游戏其实感觉怪怪的（毕竟不是专门来写游戏的…）。因为在网上找了些例子参考，虽然没有系统地学习python，但也做了几个小游戏。<br>
功夫主要都花在了“特效”上，敲代码其实还好，反正用到的也就那些。<br>
写了三个小游戏，鼠标射击，卷轴跑酷、弹幕躲避。<br>


## 鼠标射击游戏
* 除了敌机、玩家血条和玩家能量条，其他的都是自己用ps做的图（欣慰）
* 点哪往哪里射击，主要用了数学运算求正切计算旋转角度，因为子弹是自己画的图，贴图的时候用的是左上角，所以有些角度射击时，弹道会有点偏移
* 玩家有三种技能，每次消灭敌机都会积攒能量，每种能量积攒速度不同，随着等级的提高玩家子弹速度变快，敌机下落速度也变快，当然敌机种类也会增加
* 子弹击中敌机和敌机炸毁带了一点点特效，也就是随机位置画图然后再持续一会儿…
* 游戏别名：鼠标性能测试
<br><br>*运行截图*<br><br>
![relation](https://github.com/jckling/Python-Game/blob/master/Report%20Images/1.png)
<br><br>

## 卷轴跑酷游戏
* 看多了会晕乎，大概是背景图太精致(?)
* 只有简单的↑键操作，随着距离的增加速度将会变快，游戏中还可以收集金币（但没什么用处），总觉得挺没意思的…
* 这个游戏比较恶搞，其实本来想叫糖果风躲避金馆长来着的XD
<br><br>*运行截图*<br><br>
![relation](https://github.com/jckling/Python-Game/blob/master/Report%20Images/2.png)
<br><br>

## 弹幕躲避游戏
* 大概一整个下午就写出来了，躲避从窗口四周随机产生的方块
* 方块有不同的速度以及不同的分裂次数，方块的移动和分裂只有四个方向，虽然想写八方向的但四方向已经很难玩了
* 毕竟是一个很好看的游戏，运行着看久了也会入迷的（其实我就是觉得好看才写的）
<br><br>*运行截图*<br><br>
![relation](https://github.com/jckling/Python-Game/blob/master/Report%20Images/3.png)
<br><br>
