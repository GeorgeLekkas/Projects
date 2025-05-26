# Projects
Golden Cross Moving average  

Although I am aware that the Golden Cross signal on its own does not constitute a strong argument for predictive analysis, I developed this program as a means to gain a clearer picture of its behavior and potential significance within specific time frames.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------
stages

1)A list is created containing the tickers of the stocks to be examined for the Golden Cross signal. (These are the stocks under analysis.)

2)For each stock, it checks whether a Golden Cross signal has occurred, and if so, analyzes its price movement over the following 30 days, within the time frame we define.

3)It records statistics such as the maximum and minimum stock price during that 30-day period, as well as on which day (after the signal) those extreme values occurred.


📁 CSV Output Columns
1st column: Stock ticker

2nd column: Date when the Golden Cross signal was detected

3rd column: Stock price on the day the Golden Cross occurred (crossover of moving averages)

4th column: Percentage difference between the stock price on the Golden Cross day and the maximum price during the following 30 days:
  percentage = (MAX - GC) / GC


5th column: Maximum stock price within the 30-day period [MX]

6th column: Number of days after the signal until the maximum price occurred

7th column: Minimum stock price within the 30-day period [MN]

8th column: Number of days after the signal until the minimum price occurred

9th column: The sum of all differences between each day’s price and the GC price during the 30-day period:
  sum = Σ (stock_price[i] - GC)
