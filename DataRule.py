#!/usr/bin/env python

from .Rule import Rule


class DataRule(Rule):
    def __init__(self, hist, ruleHist, srcID, srcField, dstID, dstField, data):
        Rule.__init__(self, hist, ruleHist, srcID, srcField, dstID, dstField)
        self.data = list(set(data))

    def __repr__(self):
        return '{!r} {!r} {!r} {!r} {!r} {!r}'.format(self.hist, self.srcID, self.srcField, self.dstID, self.dstField,
                                                      self.data)
    def toFile(self):
        data = ','.join(self.data)
        return 'RULE transition:{0} srcID:{1} srcField:{2} dstField:{3} type:DataRule\ndata:{4}\n' \
            .format(self.ruleHist.toFile(), self.srcID, self.srcField, self.dstField, data)
