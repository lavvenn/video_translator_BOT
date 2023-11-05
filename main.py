import argostranslate.package
import argostranslate.translate
#22
from_code = "ru"
to_code = "en"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# Translate
translatedText = argostranslate.translate.translate("""Помню, как еще в школе на Basic я писал программу-переводчик. И это было то время, когда ты сам составлял словарь, зашивал перевод каждого слова, а затем разбивал строки на слова и переводил каждое слово в отдельности. В то время я, конечно же, не мог и представить, как сильно продвинутся технологии, и программы-переводчики станут в основе использовать механизмы глубокого обучения с архитектурой трансформера и блоками внимания.

В этот раз я решил окунуться немного в прошлое и сделать то, что хорошо сделать тогда у меня не получилось.

В современных задачах системы перевода нужны достаточно часто, а специалисту, занимающемуся машинным обучением, возможно чаще, чем в других видах деятельности. Потребность в переводчике стала мне необходима, и я решил прибегнуть к использованию облачных решений, в частности Google Translate.

Я программирую на python, и в python есть отличная библиотека translators. Данная библиотека позволяет использовать множество различных сервисов по переводу. Причем абсолютно бесплатно. Однако, все же данное решение не идеально по нескольким причинам:""", from_code, to_code)
print(translatedText)
# '¡Hola Mundo!'