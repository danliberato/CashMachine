##	A simple ATM program
##	Autor: Daniel Liberato de Jesus
##	Python 3+ is required
import os
import sys

cash_v = [100.00,50.00,20.00,10.00]	#array containing all possible values

def Main():
	while True: #main loop, interrupt with keyboard to exit
		try:
			withdrawal = float(input())
			if withdrawal <= 0:		#check negative values
				msg = "Erro de valor invalido"
			else:
				return_array = []
				while (withdrawal >= min(cash_v)):
					for i in range(len(cash_v)): 
						if withdrawal >= cash_v[i]:
							withdrawal = withdrawal - cash_v[i]
							return_array.append(cash_v[i])
							break
				msg = return_array
				if withdrawal > 0: # check if rest exists
					msg = "Erro de notas indisponíveis"
		except ValueError:
			msg = "Erro de valor nulo"
		print(msg)
		

if __name__ == '__main__': 
	Main() 
