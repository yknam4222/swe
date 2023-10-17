import re
from pykospacing import Spacing
import kss
from hanspell import spell_checker
from soynlp.normalizer import *
from konlpy.tag import Okt
from PyKomoran import *
komoran= Komoran(DEFAULT_MODEL['LIGHT'])
punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', } 

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = [line.strip() for line in file.readlines()]
    return stopwords

# stopwords.txt 파일로부터 불용어 로드
stopwords = load_stopwords('stopwords.txt')

def clean(text, punct, mapping): # 불용어 처리
    for p in mapping:
        text = text.replace(p, mapping[p])
    
    for p in punct:
        text = text.replace(p, f' {p} ')
    
    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    for s in specials:
        text = text.replace(s, specials[s])
    
    return text.strip()

def clean_str(text): # 불용어 처리
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s\n]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', string=text)
    text = re.sub('\n', '.', string=text)
    return text 

def spacing_str(text): # 띄어쓰기
    delspacing_text = text.replace(" ", '')  # 공백 제거
    kospacing = Spacing()
    kospacing_text = kospacing(delspacing_text)  # 띄어쓰기 적용
    return kospacing_text

def normalize_str(text): # 위에서 자음, 모음 제거하고 있긴함
    emoticon_norm = emoticon_normalize(text, num_repeats= 2)
    repeat_norm = repeat_normalize(emoticon_norm, num_repeats= 2)

    return repeat_norm

def split_str(text): # 문장 분리
    return kss.split_sentences(text)

def tokenizer_str(text): # 토큰화
    okt = Okt()
    token_text = okt.pos(text)
    return token_text

def remove_stopwords(tokens, stopwords): #불용어 처리
    return [token for token in tokens if token not in stopwords]

def lemmatize(text):
    lemmatized_text = komoran.get_morphes_by_tags(text)
    return lemmatized_text


def preprocess_text(text):
    clean_text1 = clean(text, punct, punct_mapping)
    clean_text2 = clean_str(clean_text1)
    kospacing_text = spacing_str(clean_text2)
    normalize_text = normalize_str(kospacing_text)
    tokenized_text = lemmatize(normalize_text)
    filtered_text = remove_stopwords(tokenized_text, stopwords)
    #split_text = split_str(tokenizer_text)

    okt = Okt()
    print(okt.morphs(normalize_text))
    print(type(filtered_text))
    return filtered_text