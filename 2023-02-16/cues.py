import yogi as yg
import heapq


def process_command(command: str, data: list[int],
					max_: int, sum_: int, count_: int
					) -> tuple[bool, int, int, int, int]:
	if command == "delete":
		if len(data) != 0:
			ultim = data[0]
			heapq.heappop(data)
			if len(data) != 0:
				return False, data[0], max_, sum_-ultim, count_-1
		return True, 0, 0, 0, 0
	else:
		n = yg.read(int)
		if len(data) == 0:
			max_ = n
		heapq.heappush(data, n)
		max_ = max_ if max_ > n else n
		return False, data[0], max_, sum_+n, count_+1


def main():
	data: list[int] = list()
	max_, sum_, count_ = 0, 0, 0
	for command in yg.tokens(str):
		buida, min_, max_, sum_, count_ = process_command(command, data, max_, sum_, count_)
		if not buida:
			print(f"minimum: {min_}, maximum: {max_}, average: {sum_/count_:.4f}")
		else:
			print("no elements")


if __name__ == "__main__":
	main()
