from django.views.generic import View
from django.http import HttpResponse
from natto import MeCab
from django.conf import settings as st


class CallbackView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def get_parts_of_speech(text):
        parts = ''
        with MeCab() as nm:
            for n in nm.parse(text, as_nodes=True):
                if not n.is_eos() and n.is_nor():
                    feature = n.feature.split(',', 1)
                    if 'SF' in feature:
                        parts = 'SF'
                    elif 'FAQ' in feature:
                        parts = 'FAQ'
                    elif '感動詞' in feature:
                        parts = '感動詞'
                    elif '名詞' in feature:
                        parts = '名詞'
        return parts

    @staticmethod
    def get_nominal_words(text):
        words = []
        with MeCab() as nm:
            for n in nm.parse(text, as_nodes=True):
                if not n.is_eos() and n.is_nor():
                    feature = n.feature.split(',', 1)
                    if 'SF' in feature:
                        words.append(n.surface)
                    elif 'FAQ' in feature:
                        words.append(n.surface)
                    elif '感動詞' in feature:
                        words.append(n.surface)
                    elif '名詞' in feature:
                        words.append(n.surface)
        return words


class IndexView(CallbackView):
    def get(self, _):
        speech = '今月の料金って今月の料金ですよね'

        test = self.get_parts_of_speech(speech)
        print(test)

        test1 = self.get_nominal_words(speech)
        print(test1)

        return HttpResponse()
