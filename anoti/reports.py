from beautifultable import BeautifulTable
from .util import logger
import pandas as pd
from collections import Counter


def print_orders(*orders):
    '''
    Print a text report of orders
    '''
    logger.info(
        '''
    \033[1;32m====================================================================='''
    )
    report = text_report(*orders)
    logger.info(report)


def text_report(*orders):
    '''
    Generate a report suitable for viewing as just text on a screen
    '''
    table = BeautifulTable()
    table.column_headers = [
        'Order Id',
        'SKU',
        'Order Type',
        'Title',
        'Order Amount',
        'Purchase Date',
    ]
    for order in orders:
        table.append_row(
            [
                order.AmazonOrderId,
                order.OrderItem.SellerSKU,
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
    header = """
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
    <style>
      body {
        padding-top: 40px;
        padding-bottom: 40px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <main role="main">
        <div class="row marketing">
          <div class="col-lg-12">
            <h2>You have new amazon orders!:</h2>
          </div>
          <div class="card col-lg-12" style="margin-top:20px">
            <div class="card-body">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">OrderId</th>
                      <th scope="col">SKU</th>
                      <th scope="col">OrderType</th>
                      <th scope="col">Title</th>
                      <th scope="col">OrderAmount</th>
                      <th scope="col">Purchase Date</th>
                    </tr>
                  </thead>
                  <tbody>"""

    footer = """
                  </tbody>
                </table>
            </div>
          </div>

        </div>
      </main>
    </div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
  </body>
</html>"""

    body_template = """
                  <thead>
                    <tr>
                      <th scope="row">1</th>
                      <td>{order_id}</td>
                      <td>{seller_sku}</td>
                      <td>{order_type}</td>
                      <td>{title}</td>
                      <td>{order_amount}</td>
                      <td>{purchase_date}</td>
                    </tr>
                  </thead>
"""
    body = ''.join(
        [
            body_template.format(
                order_id=order.AmazonOrderId,
                seller_sku=order.OrderItem.SellerSKU,
                order_type=order.OrderType,
                title=order.OrderItem.Title,
                order_amount=order.OrderTotal.Amount
                if 'OrderTotal' in order.keys()
                else 'N/A',
                purchase_date=order.PurchaseDate,
            )
            for order in orders
        ]
    )

    _html = ''.join([header, body, footer])
    return _html


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
