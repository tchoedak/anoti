import mws
from datetime import datetime
import click
from anoti import api, config, rules, dto, reports, emailer, sms


def pulse():
    '''
    Activate a pulse check on recent orders against Amazon's MWS API
    '''
    orders = api.CompleteOrders(
        last_updated_after=datetime.now() - config.TIMEDELTA_RANGE
    )
    new_orders, alerts = [], []
    for order in orders.complete_orders:
        if all([rule(order) for rule in rules.rules]):
            # add order to alerts queue if all rules are met
            alerts.append(order)
        if rules.is_new(order):
            # save new orders to the DB
            new_orders.append(order)
    alert(alerts)
    dto.save_orders(*new_orders)


def alert(orders):
    '''
    Perform configured alerts for ``orders``
    '''
    reports.print_orders(*orders)
    if config.email_enabled and orders:
        emailer.send_order_message(reports.html_report(*orders))
    if config.sms_enabled and orders:
        sms.send_text_message(reports.sms_report(*orders))


if __name__ == '__main__':
    pulse()
