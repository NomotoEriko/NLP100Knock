# -*- coding: utf-8 -*-
"""
$ java -cp "/usr/local/lib/stanford-corenlp-full-2013-06-20/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP\
 -annotators tokenize,ssplit,pos,lemma,ner,parse,coref -file data/nlp.txt  -outputDirectory data
"""
# stanfordcorenlpはその年のを使いましょう。どんどんよくなります。
# nlp.txt.xmlをブラウザで綺麗に開くには、同ディレクトリにCoreNLP-to-HTML.xslが必要
# stanford-corenlp*/CoreNLP-to-HTML.xslからコピーしてくる。
# 残念ながらパスで指定はうまくいかなかった。
import xml.etree.ElementTree as et


def load_xml_in_word(path='../../data/nlp.txt.xml'):
    tree = et.parse(path)
    root = tree.getroot()
    return '\n'.join(w.text for w in root.findall('.//word'))


if __name__ == '__main__':
    print(load_xml_in_word())
