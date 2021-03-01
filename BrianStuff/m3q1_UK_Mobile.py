import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

average_mobile_download_speeds_before_2018 = np.array([27.9, 20.4, 5.6, 3.1, 3.2, 2.7, 2.3])
average_mobile_peak_download_speeds_before_2018 = np.array([66.5, 90.9, 34.6, 19.3, 18.1, 15.1, 16.6])

# find the linear trend between average download and average peak download speeds for when they are available
plt.plot(average_mobile_download_speeds_before_2018, average_mobile_peak_download_speeds_before_2018, 'o')
m, b = np.polyfit(average_mobile_download_speeds_before_2018, average_mobile_peak_download_speeds_before_2018, 1)
plt.plot(average_mobile_download_speeds_before_2018, m * average_mobile_download_speeds_before_2018 + b)

# assuming the linear trend is consistent, use average peak download speeds to predict average mobile download speeds when unavailable
average_mobile_peak_download_speeds_after_2017 = np.array([59.2, 35.2, 20.1, 26.8, 25.8])
average_mobile_peak_download_speeds_after_2017 += (76.1-49.2)  # set the measurements on the akamai scale to account for discrepancies
average_mobile_download_speeds_after_2017 = (average_mobile_peak_download_speeds_after_2017 - b) / m

# plot new predicted points onto graph
plt.plot(average_mobile_download_speeds_after_2017, average_mobile_peak_download_speeds_after_2017, '*')
plt.title('Average Mobile Peak Download vs. Download Speeds in the UK')
plt.xlabel('Average Mobile Download Speeds in the UK')
plt.ylabel('Average Mobile Peak Download Speeds in the UK')

# reverse the orientation of data points to find the relationship between the year and average download speeds
average_mobile_download_speeds = np.concatenate((average_mobile_download_speeds_after_2017, average_mobile_download_speeds_before_2018))[::-1]
average_mobile_peak_download_speeds = np.concatenate(
    (average_mobile_peak_download_speeds_after_2017, average_mobile_peak_download_speeds_before_2018))[::-1]
print(average_mobile_download_speeds)
average_mobile_internet_speeds_while_in_use = (average_mobile_download_speeds + average_mobile_peak_download_speeds) / 2
years = np.arange(2010, 2022)
plt.show()

# find the linear model that best represents the data, assumption of linear relationship because of linear relationship in other UK model
plt.plot(years, average_mobile_internet_speeds_while_in_use, 'o')
m2, b2 = np.polyfit(years, average_mobile_internet_speeds_while_in_use, 1)
# print(m3)
# print(b3)
plt.plot(years, years*m2 + b2)

# using the linear function derived above, predict average internet download speeds for the following ten years
following_ten_years = np.arange(2022, 2033)
expected_average_internet_speeds = b2 + following_ten_years*m2
print(following_ten_years)
print(expected_average_internet_speeds)
plt.plot(following_ten_years, expected_average_internet_speeds, '*')

# plot and label graph
plt.title('Average Internet Download Speeds in the UK vs. Year')
plt.xlabel('Year')
plt.ylabel('Average Internet Download Speeds')
plt.show()

# assumption that a cell plan needs to be purchased to access mobile internet, and that users will not exceed 1 GB of usage
#use the average of prices among all plans to determine the trendline and growth
time_period = np.arange(2015, 2020)
average_monthly_price_of_mobile_plans_across_available_plans=np.array([23.64, 20.33, 19.50, 15.91, 13.84])
plt.plot(time_period, average_monthly_price_of_mobile_plans_across_available_plans, 'o')
m3, b3 = np.polyfit(time_period, average_monthly_price_of_mobile_plans_across_available_plans, 1)
plt.plot(time_period, m3*time_period+b3)

expected_average_monthly_price_of_mobile_plans = m3*following_ten_years + b3
print(expected_average_monthly_price_of_mobile_plans)
plt.plot(following_ten_years, expected_average_monthly_price_of_mobile_plans, '*')

# plot and label graph
plt.title('Expected Average Monthly Price of Mobile Broadband in the UK vs. Year')
plt.xlabel('Year')
plt.ylabel('Average Internet Download Speeds')
plt.show()