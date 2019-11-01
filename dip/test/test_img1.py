#!/usr/bin/python





import math, operator

from twisted.internet.defer import Deferred
from twisted.internet import reactor
from PIL import Image
def main():
	file1="/dip/test/test_scrin/scrin1.png"
	print file1



	#file2="/dip/test/test_scrin/scrin2.png"
	return self.expectScreen(file1, 0)

def expectScreen(self, filename, maxrms=0):
        """ Wait until the display matches a target image
            filename: an image file to read and compare against
            maxrms: the maximum root mean square between histograms of the
                    screen and target image
        """
        #log.debug('expectScreen %s', filename)
	return self._expectFramebuffer(filename, 0, 0, maxrms)

def _expectFramebuffer(self, filename, x, y, maxrms):
        self.framebufferUpdateRequest(incremental=1)
        image = Image.open(filename)
        w, h = image.size
        self.expected = image.histogram()
        self.deferred = Deferred()
        self.deferred.addCallback(self._expectCompare, (x, y, x + w, y + h), maxrms)
	return self.deferred

def _expectCompare(self, data, box, maxrms):
	image = "/dip/test/test_scrin/scrin2.png" #self.screen.crop(box)
	print image

        hist = image.histogram()
        if len(hist) == len(self.expected):
            sum_ = 0
            for h, e in zip(hist, self.expected):
                sum_ += (h - e) ** 2
            rms = math.sqrt(sum_ / len(hist))

       ))
            if rms <= maxrms:
                return self

        self.deferred = Deferred()
        self.deferred.addCallback(self._expectCompare, box, maxrms)
        self.framebufferUpdateRequest(incremental=1)  # use box ~(x, y, w - x, h - y)?

	return self.deferred

