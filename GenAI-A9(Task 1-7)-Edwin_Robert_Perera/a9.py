import numpy as np

#Task 1: Creating Numpy arrays
one_dim_array = ([1, 2, 3, 4, 5,6,7,8,9,10])
two_dim_array = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array=np.array([10,20,30,40,50])

np1array=np.array(one_dim_array)
print(np.shape(np1array),np1array.dtype)
np2array=np.array(two_dim_array)
print(np.shape(np2array),np2array.dtype)
print(np.shape(array),array.dtype)

#Task 2: Important Mathematical Operations
A=np.array([10,20,30,40])
B=np.array([1,2,3,4])
print('Addition:',A+B,'\nSubtraction:',A-B,'\nMultiplication:',A*B,'\nDivision:',A/B,"\nPower:",A**B)

#Task 3: Important Numpy Mathematical Formulas
values=np.array([2,4,6,8,10])
print("Squareroot",np.sqrt(values),"\nExponential:",np.exp(values),"\nLogarithm:",np.log(values),"\nSum:",np.sum(values),"\ncumulative Sum:",np.cumsum(values))

#Task 4: Aggregation Functions
data=np.array([[10,20,30],[40,50,60],[70,80,90]])

print("row wise sum:",np.sum(data,axis=1),"\ncolumn wise sum:",np.sum(data,axis=0),"\n Overall Mean:",np.mean(values),"\nMinimum Value:",np.min(values),"\nMaximum Value:",np.max(values))
#Task 5: Statistical Operations
marks=np.array([78,85,90,66,72,88,95,60])
minvalue=np.min(marks)
maxvalue=np.max(marks)
print("Mean:",np.mean(marks),"\nMedian:",np.median(marks),"\nStandard Deviation:",np.std(marks),"\nVariance:",np.var(marks),"\nMin value:",minvalue,"\nMax value:",maxvalue,"\nRange:",maxvalue-minvalue)

#Task 6: Percentiles and Sorting
percentile_25=np.percentile(marks,25)
percentile_50=np.percentile(marks,50)
percentile_75=np.percentile(marks,75)
sorted_marks=np.sort(marks)
avgmarks=np.mean(marks)
print("25th Percentile:",percentile_25,"\n50th Percentile:",percentile_50,"\n75th Percentile:",percentile_75,"\nSorted Marks:",sorted_marks,"\nAverage Marks:",avgmarks)

#Task 7: Mini Use Case:Sales Analysis
sales=np.array([1200,1500,900,2000,1800,1700,1600])
Total_weekly_sales=np.sum(sales)
Average_daily_sales=np.mean(sales)
Highest_sales_day=np.where(sales==np.max(sales))[0]
Lowest_sales_day=np.where(sales==np.min(sales))[0]
Standard_deviation_sales=np.std(sales)
sales_above_average=np.where(sales>Average_daily_sales)[0]

print("Total Weekly Sales:",Total_weekly_sales,"\nAverage Daily Sales:",Average_daily_sales,"\nHighest Sales Day:",Highest_sales_day,"\nLowest Sales Day:",Lowest_sales_day,"\nStandard Deviation of Sales:",Standard_deviation_sales,"\nSales Above Average:",sales_above_average)