import yogi as yg


def mateixa_familia(p1: str, p2: str) -> bool:
	"""Ens indica si els dos parentesis p1 i p2 son de
	la mateixa familia. Assumim que p1 obra, i p2 tanca
	"""
	return p1 == "(" and p2 == ")" or p1 == "[" and p2 == "]"


def es_correcta(paraula: str) -> bool:
	"""Ens indica si la paraula esta ben prentitzada."""
	pila: list[str] = list()
	for parent in paraula:
		if parent == "(" or parent == "[":
			pila.append(parent)
		else:
			if len(pila) == 0:
				return False
			ultim = pila.pop()  # treu i guarda l'ultim element
			if not mateixa_familia(ultim, parent):
				return False
	return len(pila) == 0


def main():
	for paraula in yg.tokens(str):
		if es_correcta(paraula):
			print(paraula, "es correcta")
		else:
			print(paraula, "es incorrecta")


if __name__ == "__main__":
	main()
