# -*- coding: utf-8 -*-

import math


x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方

#WGS84转GCJ02火星坐标
#lng为WGS84的经度坐标，lat为纬度坐标
def wgs84_to_gcj02(lng, lat):

     if out_of_china(lng, lat):  # 判断是否在国内
        return raw_input('This is not in China!')
     dlat = _transformlat(lng - 105.0, lat - 35.0)
     dlng = _transformlng(lng - 105.0, lat - 35.0)
     radlat = lat / 180.0 * pi
     magic = math.sin(radlat)
     magic = 1 - ee * magic * magic
     sqrtmagic = math.sqrt(magic)
     dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
     dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
     mglat = lat + dlat
     mglng = lng + dlng
     return [mglng, mglat]

def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

#判断坐标是否在中国境内，若不在则不做偏移
def out_of_china(lng, lat):
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


if __name__ == '__main__':
    #输入经纬度信息
    print 'Please enter the longitude coordinates:'
    lng=input()
    print 'Please enter the latitude coordinates:'
    lat=input()
    #lng = 128.543
    #lat = 37.065
    result = wgs84_to_gcj02(lng, lat)
    print  result
    raw_input('please enter key to exit')
