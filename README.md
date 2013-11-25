![img](https://raw.github.com/paulshi/iplookup/master/logo.png)

This script trys to make http://ip-api.com/json/ looks better on a daily use. 

The desktop view has a map on the bottom showing the current location of the ip. The mobile version is responsive without map and github banner

##Demo
https://iplook.herokuapp.com

http://iplook.co (http only)

##Setup
Setup virtual environment

```
virtualenv ev
source ev/bin/activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Run

```
python main.py
```

It will then run on http://localhost:5000

Enjoy

:)

##Credits
The backend API is powered by [IP Geolocation API](http://ip-api.com/docs/). They provide free usage of their API for non-commercial use.

The template is [Bootstrap](http://getbootstrap.com/).

[Map marker](http://thenounproject.com/noun/map-marker/#icon-No16939) was designed by [Kelly Walker](http://thenounproject.com/kellylesliewalker/) from The Noun Project

The color of the text is 紅(kurenai) from [Nippon Colors](http://nipponcolors.com/#kurenai).

The web framework used is [Flask](http://flask.pocoo.org/).

Redesign inspired by [@sleepingkyoto](http://twitter.com/sleepingkyoto) ([github](https://github.com/liliff)) at [ip.milk.tea.jp](http://ip.milk.tea.jp)


##Google Map Styling
If you are wondering how you can reuse my Google Map styling, I have created a simple version here: [https://github.com/paulshi/GoogleMapStyling](https://github.com/paulshi/GoogleMapStyling)

##Documentation
[http://iplookup.readthedocs.org/](http://iplookup.readthedocs.org/)

##License
```
The MIT License (MIT)

Copyright (c) 2013 (Paul) Jianer Shi (hipaulshi@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
##Why Did I Build This?
[http://blog.paulshi.me/technical/2013/11/21/IP-Look.html](http://blog.paulshi.me/technical/2013/11/21/IP-Look.html)

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/paulshi/iplookup/trend.png)](https://bitdeli.com/free "Bitdeli Badge")