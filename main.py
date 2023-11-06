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
translatedText = argostranslate.translate.translate("""
если говорить о том что в разработке принимали участие много японцев тяжело не отметить, что игра дерьмо
""",
 from_code, to_code)

 
while True:
    print(argostranslate.translate.translate(input('что перевести?  '),from_code, to_code))
