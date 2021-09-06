import talib as ta
import yfinance as yf
import matplotlib.pyplot as plt

tick = yf.download('TSLA', '2021-6-1','2021-9-4')

plt.style.use('dark_background')

h1 = plt.subplot(3,2,1)
h2 = plt.subplot(3,2,2)
h3 = plt.subplot(3,2,3)
h4 = plt.subplot(3,2,4)
h5 = plt.subplot(3,2,5)
h6 = plt.subplot(3,2,6)

h1.grid('ON',linestyle=':')
h2.grid('ON',linestyle=':')
h3.grid('ON',linestyle=':')
h4.grid('ON',linestyle=':')
h5.grid('ON',linestyle=':')
h6.grid('ON',linestyle=':')

# Moving average
tick['Simple MA'] = ta.SMA(tick['Close'],14)
tick['EMA'] = ta.EMA(tick['Close'], timeperiod = 14)

# Bollinger Bands 
tick['upper_band'], tick['middle_band'], tick['lower_band'] = ta.BBANDS(tick['Close'], timeperiod =20)

# RSI
tick['RSI'] = ta.RSI(tick['Close'],14) 

tick['upper_RSI'] = 70
tick['lower_RSI'] = 30

# On-balance volume
tick['OBV'] = ta.OBV(tick['Close'], tick['Volume'])

# MACD
tick['macd'], tick['macdsignal'], tick['macdhist'] = ta.MACD(tick['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Stochiastic oscillators
tick['slowk'], tick['slowd'] = ta.STOCH(tick['High'], tick['Low'], tick['Close'], fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0) 
tick['fastk'], tick['fastd'] = ta.STOCHF(tick['High'], tick['Low'], tick['Close'], fastk_period=14, fastd_period=3, fastd_matype=0)

tick['stochosc_high'] = 80
tick['stochosc_low'] = 20

# Plots
h1.plot(tick[['Close','upper_band','middle_band','lower_band']])
h1.legend(['Close','upper_band','middle_band','lower_band'],loc='lower left')
h2.plot(tick[['RSI','upper_RSI','lower_RSI']])
h2.legend(['RSI','upper_RSI','lower_RSI'],loc='lower left')
h3.plot(tick[['Simple MA','EMA']])
h3.legend(['Simple MA','EMA'],loc='lower left')
h4.plot(tick[['macd','macdsignal','macdhist']])
h4.legend(['macd','macdsignal','macdhist'],loc='lower left')
h5.plot(tick[['slowk','slowd','stochosc_high', 'stochosc_low']])
h5.legend(['slowk','slowd','stochosc_high', 'stochosc_low'],loc='lower left')
h6.plot(tick[['fastk','fastd','stochosc_high', 'stochosc_low']])
h6.legend(['fastk','fastd','stochosc_high', 'stochosc_low'],loc='lower left')
plt.show()