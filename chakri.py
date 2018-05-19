from datetime import date
from nsepy import get_history

class Chakri:

    def __init__(self, stock_name, start_date, end_date):
        self.stock_name = stock_name
        self.start_date = start_date
        self.end_date = end_date
    
    def get_complete_history(self):
        print(get_history(symbol=self.stock_name,
                            start=date(2018, 1, 1),
                            end=date(2018, 1, 10),
                          index=True))
        
