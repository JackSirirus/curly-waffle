#!/usr/bin/python
# coding: utf-8
import re, sys,urllib2,os,csv,codecs
reload(sys)
sys.setdefaultencoding('utf8')
while True:
    file = open('lianjiacsv.csv', 'ab')
    file.write(codecs.BOM_UTF8)
    writer = csv.writer(file)
    title = ['Village information', 'Transaction price', 'Listing time', 'Transaction details', 'Built-up area',
             'Architectural age', 'Latitude and longitude coordinates', 'Website']
    writer.writerow(title)
    url1 = "https://bj.lianjia.com/chengjiao/pg"
    try:
        x = int(raw_input("Please enter a number (end of input 0), with a maximum of 100 pages."))
    except Exception as e:
        print e
        print "please enter a number"
        continue
    if x == 0:
        break
    for xm in range(1,x):
     print xm
     url = url1 + str(xm)
     #print url
     headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
     try:
        html = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(html).read()
     except Exception as e:
        print e
        print "No link!"
     reg = re.compile('<a class="img" href="(.*?)" target="_blank" ')
     items = reg.findall(html, re.S)
     neirong=items

     print("第%d页" % xm)

     for x, neirong in zip(range(1, len(neirong)),neirong):

        urlnew=neirong
        htmlnew=urllib2.Request(urlnew,headers=headers)
        htmlnew=urllib2.urlopen(htmlnew).read()
        regnew=re.compile('<span class="dealTotalPrice"><i>(.*?)</span>')
        regnewname=re.compile('<h1 class="index_h1">(.*?)</h1>')
        listingdate=re.compile('<span class="label">挂牌时间</span>(.*?)</li>')
        transactionrecode=re.compile('<p class="record_detail">(.*?)</p>')
        coveredarea=re.compile('<span class="label">建筑面积</span>(.*?)</li>')
        yearbuilt=re.compile('<span class="label">建成年代</span>(.*?)</li>')
        lnglat=re.compile("resblockPosition:'(.*?)',")


        itemsnewname=regnewname.findall(htmlnew,re.S)
        itemsnew=regnew.findall(htmlnew,re.S)
        listingdatefind=listingdate.findall(htmlnew,re.S)
        transactionrecodefind=transactionrecode.findall(htmlnew,re.S)
        coveredareafind=coveredarea.findall(htmlnew,re.S)
        yearbuiltfind=yearbuilt.findall(htmlnew,re.S)
        lnglatfind=lnglat.findall(htmlnew,re.S)


        for itx in itemsnewname:#标题Village information
             itx=itx
        for ity in itemsnew:#交易价格Transaction price
             ity = "".join(ity.split('>'))
             ity = "".join(ity.split('</i'))
             ity = "".join(ity.split('</i>'))
             ity = "".join(ity.split('\n'))


        for listingdatex in listingdatefind:#挂牌时间Listing time
            listingdatex="".join(listingdatex.split('"'))
            listingdatex="".join(listingdatex.split('         '))

        for transactionrecodex in transactionrecodefind:#交易详情Transaction details
            transactionrecodex=" ".join(transactionrecodex.split(","))

        for coveredareax in coveredareafind:#建筑面积Built-up area
            coveredareax="".join(coveredareax.split('"'))
            coveredareax="".join(coveredareax.split('         "'))
            coveredareax="".join(coveredareax.split('          </li>'))

        for yearbuiltx in yearbuiltfind:#建筑年代Architectural age
            yearbuiltx="".join(yearbuiltx.split('"'))
            yearbuiltx="".join(yearbuiltx.split('"'))

        for lnglatx in lnglatfind:#经纬度坐标Latitude and longitude coordinates
            #listingdatex="".join(lontlatx.split(''))
            lnglatx=lnglatx

        links=[itx,ity,listingdatex,transactionrecodex,coveredareax,yearbuiltx,lnglatx,neirong]
        writer.writerow(links)
        print "第%d条" % x



