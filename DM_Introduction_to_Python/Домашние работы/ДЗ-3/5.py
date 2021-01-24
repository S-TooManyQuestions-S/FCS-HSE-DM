import typing as tp
from enum import Enum

import numpy as np
import pandas as pd


class Transmission(Enum):
    AUTO = 'auto'
    MANUAL = 'manual'
    ROBOT = 'robot'


def merge_ratings(*rate_configs: tp.Iterable[tp.Tuple[str, pd.DataFrame]]) -> pd.DataFrame:
    '''
    Merge array of ratings `rate_configs` in a one dataframe, storing ratings names

    :param rate_configs: list of `Tuple(name, rating_df)`, where `name` - is rating name and
    `rating_df` - is a table of format `{'car_id': int, 'rating': float}`
    :return: merged dataframe with format `{'car_id': int, 'rating_name1': float, ...}`
    '''
    
