def dmg(atk, crit_dmg, target_hp):
	if atk*1.2 >= target_hp*0.1:
		zhen_nv = target_hp*0.1
	else:
		zhen_nv = atk*1.2
	dmg_avg = crit_dmg*atk*(0.33*3+0.88) + 0.4*4*zhen_nv
	return dmg_avg

def dmg_others(atk, crit_dmg, target_hp):
	if atk*1.2 >= target_hp*0.1:
		zhen_nv = target_hp*0.1
	else:
		zhen_nv = atk*1.2
	dmg_avg = crit_dmg*atk*(0.33*3) + 0.4*3*zhen_nv
	return dmg_avg

def group_dmg(atk, crit_dmg, targets):
	total_dmg = 0
	total_dmg += dmg(atk, crit_dmg, targets[0])
	for i in range(1, 5):
		total_dmg += dmg_others(atk, crit_dmg, targets[i])
	return total_dmg

def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step

if __name__ == '__main__':
	target = 200000
	targets = [30000, 20000, 200000, 10000, 10000, 200000]
	god_dmg = group_dmg(3082+4614, 2, targets)
	shit_dmg = group_dmg(3082+5145, 1.64, targets)
	print "target_hp", targets
	print "god dmg", god_dmg
	print "shitty dmg", shit_dmg

	flag = 0
	for atk in range(10000):
		if dmg(3082+4614, 2, 1000000) < dmg(atk, 1.64, 1000000):
			print "attack dmg needs to be: ", atk
			flag = 1
			break

		
	if flag == 0:
		print "no solution"

	flag_g = 0
	for atk in range(10000):
		if group_dmg(3082+4614, 2, targets) < group_dmg(atk, 1.64, targets):
			print "for group dmg, attack dmg needs to be: ", atk
			flag_g = 1
			break

		
	if flag_g == 0:
		print "no solution"	

	flag_crit = 0
	for crit in drange(1,2,0.01):
		if group_dmg(3082+4614, 2, targets) < group_dmg(3082+5145, crit, targets):
			print "crit needs to be: ", crit
			flag_crit = 1
			break

		
	if flag_crit == 0:
		print "no solution"
	# flag = 0
	# for target in range(2000000):
	# 	if dmg(3082+4614, 2, target) < dmg(3082+5145, 1.64, target):
	# 		print target
	# 		flag = 1
	# 		break

		
	# if flag == 0:
	# 	print "no solution"