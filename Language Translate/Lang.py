from translate import Translator

lang = Translator(to_lang="German")

lang_trans = lang.translate("Good Morning")

print(lang_trans)
