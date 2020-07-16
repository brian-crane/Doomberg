# The Purpose of this class is to:
# Update all stock prices in DB stocks.stocks
# Include all stocks that are included in at least ONE portfolio
# Include major index funds
# Run on a cron job cycle
# No outside API interaction planned at the moment

#

from tools import YFinance as YF
from tools import IEXCloud as IEX

print(IEX.getCurrentStockPrice("TSLA"))
