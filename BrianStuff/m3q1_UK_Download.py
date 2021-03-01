import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

average_download_speeds_before_2018 = np.array([16.9, 14.9, 11.6, 9.9, 7.9, 5.6, 4.6])
average_peak_download_speeds_before_2018 = np.array([76.1, 61.0, 51.6, 42.2, 36.3, 23.7, 17.2])

# find the linear trend between average download and average peak download speeds for when they are available
plt.plot(average_download_speeds_before_2018, average_peak_download_speeds_before_2018, 'o')
m, b = np.polyfit(average_download_speeds_before_2018, average_peak_download_speeds_before_2018, 1)
plt.plot(average_download_speeds_before_2018, m * average_download_speeds_before_2018 + b)

# assuming the linear trend is consistent, use average peak download speeds to predict average download speeds when unavailable
average_peak_download_speeds_after_2016 = np.array([81.1, 65.8, 55.2, 55.6, 49.2])
average_peak_download_speeds_after_2016 += (76.1 - 49.1)  # set the measurements on the akamai scale to account for discrepancies
average_download_speeds_after_2016 = (average_peak_download_speeds_after_2016 - b) / m

# plot new predicted points onto graph
plt.plot(average_download_speeds_after_2016, average_peak_download_speeds_after_2016, '*')
plt.title('Average Peak Download vs. Download Speeds in the UK')
plt.xlabel('Average Download Speeds in the UK')
plt.ylabel('Average Peak Download Speeds in the UK')

# reverse the orientation of data points to find the relationship between the year and average download speeds
average_download_speeds = np.concatenate((average_download_speeds_after_2016, average_download_speeds_before_2018))[
                          ::-1]
average_peak_download_speeds = np.concatenate(
    (average_peak_download_speeds_after_2016, average_peak_download_speeds_before_2018))[::-1]
print(average_download_speeds)
average_internet_speeds_while_in_use = (average_download_speeds + average_peak_download_speeds) / 2
years = np.arange(2010, 2022)
plt.show()


# find the linear model that best represents the data
plt.plot(years, average_internet_speeds_while_in_use, 'o')
m2, b2 = np.polyfit(years, average_internet_speeds_while_in_use, 1)
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

# Line of best Fit for Superfast Connection
average_monthly_price_for_year = np.array([34.25, 29.5, 30.25, 28.25, 26.5, 27.33])
period = np.arange(2014, 2020)
m3, b3 = np.polyfit(period, average_monthly_price_for_year, 1)

# Line of best fit for Fast Connection
average_monthly_price_for_year_fast = np.array([24, 19.75, 22, 18.25, 19, 22])
m4, b4 = np.polyfit(period, average_monthly_price_for_year_fast, 1)

# With the predictions for average internet speeds for the following years and assuming slight decreases in pricing, we can predict the price per mbps for the next ten years
#take into account two sets of values, less than 30 mbps and greater than 30 mbps (don't have to worry about past that because the maximum speed our graph predicts is less than that value)
predicted_monthly_prices_for_internet_for_next_ten_years = np.zeros(expected_average_internet_speeds.shape)
for i in range(0, expected_average_internet_speeds.size):
    if expected_average_internet_speeds[i] < 30:
        predicted_monthly_prices_for_internet_for_next_ten_years[i] = m4*following_ten_years[i] + b4
    else:
        predicted_monthly_prices_for_internet_for_next_ten_years[i] = m3*following_ten_years[i] + b3

print(predicted_monthly_prices_for_internet_for_next_ten_years)

# plot and label graph
plt.plot(period, average_monthly_price_for_year, 'o')
plt.plot(period, average_monthly_price_for_year_fast, 'o')
plt.plot(following_ten_years, predicted_monthly_prices_for_internet_for_next_ten_years, '*')
plt.title('Average Monthly Price in the UK vs. Year')
plt.xlabel('Year')
plt.ylabel('Average Monthly Price in the UK (£)')
plt.show()