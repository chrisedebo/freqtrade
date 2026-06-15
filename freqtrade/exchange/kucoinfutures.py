"""Kucoinfutures exchange subclass."""
import logging

from freqtrade.constants import BuySell
from freqtrade.enums import MarginMode, PriceType, TradingMode
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
        "stop_price_type_field": "stopPriceType",
        "stop_price_type_value_mapping": {
            PriceType.LAST: "TP",
            PriceType.MARK: "MP",
            PriceType.INDEX: "IP",
        },
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

    def _get_stop_params(self, side: BuySell, ordertype: str, stop_price: float) -> dict:
        params = self._params.copy()
        
        # In KuCoin Futures, 'stop' must be 'up' or 'down'
        # For a stoploss on a long position (selling to close), we trigger when price drops ('down')
        # For a stoploss on a short position (buying to close), we trigger when price rises ('up')
        stop_direction = "up" if side == "buy" else "down"
        
        params.update({"stopPrice": stop_price, "stop": stop_direction})
        return params
