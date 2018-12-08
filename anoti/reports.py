from beautifultable import BeautifulTable
from . import util
import pandas as pd
from collections import Counter


def print_orders(*orders):
    '''
    Print a text report of orders
    '''
    print(
        '''
    \033[1;32m====================================================================='''
    )
    report = text_report(*orders)
    print(report)


def text_report(*orders):
    '''
    Generate a report suitable for viewing as just text on a screen
    '''
    table = BeautifulTable()
    table.column_headers = [
        'Order Id',
        'Order Type',
        'Title',
        'Order Amount',
        'Purchase Date',
    ]
    for order in orders:
        table.append_row(
            [
                order.AmazonOrderId,
                order.OrderType,
                order.OrderItem.Title,
                order.OrderTotal.Amount if 'OrderTotal' in order.keys() else 'N/A',
                order.PurchaseDate,
            ]
        )

    table.sort('Purchase Date')
    return table


def html_report(*orders):
    '''
    Generate a report suitable for viewing as html through email or webpage
    '''
    data = [
        {
            'Order Id': order.AmazonOrderId,
            'Order Type': order.OrderType,
            'Title': order.OrderItem.Title,
            'Order Amount': order.OrderTotal.Amount
            if 'OrderTotal' in order.keys()
            else 'N/A',
            'Purchase Date': order.PurchaseDate,
        }
        for order in orders
    ]
    return pd.DataFrame(data).to_html()


def sms_report(*orders):
    '''
    Generate a report suitable for SMS/text messaging by following a character limit
    '''
    elipses = '...'
    character_limit = 160
    counter = Counter([order.OrderItem.Title for order in orders])
    count_summary = '. '.join([f'{n} {item} sold' for item, n in counter.items()])
    payload = ' '.join([f'You have {len(orders)} new orders.', count_summary])

    if len(payload) > character_limit:
        payload = payload[: character_limit - len(elipses)]
        payload = ''.join([payload, elipses])
    return payload[:character_limit]
