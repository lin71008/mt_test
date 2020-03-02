"""
計算月票 & 新捷運計費制間的哪個划算

月票: $1280 -> 捷運, 公車 免費
新計費制: $??? -> 捷運看搭乘次數打折, 公車看卡片計費(?)

以下以捷運每次 $40, 公車每次 $15 來計算.
"""
import numpy as np
from matplotlib import pyplot as plt



"""設定搭幾次捷運, 公車"""
ST = 44
BT = 6

# Original Cost
subway_cost = 40.
bus_cost = 15.


# Function Setting
def F0(subway_times, bus_times):
	return (subway_cost * subway_times + bus_cost * bus_times)


# Monthly ticket
def P1280(subway_times, bus_times):
	return 1280. / F0(subway_times, bus_times)


# New System
def pre_F75(times):
	if times > 50:
		return .7
	elif times > 10:
		return .95 - .05 * ((times - 1) // 10)
	else:
		return 1.


def F75(subway_times, bus_times):
	return (pre_F75(subway_times) * subway_cost * subway_times + bus_cost * bus_times)


def F75_subway(subway_times, bus_times):
	Re = []
	for t in subway_times:
		Re.append(pre_F75(t) * subway_cost * t + bus_cost * bus_times)
	return np.array(Re)


def P75(subway_times, bus_times):
	return F75(subway_times, bus_times) / F0(subway_times, bus_times)


def P75_subway(subway_times, bus_times):
	return F75_subway(subway_times, bus_times) / F0(subway_times, bus_times)


# Analysis
Original = F0(ST, BT)
Old_Sys = P1280(ST, BT)
New_SysCost = F75(ST, BT)
New_Sys = P75(ST, BT)
print(f'原價 => {Original}')
print(f'舊制度 => 1280, {Old_Sys*100:.2f}%')
print(f'新制度 => {New_SysCost}, {New_Sys*100:.2f}%')
if New_Sys > Old_Sys: print('=> 用舊制度')
else: print('=> 用新制度')


# Graph
T = np.arange(65)
O = F0(T, ST)
Old_Sys = P1280(T, BT)*100
New_Sys = np.array(P75_subway(T, BT))*100
plt.title(f'搭{BT}次公車時的總累進折扣')
plt.xlabel('搭捷運次數')
plt.ylabel('折扣 [100%]')
plt.ylim(70, 120)
plt.plot(T, O, 'w-', label='Original')
plt.plot(T, Old_Sys, 'b-', label='Old_Sys')
plt.plot(T, New_Sys, 'g-', label='New_Sys')
plt.legend()
plt.show()