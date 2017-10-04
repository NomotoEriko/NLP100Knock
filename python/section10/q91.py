# -*- coding: utf-8 -*-
# nomotoeinashi-no-MacBook-Pro:data nomotoeriko$ cat questions-words.txt | grep -n :
# 1:: capital-common-countries
# 508:: capital-world
# 5033:: currency
# 5900:: city-in-state
# 8368:: family
# 8875:: gram1-adjective-to-adverb
# 9868:: gram2-opposite
# 10681:: gram3-comparative
# 12014:: gram4-superlative
# 13137:: gram5-present-participle
# 14194:: gram6-nationality-adjective
# 15794:: gram7-past-tense
# 17355:: gram8-plural
# 18688:: gram9-plural-verbs
# nomotoeinashi-no-MacBook-Pro:data nomotoeriko$ head -8874 questions-words.txt | \
#  tail -n $((8874-8368+1)) > questions_words_family.txt


if __name__ == '__main__':
    import os
    file_path = "../../data/questions-words.txt"
    out_path = "../../data/questions_words_family.txt"
    os.system("head -8874 $s | tail -n $((8874-8368+1)) > $s" % (file_path, out_path))
