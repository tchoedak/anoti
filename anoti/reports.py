from beautifultable import BeautifulTable


def print_orders(*orders):
    print("""
    \033[1;32m====================================================================="""
    )
    table = BeautifulTable()
    table.column_headers = ['Order Id', 'Order Type', 'Title', 'Order Amount', 'Purchase date']
    for order in orders:
        table.append_row(
            [
                order.AmazonOrderId,
                order.OrderType,
                order.OrderItem.Title,
                order.OrderTotal.Amount if 'OrderTotal' in order.keys() else 'N/A',
                order.PurchaseDate
            ]
        )

    print(table)

