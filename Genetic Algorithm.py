from numpy.random import randint
from numpy.random import rand

s_iter = 100
gen_sayisi = 20
pop_sayisi = 20
cross_orani = 0.9
mut_orani = 0.05
eror = 0

def onemax(x):
	return -sum(x)

def secim(pop, toplam, k=3):
	secim_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		if toplam[ix] < toplam[secim_ix]:
			secim_ix = ix
	return pop[secim_ix]

def crossover(p1, p2, cross_orani):
	c1, c2 = p1.copy(), p2.copy()
	if rand() < cross_orani:
		pt = randint(1, len(p1)-2)
		c1 = p1[:pt] + p2[pt:]
		c2 = p1[pt:] + p2[:pt]
	return [c1, c2]

def mutasyon(degisken, mut_orani):
	for i in range(len(degisken)):
		if rand() < mut_orani:
			degisken[i] = 1 - degisken[i]

def genetic_algorithm(objective, gen_sayisi, s_iter, pop_sayisi, cross_orani, mut_orani, eror):
	pop = [randint(0, 2, gen_sayisi).tolist() for _ in range(pop_sayisi)]
	enb, enb1 = 0, objective(pop[0])
	for gen in range(s_iter):
		toplam = [objective(c) for c in pop]
		for i in range(pop_sayisi):
			eror = eror + toplam[i]
			if toplam[i] < enb1:    
				enb, enb1 = pop[i], toplam[i]
			print((gen,  pop[i], toplam[i], eror))	
		print(" ")

		secim1 = [secim(pop, toplam) for _ in range(pop_sayisi)]
		yeni_nesil = list()
		for i in range(0, pop_sayisi, 2):
			p1, p2 = secim1[i], secim1[i+1]
			for c in crossover(p1, p2, cross_orani):
				if (c == 0):
					mutasyon(c, mut_orani)
				yeni_nesil.append(c)
			pop = yeni_nesil

		if (eror == -400):
			break

		if (eror != -400):
			eror = 0
			
	return [enb, enb1]

enb, score = genetic_algorithm(onemax, gen_sayisi, s_iter, pop_sayisi, cross_orani, mut_orani, eror)

