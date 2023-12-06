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


def macd_cross(candles):
    """As evaluate function, takes pandas.DataFrame contains 'MACD..._XA_0' column,
    return: (str)what_to_action, (str)mode_buy_or_sell.
    """
    cols = candles.columns.to_list()
    col_xa = {'name': c for c in cols if c.startswith('MACD') and ('_XA_' in c)}
    col_xb = {'name': c for c in cols if c.startswith('MACD') and ('_XB_' in c)}
    if not col_xa or not col_xb:
        return 'Stay', 'NA'
    buy_signal  = candles.iloc[-1][col_xa.get('name')]
    sell_signal = candles.iloc[-1][col_xb.get('name')]
    if sum([buy_signal, sell_signal]) == 1:
        if  buy_signal == 1: return 'Open', 'buy'
        if sell_signal == 1: return 'Open', 'sell'
    return 'Stay', 'Wait'
