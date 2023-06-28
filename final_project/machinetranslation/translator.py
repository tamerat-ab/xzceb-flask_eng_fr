from  deep_translator import  MyMemoryTranslator


def english_to_french(englishtext):
    """translates from English to French"""    
    frenchtext = MyMemoryTranslator( source = 'english', target = 'french').translate(englishtext)
    return frenchtext

def french_to_english(frenchtext):
    """translates from English to French"""  


    englishtext = MyMemoryTranslator(source = 'french', target = 'english').translate(frenchtext)
    return englishtext
