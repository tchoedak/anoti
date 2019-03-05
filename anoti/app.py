from datetime import datetime
import click
import time
from anoti import api, config, rules, dto, reports, emailer, sms
from anoti.util import logger


@click.group()
def cli():
    pass


@click.command()
@click.argument('minutes_interval')
def pulse(minutes_interval):
    '''
    Activate a pulse check on recent orders against Amazon's MWS API
    '''
    while True:
        logger.info(f'Finding orders since {datetime.now() - config.TIMEDELTA_RANGE}')
        orders = api.CompleteOrders(
            created_after=datetime.now() - config.TIMEDELTA_RANGE
        )
        new_orders, alerts, total = [], [], []
        for order in orders.complete_orders:
            if all([rule(order) for rule in rules.rules]):
                # add order to alerts queue if all rules are met
                alerts.append(order)
            if rules.is_new(order):
                # save new orders to the DB
                new_orders.append(order)
            total.append(order)

        logger.info(f'Found {len(total)} total orders')
        logger.info(f'Captured {len(alerts)} alerts to be sent')
        alert(alerts)
        logger.info(f'Saving {len(new_orders)} new orders to the DB')
        dto.save_orders(*new_orders)
        sleep_minutes = int(minutes_interval) * 60
        logger.info(f'Sleeping for {minutes_interval} minutes')
        time.sleep(sleep_minutes)


def alert(orders):
    '''
    Perform configured alerts for ``orders``
    '''
    reports.print_orders(*orders)
    if config.email_enabled and orders:
        emailer.send_order_message(reports.html_report(*orders))
    if config.sms_enabled and orders:
        sms.send_text_message(reports.sms_report(*orders))


cli.add_command(pulse)


if __name__ == '__main__':
    cli()
