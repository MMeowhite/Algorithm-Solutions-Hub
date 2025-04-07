def counting_sundays(start_year, end_year):
	"""
	You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
	"""
	# total days of each month in non-leap months
	days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	current_day = 0 # 0->Monday, 1->tuesday, 2->wensday,... ,6->sundays
	sundays_count = 0

	for year in range(start_year, end_year+1):
		for month in range(12):
			if month == 1 and is_leap_year(year):
				days = 29
			else:
		 		days = days_in_month[month]

			# update current day
			current_day = (current_day + days) % 7

			# 如果是 1901 年到 2000 年之间的日期，并且当前月的第一天是星期日，计数加 1
			if year >= 1901 and current_day == 6:  # 6 表示星期日
				sundays_count += 1

	return sundays_count

def is_leap_year(year):
	# determine the year is leap or not
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	return year % 4 == 0

if __name__ == "__main__":
	print(counting_sundays(1900, 2000))
