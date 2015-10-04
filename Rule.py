#!/usr/bin/env python

class Rule(object):
    def __init__(self, hist, ruleHist, srcID, srcField, dstID, dstField):
        self.hist = hist
        self.ruleHist = ruleHist
        self.srcID = srcID
        self.srcField = srcField
        self.dstID = dstID
        self.dstField = dstField

    def __str__(self):
        return 'ID {!s} {!s} {!s} {!s} {!s}'.format(self.hist, self.srcID, self.srcField, self.dstID, self.dstField)

    def __repr__(self):
        return '{!r} {!r} {!r} {!r} {!r}'.format(self.hist, self.srcID, self.srcField, self.dstID, self.dstField)

    def toFile(self):
        return 'RULE transition:{0} srcID:{1} srcField:{2} dstField:{3} type:ExactRule\n\n'\
            .format(self.ruleHist.toFile(), self.srcID, self.srcField, self.dstField)
