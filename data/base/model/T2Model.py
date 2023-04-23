#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 5:06
# @Author  : cap669
# @File    : T2Model.py
# @Software: PyCharm
from pydantic import BaseModel
from typing import Any,List,Dict
class Sub0(BaseModel):
    form:Any
    form_norm:Any
    pos:str
    diocoFreq:str


class NlpModel(BaseModel):
    subs: List[Any]
    wordFrequenciesSupported: bool


class MmModle(BaseModel):
    movieId: str
    originalAudioLangCode_G: str
    originalAudioLangCode_N: str


class SubtitlesModel(BaseModel):
    begin: int
    end: int
    text: str


class PrintIndexesModel(BaseModel):
    sourceIndexes: List[int]
    translationIndexes: List[int]


class HTranslationsModel(BaseModel):
    alignInfo: Dict[int, List[List[int]]]
    printIndexes: List[PrintIndexesModel]
    printSubs: List[List[str]]
    raw: List[SubtitlesModel]
    subs: Dict[int, str]


class DataModel(BaseModel):
    mm: MmModle
    nlp: NlpModel
    subtitles: List[SubtitlesModel]
    hTranslations: HTranslationsModel

class MixModel(BaseModel):
    es:int
    xpos: str
    text: str
class LemmaModle(BaseModel):
    text: str
    # translit: str

class SubsModel(BaseModel):
    xpos: str
    lemma: LemmaModle

class CyModel(BaseModel):
    es:int
    text:str
class OutModel(BaseModel):
    yw:str
    fy:str
    cy:List[SubsModel]
# Tips     :
