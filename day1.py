from typing import List

def compute_calibration(calibration_datas: List[str]) -> int:
	spelled_digit = {"0": "zero", "1":"one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
	total = 0
	for calibration_data in calibration_datas:
		for digit, value in spelled_digit.items():

		value = "0"
		digit_list = [x for x in calibration_data if x.isdigit()]
		if digit_list:
			value = f"{digit_list[0]}{digit_list[-1]}"
		total += int(value)
	return total

if __name__ == '__main__':
	with open("input.txt", "r", encoding="utf-8") as input_datas:
		print(f"Total calibration {compute_calibration(input_datas.readlines())}")
x