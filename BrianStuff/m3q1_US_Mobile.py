import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

average_mobile_download_speeds_before_2018 = np.array([5.1, 4.0, 5.5, 2.8, 1.6, 1.3, 0.9])
average_mobile_peak_download_speeds_before_2018 = np.array([19.8, 17.8, 15.1, 15.1, 5.3, 3.8, 2.2])

# find the linear trend between average download and average peak download speeds for when they are available
plt.plot(average_mobile_download_speeds_before_2018, average_mobile_peak_download_speeds_before_2018, 'o')
m, b = np.polyfit(average_mobile_download_speeds_before_2018, average_mobile_peak_download_speeds_before_2018, 1)
plt.plot(average_mobile_download_speeds_before_2018, m * average_mobile_download_speeds_before_2018 + b)

# assuming the linear trend is consistent, use average peak download speeds to predict average mobile download speeds when unavailable
average_mobile_peak_download_speeds_after_2017 = np.array([67.3, 41.2, 33.2, 27.4, 23.1])
average_mobile_peak_download_speeds_after_2017 += (86.5 - 70.8)  # set the measurements on the akamai scale to account for discrepancies
average_mobile_download_speeds_after_2017 = (average_mobile_peak_download_speeds_after_2017 - b) / m

# plot new predicted points onto graph
plt.plot(average_mobile_download_speeds_after_2017, average_mobile_peak_download_speeds_after_2017, '*')
plt.title('Average Mobile Peak Download vs. Download Speeds in the US')
plt.xlabel('Average Mobile Download Speeds in the US')
plt.ylabel('Average Mobile Peak Download Speeds in the US')

# reverse the orientation of data points to find the relationship between the year and average download speeds
average_mobile_download_speeds = np.concatenate((average_mobile_download_speeds_after_2017, average_mobile_download_speeds_before_2018))[
                          ::-1]
average_mobile_peak_download_speeds = np.concatenate(
    (average_mobile_peak_download_speeds_after_2017, average_mobile_peak_download_speeds_before_2018))[::-1]
print(average_mobile_download_speeds)
average_mobile_internet_speeds_while_in_use = (average_mobile_download_speeds + average_mobile_peak_download_speeds) / 2
years = np.arange(2010, 2022)
plt.show()

# find the exponential model that best represents the data

plt.plot(years, average_mobile_internet_speeds_while_in_use, 'o')
log_average_mobile_internet_speeds_while_in_use=np.log(average_mobile_internet_speeds_while_in_use)
m2, b2 = np.polyfit(years, log_average_mobile_internet_speeds_while_in_use, 1)
# print(m3)
# print(b3)
plt.plot(years, np.exp(b2) * np.exp(m2*years))

# using the exponential function derived above, predict average internet download speeds for the following ten years
following_ten_years = np.arange(2022, 2033)
expected_average_mobile_internet_speeds = np.exp(b2) * np.exp(m2*following_ten_years)
print(following_ten_years)
print(expected_average_mobile_internet_speeds)
plt.plot(following_ten_years, expected_average_mobile_internet_speeds, '*')

# plot and label graph
plt.title('Average Internet Download Speeds in the US vs. Year')
plt.xlabel('Year')
plt.ylabel('Average Internet Download Speeds')
plt.show()

# find equation to represent download speed for a plan vs. the median monthly price, use data from D2, 2014 table
# use upper bounds on plan download speeds
plan_speeds = np.array([6, 20, 30, 50, 150])
plan_median_monthly_prices = np.array([34.99, 41.95, 54.97, 59.95, 69.99])
plt.plot(plan_speeds, plan_median_monthly_prices, 'o')
log_plan_speeds = np.log(plan_speeds)
m3, b3=np.polyfit(log_plan_speeds, plan_median_monthly_prices, 1)
print(m3)
print(b3)
plt.plot(plan_speeds, m3*log_plan_speeds + b3)
plt.title('Plan Median Monthly Prices vs. Plan Speeds in the US')
plt.xlabel('Plan Speeds in the US')
plt.ylabel('Plan Median Monthly Prices')
plt.show()

# use the derived logarithmic expression to find the expected prices for the future expected average internet speeds
predicted_monthly_prices_for_mobile_internet_each_year = m3*np.log(expected_average_mobile_internet_speeds) + b3
print(predicted_monthly_prices_for_mobile_internet_each_year)

predicted_cost_per_mbps_for_mobile_for_next_ten_years = predicted_monthly_prices_for_mobile_internet_each_year/expected_average_mobile_internet_speeds
print(predicted_cost_per_mbps_for_mobile_for_next_ten_years)