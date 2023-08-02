# Outlier Detection Utils

## これは何

外れ値検知用のPythonライブラリ．
現状では正規性のあるデータに適用できる3シグマ法ベースの`n_sigma`と，正規性が仮定できないデータに使える中央値ベースの`DOMAD`が利用可能です．

## 使い方

`outlier_detection_utils`をインポートして`Outlier_Detection`のインスタンスを作ってください．
```[python]
import outlier_detection_utils as odu

OD = odu.Outlier_Detection()
```
上の例の`OD`から`n_sigma()`や`DOMAD()`を呼び出せます．

パラメータについてはいずれ．