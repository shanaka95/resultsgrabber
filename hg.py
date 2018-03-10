import urllib,re,zlib,urllib2,requests
import base64
def findkey():
        link='http://www.doenets.lk/result/alresult.jsf'
        sock = urllib.urlopen(link) 
        htmlSource = sock.read()                            
        sock.close()
        key=re.findall ('<input type="hidden" name="javax.faces.ViewState" id="javax.faces.ViewState" value="(.*?)" autocomplete="off" />',htmlSource, re.DOTALL)[0].strip()
        return key
        
def res(index):
        ky=urllib.quote_plus(findkey())
        link=r'http://www.doenets.lk/result/alresult.jsf?frm=frm&frm%3Ausername='+index+'&frm%3AbtnSubmit=&javax.faces.ViewState='+ky      
        sock = urllib.urlopen(link) 
        htmlSource = sock.read()                            
        sock.close()
        exam=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Examination :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        year=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Year :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        name=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Name :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        index=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Index Number :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        stream=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Stream :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        zscore=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Z-Score :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        drank=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">District Rank :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        irank=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Island Rank :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        irank=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Island Rank :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        return (exam,year,name,index,stream,zscore,drank,irank)

print res('6052657')
