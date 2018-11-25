import mws
from datetime import datetime, timedelta
import click
from anoti import api, config, rules, dto


@click.command()
def cli():
    pulse()

def pulse():
    pulse_range = timedelta(hours=120)
    pulse_interval = timedelta(hours=1)
    pulse_orders = api.CompleteOrders(last_updated_after=datetime.now()-pulse_range)
    new_orders = []
    for order in pulse_orders.complete_orders:
        print(order)
        if all([rule(order) for rule in rules.rules]):
            alert(order)
        if rules.is_shipped(order):
            print('is shipped!')

        if rules.is_new(order):
            new_orders.append(order)
    dto.save_orders(*new_orders)

def alert(order):
    print('Woah!!!')

def save(orders):
    pass

if __name__ == '__main__':
    cli()
