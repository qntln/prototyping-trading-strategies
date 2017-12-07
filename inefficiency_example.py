import numpy as np
from plotly import graph_objs
from plotly.offline import init_notebook_mode, iplot



def generate_and_plot() -> None:
    initial_index = 1
    initial_price = 17

    # efficient price
    prices_before_auction = [initial_price + np.random.normal() / 40 for i in range(120)]
    indices = [initial_index + i for i in range(120)]

    # market moved by exiting positions
    for i in range(1, 61):
        prices_before_auction.append(initial_price + i / 400 + np.random.normal() / 40)
        indices.append(initial_index + 120 + i)

    # moved closing auction - by 1.5%
    relative_closing_auction_inefficiency = 0.015
    prices_before_auction.append((1 + relative_closing_auction_inefficiency) * initial_price)
    indices.append(initial_index + 195)

    # somewhat efficient open auction
    prices_before_auction.append(1.005 * initial_price)
    indices.append(initial_index + 210)

    trace_price = graph_objs.Scatter(
        x = indices[:-2],
        y = prices_before_auction[:-2],
        name = 'Price'
    )
    trace_close = graph_objs.Scatter(
        x = [indices[-2]],
        y = [prices_before_auction[-2]],
        name = 'Closing auction',
        marker = {'size': 12}
    )
    trace_open = graph_objs.Scatter(
        x = [indices[-1]],
        y = [prices_before_auction[-1]],
        name = 'Opening auction',
        marker = {'size': 12}
    )
    data = [trace_price, trace_close, trace_open]
    init_notebook_mode()
    iplot({'data': data, 'layout': {'title': 'Inefficiency example'}})
