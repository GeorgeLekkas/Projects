# Projects

Golden Cross Moving Average . [GC_stat.py]

Long - Short Term Memory Neural Network. [D_D.py], [plh8os.py], and [tst_pl.py].
 
============================================================
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Golden Cross Moving Average . [GC_stat.py]

Although I am aware that the Golden Cross signal on its own does not constitute a strong argument for predictive analysis, I developed this program as a means to gain a clearer picture of its behavior and potential significance within specific time frames.

The Algorithm does:

1)A list is created containing the tickers of the stocks to be examined for the Golden Cross signal. (These are the stocks under analysis.)

2)For each stock, it checks whether a Golden Cross signal has occurred, and if so, analyzes its price movement over the following 30 days, within the time frame we define.

3)It records statistics such as the maximum and minimum stock price during that 30-day period, as well as on which day (after the signal) those extreme values occurred.


📁 CSV Output Columns.


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






------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





Long - Short Term Memory Neural Network.  [LSTM]

The project consists of three scripts: [D_D.py], [plh8os.py], and [tst_pl.py].

>> [D_D.py] || Downloads two datasets:
ticker_D1.csv and ticker_D2.csv

>> [plh8os.py] ||  Trains 4 LSTM models.
It runs two nested for loops over the values of window (w) and units (un) of the LSTM layers.
Therefore, it trains neural networks for all possible combinations of (w, un).
Using the second dataset, it tests each model over the last 30 days and logs statistics into a CSV file.

>> [tst_pl.py] || Visualizes the model of your choice.


How to run the project:

a) In [D_D.py], select the ticker you want to analyze, as well as the date range for training and testing.
Then run the script to download the data.

b) In [plh8os.py], on line 9, set the same ticker you used in the previous script.
Run the script to train the 4 neural networks and generate their corresponding performance statistics.

c) In [tst_pl.py], once again set the same ticker, and also select values for un and w on lines 7 and 8, respectively.
Valid values are:

un ∈ A = (40, 50)

w ∈ B = (50, 60)
where A and B are sets.











  
