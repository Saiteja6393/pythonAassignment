import time
import random
def stock_price_manipulator(base_price, volatility, steps):
    cur=base_price
    for price in range(steps):
        change_per=random.uniform(-volatility,volatility)
        cur=cur+(cur*change_per)
        print(f"{cur:.2f}")
        time.sleep(1)
stock_price_manipulator(200,0.03,10)

