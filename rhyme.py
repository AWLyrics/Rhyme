from pypinyin import pinyin, FINALS, FINALS_TONE

def n_rhyme(a,b):
	result = 0
	for i in range(len(a)):
		py1 = ''.join(a[i])
		py2 = ''.join(b[i])
		if len(py1) >= 3:
			py1 = py1[-2:]
		if len(py2) >= 3:
			py2 = py2[-2:]
		if py1 == py2:
			result = result + 1
		else:
			break
	return result

def rhyme(a,b):
	# 判断两句话是几押，返回0为不押韵
	# 两句话完全相同也返回0
	if a == b:
		return 0
	# N押 韵母和声调都要相同
	py1_tone = pinyin(a, style=FINALS_TONE)
	py2_tone = pinyin(b, style=FINALS_TONE)
	py1_tone.reverse()
	py2_tone.reverse()
	result = 0
	if len(py1_tone) <= len(py2_tone):
		result = n_rhyme(py1_tone,py2_tone)
	else:
		result = n_rhyme(py2_tone,py1_tone)
	if result > 1:
		return result
	# 单押和双押 韵母相同  声调可以不同
	py1 = pinyin(a, style=FINALS)[-2:]
	py2 = pinyin(b, style=FINALS)[-2:]
	py1.reverse()
	py2.reverse()
	result = 0
	for i in range(len(py1)):
		if py1[i] == py2[i]:
			result = result + 1
		else:
			break
	return result


if __name__ == '__main__':
    print(rhyme('孤独生孤独','泛滥得想吐纵横交错的金属发酥'))
    print(rhyme('孤独生孤独','泛滥得想吐纵横交错的金属负熟'))
    print(rhyme('军火走私犯被拿下武器全部充公','然后它们又被卖给非洲或者是中东'))
    print(rhyme('看着湖南卫视的脑残山寨片','吃着汪涵代言的老坛酸菜面'))
    print(rhyme('孤独生孤独','孤独生孤独'))
    print(rhyme('面对贝爷，你还能做到百般淡定','我看一会去医院没人帮你买单看病'))