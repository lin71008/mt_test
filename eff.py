# Minecraft Eff 
import os

common_unit = {'unit':1, 'rare_stack':16, 'stack':64, 'shulker_box':1728, 'double_box':3456}
def cuu(count, unit=None):
	if unit != None:
		return int(count)*common_unit[str(unit)]
	else:
		return int(count)
def cuu_list(item_list):
	counter = 0
	for item in item_list:
		counter += cuu(item[0], item[1])
	return counter

def mk_item_list(ilist):
	item_list = list()
	for i in range(0,len(ilist),2):
		item_list.append([ilist[i], ilist[i+1]])
	return item_list

ilist = mk_item_list(input("product[num unit] : ").split(' '))
tot_time = [float(i) for i in input("time[h,m,s] : ").split(' ')]
tot_time = 3600*tot_time[0]+60*tot_time[1]+tot_time[2]
if tot_time == 0:
	tot_time = 1
print("total product : {:.4g} items".format(cuu_list(ilist)))
print("total time : {:.4g} s".format(tot_time))
print("rate : {:.4g} / s".format(cuu_list(ilist)/tot_time))