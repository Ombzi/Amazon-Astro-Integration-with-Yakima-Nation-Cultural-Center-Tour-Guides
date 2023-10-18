from googletrans import Translator as googletrans_Translator
from translate import Translator as translate_Translator
from deep_translator import *
import openapi
chatGPT_api_key = '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'

# init the Google API translator
googletrans_Translator = googletrans_Translator()
# init the translate translator
translate_Translator = translate_Translator(to_lang='es')

# the phrase every translator will use
inputPhrase = "Welcome to our museum"

# translate using googletrans
translation = googletrans_Translator.translate(inputPhrase, dest='spanish')
print(f"{translation.origin} --> {translation.text} :google")

# translate using translator
translation = translate_Translator.translate(inputPhrase)
print(f"{inputPhrase} --> {translation} :translate")


# deep-translator
# deep_google_result = GoogleTranslator(source='auto', target='es').translate(inputPhrase)
# deep_LingueeTranslator_result = LingueeTranslator(source='auto', target='spanish').translate(inputPhrase)
# deep_MyMemoryTranslator_result = MyMemoryTranslator(source='english', target='spanish').translate(inputPhrase)
deep_chatGPT_result = ChatGptTranslator(source='english', target='spanish', api_key = chatGPT_api_key).translate(inputPhrase)
# print(f"{inputPhrase} --> {deep_google_result} :deep google")
# print(f"{inputPhrase} --> {deep_LingueeTranslator_result} :deep Linguee")
# print(f"{inputPhrase} --> {deep_MyMemoryTranslator_result} :deep MyMemory")
print(f"{inputPhrase} --> {deep_chatGPT_result} :deep ChatGPT")