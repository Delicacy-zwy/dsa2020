# P1270:皮卡丘的冒险

总时间限制: 1000ms 内存限制: 65536kB
## 描述
某天火箭队终于成功抓到了皮卡丘，但是因为主角光环加身，他又双叒叕逃脱了。他想赶紧回到
小智身边，但是前面有一片森林挡住了去路。
用一张地图表示这片森林，其中顶点代表森林的隘口，隘口之间有路相连，皮卡丘想要穿过隘口
就必须打败这里的宝可梦（只用打败一次就可以，第二次再来的时候不用再打），打败宝可梦需
要时间，在路上跑也需要花费时间，假设小智一直在原地等待，皮卡丘想知道他最短需要花费多
长时间才能和小智重逢。

## 输入
输入的第一行为整数N（1≤N≤2000）和整数M（2≤M≤5000），用空格分开，分别代表隘口的数量和路的数量，隘口的编号为2..N+1，编号0和1用来分别代表皮卡丘和小智所在的位置。
输入的第2..N+1行为一个自然数，表示击败该编号对应的隘口的宝可梦需要的时间。
接下来M行，每行三个自然数，用空格分开，代表一条路两端的顶点编号和经过这条路需要的时间。路是双向的。
## 输出
输出一行，即皮卡丘和小智重逢所需的最短时间。测试用例保证皮卡丘和小智一定能再次相逢。
## 样例输入
2 5
1
1
0 2 4
3 0 1
2 3 1
2 1 2
1 3 5
## 样例输出
6