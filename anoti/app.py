import mws
from datetime import datetime, timedelta
import click
from anoti import orders, config, db, rules


@click.command()
def cli():
    pulse()

def pulse():
    pulse_range = timedelta(hours=24)
    pulse_interval = timedelta(hours=1)
    pulse_orders = orders.orders(last_updated_after=datetime.now() - pulse_range)
    for order in pulse_orders:
        if all([rule(order) for rule in rules.rules]):
            alert(order)
    pulse_orders.save()

def alert(order):
    print('Woah!!!')
