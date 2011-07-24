import random
import re
import urllib2
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin

class SeeonResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "seeon.tv"

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)

    def get_media_url(self, web_url):
        response = urllib2.urlopen(web_url)
        html = response.read()
        swf_url, play = re.search('data="(.+?)".+?file=(.+?)\.flv', 
                                  html, re.DOTALL).groups()
        rtmp = 'rtmp://live%d.seeon.tv/edge' % (random.randint(1, 10)) 
        rtmp += '/%s swfUrl=%s pageUrl=%s tcUrl=%s' % (play, swf_url, 
                                                       web_url, rtmp)
        return rtmp
        
    def valid_url(self, web_url):
        return re.match('http:\/\/(?:www.)?seeon.tv\/view\/(?:\d+)(?:\/.+)?',
                        web_url)
    
