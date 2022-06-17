import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--base", type=int)
	parser.add_argument("-e", "--exponent", type=int)
	args = parser.parse_args()

	base = args.base
	exponent = args.exponent

	ret_string = f"{base} to the power of {exponent} is {base ** exponent}"

	print(ret_string)

	with open('ret.txt', 'w') as file:
		file.write(ret_string)

main()