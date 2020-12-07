import sys

from market_maker.market_maker import OrderManager


class CustomOrderManager(OrderManager):
    """A sample order manager for implementing your own custom strategy"""

    def place_orders(self) -> None:
        # implement your custom strategy here
        if settings.BUY[0] > 0:
            buy_orders = []
            #sell_orders = []
            for i in 1:
                if not self.long_position_limit_exceeded():
                    buy_orders.append(self.prepare_order_2(-i))
                #if not self.short_position_limit_exceeded():
                #    sell_orders.append(self.prepare_order(i))


            return self.converge_orders_2(buy_orders)

def run() -> None:
    order_manager = CustomOrderManager()

    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        order_manager.run_loop()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
