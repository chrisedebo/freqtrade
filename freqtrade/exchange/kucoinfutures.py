"""Kucoinfutures exchange subclass."""
import logging

from freqtrade.enums import MarginMode, TradingMode
from freqtrade.exchange.exchange_types import FtHas
from freqtrade.exchange.kucoin import Kucoin

logger = logging.getLogger(__name__)


class Kucoinfutures(Kucoin):
    """
    Kucoinfutures exchange class.
    """

    _ft_has: FtHas = {
        "stoploss_on_exchange": True,
        "stoploss_order_types": {"limit": "limit", "market": "market"},
        "stoploss_blocks_assets": False,
        "stop_price_param": "stopPrice",
        "stop_price_prop": "stopPrice",
        "funding_fee_candle_limit": 100,
        "ohlcv_candle_limit": 200,
        "tickers_have_bid_ask": True,
        "tickers_have_price": True,
        "l2_limit_range": [20, 100],
        "l2_limit_range_required": False,
        "order_time_in_force": ["GTC", "FOK", "IOC"],
    }

    _supported_trading_mode_margin_pairs: list[tuple[TradingMode, MarginMode]] = [
        (TradingMode.FUTURES, MarginMode.ISOLATED),
        (TradingMode.FUTURES, MarginMode.CROSS),
    ]
