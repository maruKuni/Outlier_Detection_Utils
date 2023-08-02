from typing import Literal
import numpy as np
from numpy.typing import ArrayLike
from scipy import stats


class Outlier_Detection:
    _normality = Literal[True, False, 'auto']
    _normality_test = Literal['KS', 'SW', ]

    def __init__(self) -> None:
        pass

    def _as_array(self, x: ArrayLike) -> np.ndarray:
        return np.array(x)

    def _empritical_quantile(self, x: np.ndarray, upper: np.float64 = 0.75) -> np.float64:
        std = x.std()
        mean = x.mean()
        standardized_x = (x-mean)/std
        upper_bound = np.floor(len(x) * upper)
        quantile = sorted(standardized_x)[upper_bound]
        return quantile

    def _is_normal(self, x: np.ndarray, test: _normality_test) -> bool:
        standardized_x = (x - x.mean()) / x.std()
        p_value: np.float64
        match test:
            case 'KS':
                _, p_value = stats.kstest(standardized_x, stats.norm.cdf)
                pass
            case 'SW':
                _, p_value = stats.shapiro(x)
                pass
        if p_value < 0.05:
            return False
        else:
            return True

    def n_sigma(self, x: ArrayLike, n: np.float64 = 2, ) -> np.ndarray:
        '''
        Detectiing oulier by n-sigma method.

        Parameters
        ---
        x : ArrayLike-object
            Array of data that you want to detect outlier.
        n : int
            For determining threshold of detecting outlier.
            The value out of range [-n * x.std() + x.mean(), n * x.std() + x.mean()] is recognized as outlier.
            default = 2.

        Return
        ---
        np.ndarray : index of outlier data.
        '''
        _x = self._as_array(x)
        std = _x.std()
        mean = _x.mean()
        list_outlier = []
        for i, value in enumerate(_x):
            if -n*std + mean < value and value < n*std+mean:
                continue
            list_outlier.append(i)
        return np.array(list_outlier, dtype=np.int32)

    def DOMAD(self, x: ArrayLike, n: np.float64 = 2, normality: _normality = 'auto', normality_test: _normality_test = 'KS') -> np.ndarray:
        '''
        Detectin Outlier using Mean Absolute Deviation.
        In this method, we detecting outlier using median instead of mean, mean absolute deviation (MAD) instead of standard deviation.

        Parameter
        ---
        x: ArrayLike.
            source array.
        n:np.float64
            determining threshold of outlier detection.
            normal value is in median - n * MAD < value < median + n * MAD.
            default = 2.
        normality: {True, False, 'auto'}
            Is the source array x drawn from normal distribution.
            If this value is 'auto', Automatically normality test executed and recognize x as normal or not.
            default = 'auto'.
        normality_test: {'KS', 'SW'}
            The way of normality test.
            This parameter only use when normality = 'auto'.
            KS ... Kolmogolov - Smirnov test
            SW ... Shapiro - Will test
            default = 'SW'
        '''
        consistency_constant: np.float64
        median = np.median(x)
        mad = np.median(np.abs(x - median))
        outlier_index = []
        match normality:
            case True:
                consistency_constant = 1.4826
            case False:
                consistency_constant = self._empritical_quantile(x)
            case 'auto':
                is_normal: bool = self._is_normal(x)
                if is_normal:
                    consistency_constant = 1.4286
                else:
                    consistency_constant = self._empritical_quantile(x)
        mad = consistency_constant * mad
        for i, value in enumerate(x):
            if np.abs(value - median) / mad > n:
                outlier_index.append(i)
        return outlier_index
