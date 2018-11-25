import mws
from datetime import datetime, timedelta
import click
from anoti import api, config, rules, dto, reports

@click.command()
def cli():
    pulse()

def pulse():
    pulse_range = config.TIMEDELTA_RANGE
    pulse_interval = config.TIMEDELTA_INTERVAL
    pulse_orders = api.CompleteOrders(last_updated_after=datetime.now()-pulse_range)
    new_orders = []
    for order in pulse_orders.complete_orders:
        if all([rule(order) for rule in rules.rules]):
            alert(order)
        if rules.is_shipped(order):
            pass
        if rules.is_new(order):
            new_orders.append(order)
    dto.save_orders(*new_orders)
    reports.print_orders(*new_orders)

def alert(order):
    print('Woah!!!')

def save(orders):
    pass

if __name__ == '__main__':
    cli()
