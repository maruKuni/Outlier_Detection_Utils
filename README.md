# Outlier Detection Utils

## これは何

外れ値検知用のPythonライブラリ．
現状では正規性のあるデータに適用できる3シグマ法ベースの`n_sigma`と，正規性が仮定できないデータに使える中央値ベースの`DOMAD`が利用可能です．

## 使い方

### インスタンスの作成

`outlier_detection_utils`をインポートして`Outlier_Detection`のインスタンスを作ってください．
```python
import outlier_detection_utils as odu

OD = odu.Outlier_Detection()
```
上の例の`OD`から`n_sigma()`や`DOMAD()`を呼び出せます．

### 関数呼び出し

`OD.n_sigma()`にしても`OD.DOMAD()`にしても，基本的には外れ値を検知したい配列を渡してやれば最低限は使えます．

```python
>>> import numpy as np
>>> import outlier_detection_utils as odu
>>> OD = odu.Outlier_Detection()
>>> x = np.array([1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90])
>>> OD.DOMAD(x)
[17, 18, 19]
>>> OD.n_sigma(x)
array([19])

```

戻り値は，外れ値のインデックス配列です．外れ値検知で計算した統計量とかも返した方がいいのかなぁ．

デフォルトパラメータはそのうち解説します．
早く知りたい人はソースコード読んでください．