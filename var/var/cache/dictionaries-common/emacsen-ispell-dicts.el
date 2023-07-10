;;; This file is part of the dictionaries-common package.
;;; It has been automatically generated.
;;; DO NOT EDIT!

;; Adding aspell dicts

(add-to-list 'debian-aspell-only-dictionary-alist
  '("english"
     "[a-zA-Z]"
     "[^a-zA-Z]"
     "[']"
     nil
     ("-d" "en")
     nil
     iso-8859-1))
(add-to-list 'debian-aspell-only-dictionary-alist
  '("canadian"
     "[a-zA-Z]"
     "[^a-zA-Z]"
     "[']"
     nil
     ("-d" "en_CA")
     nil
     iso-8859-1))
(add-to-list 'debian-aspell-only-dictionary-alist
  '("british"
     "[a-zA-Z]"
     "[^a-zA-Z]"
     "[']"
     nil
     ("-d" "en_GB")
     nil
     iso-8859-1))
(add-to-list 'debian-aspell-only-dictionary-alist
  '("american"
     "[a-zA-Z]"
     "[^a-zA-Z]"
     "[']"
     nil
     ("-d" "en_US")
     nil
     iso-8859-1))


;; Adding hunspell dicts

(add-to-list 'debian-hunspell-only-dictionary-alist
  '("korean"
     "[\200\201\202\203\204\205\206\207\210\211\212\213\214\215\216\217\220\221\222\223\224\225\226\227\230\231\232\233\234\235\236\237\240\241\242\243\244\245\246\247\250\251\252\253\254\255\256\257\260\261\262\263\264\265\266\267\270\271\272\273\274\275\276\277\352\353\354\355]"
     "[^\200\201\202\203\204\205\206\207\210\211\212\213\214\215\216\217\220\221\222\223\224\225\226\227\230\231\232\233\234\235\236\237\240\241\242\243\244\245\246\247\250\251\252\253\254\255\256\257\260\261\262\263\264\265\266\267\270\271\272\273\274\275\276\277\352\353\354\355]"
     "[']"
     nil
     ("-d" "ko_KR")
     nil
     utf-8))
(add-to-list 'debian-hunspell-only-dictionary-alist
  '("australian"
     "[A-Za-z]"
     "[^A-Za-z]"
     "[']"
     nil
     ("-d" "en_AU")
     nil
     iso-8859-1))



;; No emacsen-aspell-equivs entries were found


;; An alist that will try to map hunspell locales to emacsen names

(setq debian-hunspell-equivs-alist '(
     ("en" "australian")
     ("en_AU" "australian")
     ("ko" "korean")
     ("ko_KR" "korean")
))

;; Get default value for debian-hunspell-dictionary. Will be used if
;; spellchecker is hunspell and ispell-local-dictionary is not set.
;; We need to get it here, after debian-hunspell-equivs-alist is loaded

(setq debian-hunspell-dictionary (debian-ispell-get-hunspell-default))

