# rpi_webcamera

camera.pyだけラズパイで実行

python3 camera.py



PC側
lib/images/ini.jpgに適当な画像ファイルを作っておく

lib/main.dart
```
var url = Uri.parse('http://192.168.1.25:5000/');
↓
var url = Uri.parse('http://ラズパイIP:5000/');
```

