from typing import List

from plotly.offline import init_notebook_mode, iplot
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import statsmodels.stats.api as sms



def plot_afternoon_returns_on_morning_returns_error_bar(
    results: pd.DataFrame, epsilon: float = 0.005, width: float = 0.02,
    empirical_distribution_returns: bool = True,
    alpha: float = 0.05
) -> None:
    '''
    Plots afternoon returns and the number of their occurences
    dependent on the morning returns (starting from -width% up to width% with steps length equal to epsilon).
    The plotted distribution of returns is either empirical (if empirical_distribution_returns) or set to be normal otherwise.
    '''
    lower_bounds_graph = np.linspace(-width, width - epsilon, int(width / epsilon))
    upper_bounds_graph = np.linspace(-width + epsilon, width, int(width / epsilon))

    mean_returns: List[float] = []
    occurrences: List[int] = []
    points: List[float] = []
    ci0: List[float] = []
    ci1: List[float] = []

    for alfa_L, alfa_U in zip(lower_bounds_graph, upper_bounds_graph):
        sub_results = results[(alfa_L < results.relative_diff) & (results.relative_diff < alfa_U)]
        mean_return = sub_results.over_night_change.mean()
        occurrence = sub_results.date.count()
        point = alfa_L + epsilon / 2

        mean_returns.append(mean_return)

        if occurrence > 10:
            if empirical_distribution_returns:
                ci0_local_estimate = -sub_results.over_night_change.quantile(alpha / 2) + mean_return
                ci1_local_estimate = sub_results.over_night_change.quantile(1 - alpha / 2) - mean_return
            else:
                ci = sms.DescrStatsW(sub_results.over_night_change).zconfint_mean(alpha = alpha)
                ci0_local_estimate = -ci[0] + mean_return
                ci1_local_estimate = ci[1] - mean_return

            ci0.append(ci0_local_estimate)
            ci1.append(ci1_local_estimate)
        else:
            ci0.append(np.nan)
            ci1.append(np.nan)
        occurrences.append(occurrence)
        points.append(point)

    trace_returns = go.Scatter(
        x = points,
        y = mean_returns,
        mode = 'lines+markers',
        name = 'Mean overnight returns',
        error_y = {
            'type': 'data',
            'symmetric': False,
            'array': ci1,
            'arrayminus': ci0,
            'visible': True,
            'color': 'grey',
            'thickness': 1,
            'width': 7,
            'opacity': 1
        }
    )

    trace_occurences = go.Scatter(
        x = points,
        y = occurrences,
        mode = 'markers',
        name = 'Number of occurrences',
        yaxis = 'y2'
    )

    if empirical_distribution_returns:
        distribution_text = 'with empirical confidence intervals'
    else:
        distribution_text = 'with confidence intervals from the normal distribution'
    layout = {
        'title': 'Expected overnight return given the yesterday afternoon return, {}.'.format(distribution_text),
        'yaxis': {'title': 'Overnight returns (open / close)'},
        'yaxis2': {'title': 'Number of occurrences', 'overlaying': 'y', 'side': 'right'},
        'xaxis': {'title': 'Yesterday afternoon returns (close / VWAP)'}
    }
    init_notebook_mode()
    iplot({'data': [trace_returns, trace_occurences], 'layout': layout})
