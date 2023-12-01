from typing import List

def compute_calibration(calibration_datas: List[str]) -> int:
	spelled_digit = {"1":"one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
	total = 0
	for calibration_data in calibration_datas:
		value = "0"
		digit_dict = {index:value for index,value in enumerate(calibration_data) if value.isdigit()}
		for digit, value in spelled_digit.items():	
			number_indexes = [i for i in range(len(calibration_data)) if calibration_data.startswith(value,i)]
			for index in number_indexes:
				digit_dict[index] = digit
		if digit_dict:
			sorted_index = sorted(digit_dict)
			value = f"{digit_dict[sorted_index[0]]}{digit_dict[sorted_index[-1]]}"
		total += int(value)
	return total

if __name__ == '__main__':
	with open("input.txt", "r", encoding="utf-8") as input_datas:
		print(f"Total calibration {compute_calibration(input_datas.readlines())}")
