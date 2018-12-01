import mws
from datetime import datetime, timedelta
import click
from anoti import api, config, rules, dto, reports, email

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

def alert(*orders):
    reports.print_orders(*orders)
    if config.email_enabled:
        email.send_order_message(report.text_report(*orders))
    if config.sms_enabled:
        print('woah!')

if __name__ == '__main__':
    cli()
