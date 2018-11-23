import mws
from datetime import datetime, timedelta
import click
from anoti import api, config, rules


@click.command()
def cli():
    pulse()

def pulse():
    pulse_range = timedelta(hours=120)
    pulse_interval = timedelta(hours=1)
    pulse_orders = api.CompleteOrders(last_updated_after=datetime.now()-pulse_range)
    for order in pulse_orders.complete_orders:
        print(order)
        if all([rule(order) for rule in rules.rules]):
            alert(order)
        if rules.is_shipped(order):
            print('is shipped!')

def alert(order):
    print('Woah!!!')

def save(orders):
    pass

if __name__ == '__main__':
    cli()
