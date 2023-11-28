def macd_A0(df):
    """As evaluate function, takes pandas.DataFrame contains 'MACD..._A_0' column,
    return: (bool)whether_to_open_position, (str)mode_buy_or_sell.
    """
    cols = df.columns.to_list()
    col = [c for c in cols if c.startswith('MACD') and c.endswith('_A_0')]
    signal_col = col[0] if col else ''
    last_signal = df.iloc[-1][signal_col]
    prev_signal = df.iloc[-2][signal_col]
    open_tx = last_signal != prev_signal
    mode = 'buy' if last_signal > 0 else 'sell'
    return open_tx, mode


def macd_cross(df):
    """As evaluate function, takes pandas.DataFrame contains 'MACD..._XA_0' column,
    return: (bool)whether_to_open_position, (str)mode_buy_or_sell.
    """
    cols = df.columns.to_list()
    col_xa = [c for c in cols if c.startswith('MACD') and c.endswith('_XA_0')]
    col_xb = [c for c in cols if c.startswith('MACD') and c.endswith('_XB_0')]
    col_xa = col_xa[0] if col_xa else ''
    col_xb = col_xb[0] if col_xb else ''
    buy_signal = df.iloc[-1][col_xa]
    sell_signal = df.iloc[-1][col_xb]
    open_tx = sum([buy_signal, sell_signal]) == 1
    mode = 'none'
    if open_tx:
        mode = 'buy' if buy_signal == 1 else 'sell'
    return open_tx, mode
