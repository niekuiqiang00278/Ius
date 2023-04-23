#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 5:03
# @Author  : cap669
# @File    : PdtBis.py
# @Software: PyCharm
import traceback

from zhconv import convert

from data.base.model.T2Model import OutModel, MixModel, SubsModel, Sub0, CyModel, DataModel
from typing import List,Dict
e = ['WS', 'NOUN', 'AUX', 'ADP', 'VERB','ADV', 'PRON', 'CCONJ', 'PROPN', 'ADJ', 'INTJ', 'NUM']
y = ['SYM','X','PUNCT']
w = ['WS']
import unicodedata
def full2half(uchar):
    try:
        if ord(uchar) >= 0xFF01 and ord(uchar) <= 0xFF5E:
            uchar= chr(ord(uchar) - 0xFEE0)
    except:
        pass
    return uchar


class PdtHit:
    def __init__(self):
        pass


class PdtBis(PdtHit):
    def __init__(self,km2):
        PdtHit.__init__(self)
        self.km2 = km2

    def pd0(self):
        d0 = DataModel(**self.km2('80241859'))
        r0: List[OutModel] = []
        m0: Dict[str, MixModel] = {}
        def y0():
            e0: List[List[SubsModel]] = []
            js = 0
            for s0 in d0.nlp.subs:
                q0: List[SubsModel] = []
                es = 0
                for s1 in s0:
                    def y0():
                        # q0.append(SubsModelxpos=' ', lemma=dict(text=' ', translit=' ')))
                        q0.append(SubsModel(xpos=' ', lemma=dict(text=' ')))

                    def y1():
                        f8 = SubsModel(**s1)
                        f8.xpos = convert(f8.xpos, 'zh-cn')
                        f8.lemma.text = full2half(f8.lemma.text)
                        # f8.lemma.translit = full2half(f8.lemma.translit)
                        q0.append(f8)
                        return f8

                    try:
                        k0 = Sub0(**s1)
                        pos = k0.pos
                        if pos in w:
                            y0()
                        elif pos in y:
                            y1()
                        elif pos in e:
                            f8 = y1()
                            mix = MixModel(es=es, xpos=f8.xpos, text=f8.lemma.text)
                            if m0.get(f8.lemma.text):
                                pass
                            else:
                                m0[f8.lemma.text] = mix
                        else:
                            pass
                    except:
                        print(traceback.format_exc())
                        print(s1)
                        break
                    es += 1
                e0.append(q0)
                js += 1
            return e0

        e0: List[List[SubsModel]] = y0()

        def y1():
            for z0 in d0.hTranslations.printIndexes:
                i0 = []
                i2: List[SubsModel] = []
                for s in z0.sourceIndexes:
                    i0.append(d0.subtitles[s].text)
                    i2 = e0[s]
                i1 = []
                for s in z0.translationIndexes:
                    i1.append(full2half(d0.hTranslations.raw[s].text))

                w0 = OutModel(yw=','.join(i0), fy=','.join(i1), cy=i2)
                r0.append(w0)

        y1()
        for k, v in m0.items():
            print(v.dict())
        # for s in r0:
        #     print(s.dict())

# Tips     :
