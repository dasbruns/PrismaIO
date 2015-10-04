#!/usr/bin/env python

from .Rule import Rule


class CopyRule(Rule):
    def __init__(self, hist, ruleHist, srcID, srcField, dstID, dstField, typ, ptype, content):
        Rule.__init__(self, hist, ruleHist, srcID, srcField, dstID, dstField)
        self.typ = typ
        self.ptype = ptype
        self.content = list(set(self.content))

    def __str__(self):
        return 'ID {!s} {!s} {!s} {!s} {!s}'.format(self.hist, self.srcID, self.srcField, self.dstID, self.dstField)

    def __repr__(self):
        return '{!r} {!r} {!r} {!r} {!r} {!r} {!r}'.format(self.hist, self.srcID, self.srcField, self.dstID,
                                                           self.dstField, self.ptype, self.content)

    def toFile(self):
        if 'Seq' in self.typ:
            return 'RULE transition:{0} srcID:{1} srcField:{2} dstField:{3} type:SeqRule\ndiff:{4}\n' \
                .format(self.ruleHist.toFile(), self.srcID, self.srcField, self.dstField, self.content)
        elif 'Part' in self.typ:
            if self.ptype == 'SUFFIX':
                ptype = 'COPY_THE_SUFFIX'
            elif self.ptype == 'PREFIX':
                ptype = 'COPY_THE_PREFIX'
            return 'RULE transition:{0} srcID:{1} srcField:{2} dstField:{3} type:CopyPartialRule\nptype:{4} sep:{5}\n' \
                .format(self.ruleHist.toFile(), self.srcID, self.srcField, self.dstField, ptype, self.content)
        elif 'Comp' in self.typ:
            rest = '.'.join(self.content)
            if self.ptype == 'SUFFIX':
                ptype = 'COPY_AS_SUFFIX'
            elif self.ptype == 'PREFIX':
                ptype = 'COPY_AS_PREFIX'
            return 'RULE transition:{0} srcID:{1} srcField:{2} dstField:{3} type:CopyCompleteRule\n' \
                   'ptype:{4} rest:{5}\n'\
                .format(self.ruleHist.toFile(), self.srcID, self.srcField, self.dstField, ptype, rest)

