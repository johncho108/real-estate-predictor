# import pandas as pd
# import matplotlib.pyplot as plt
# import regression as r
# import numpy as np
# from scipy import stats

# dataset = pd.read_csv('base/kc_house_data_cleaned.csv')
# x = dataset['price'].to_numpy()
# plt.hist(x, bins=100)
# plt.title('Distribution of House Prices')
# plt.xlabel('House Prices (in Millions of Dollars)')
# plt.ylabel('Frequency')
# plt.show()

# dataset = pd.read_csv('base/kc_house_data_cleaned.csv')
# x = dataset['sqft_living'].to_numpy()
# y = dataset['price'].to_numpy()
# plt.plot(x, y, 'o', alpha=0.5)
# m, b = np.polyfit(x, y, 1)
# plt.plot(x, m*x + b)
# plt.title('House Prices vs. Living Space')
# plt.xlabel('Living Space (in Square Feet)')
# plt.ylabel('House Prices (in Millions of Dollars)')
# plt.show()

# dataset = pd.read_csv('base/kc_house_data_cleaned.csv')
# x = dataset['grade'].to_numpy()
# count_low = count_average = count_high = 0
# for grade in x:
#     if grade <= 6:
#         count_low += 1
#     elif 7 <= grade <= 10:
#         count_average += 1
#     elif grade >= 11:
#         count_high += 1
# count_total = len(x)
# p_low = (count_low / count_total)*100
# p_average = (count_average / count_total)*100
# p_high = (count_high / count_total)*100
# labels = "Low Quality (1-6)", "Average Quality (7-10)", "High Quality (11-13)"
# sizes = [p_low, p_average, p_high]
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
# ax1.axis('equal')
# plt.title('Quality of Construction/Design')
# plt.show()

# regression = r.fit_regression('condition','bathrooms','sqft_lot','floors','waterfront','view', visualize=True)