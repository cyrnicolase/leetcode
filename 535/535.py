#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
DocString
'''

import md5

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """


    def md5Str(self, str):
        m = md5.new()
        m.update(str)

        return m.hexdigest()


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

code = Codec()
output = code.encode('http://www.baidu.com/foobar')
print output
