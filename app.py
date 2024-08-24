import requests
import pandas as pd
from googletrans import Translator
import os
from flask import Flask, render_template, request, jsonify, send_file, after_this_request
import spacy
from collections import Counter
from string import punctuation
from gtts import gTTS
import tempfile
import base64


app = Flask(__name__, template_folder='templates', static_folder='static')

global dest_language
dest_language = "ko"
global accent
accent = 'uk'

# Translate a word into a destination language
translator = Translator()
def translate_text(text, language_code):
    try:
        translation = translator.translate(text, dest=language_code)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

# update the excel file
def add_word(word, phonetic, phonetic_audio, origin, types, word_translation, definitions, defi_translations, filename):
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        df = pd.DataFrame(columns=['Word', 'phonetic', 'phonetic_audio', 'origin', 'Type', 'Translation', 'Definition', 'Translated_Definition'])
    
    for type, definition in zip(types, definitions):
        df = pd.concat([df, pd.DataFrame({'Word': [word], 'Translation': [word_translation[0]], 'Type': [type], 'Definition': [definition]})], ignore_index=True)
    df.to_excel(filename, index=False)

# get definition, example, type
def get_word_definition(word):
    # Free dictionary api: https://dictionaryapi.dev/
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            global accent
            #origin = data[0].get('origin', 'No origin available.')
            phonetics = data[0].get('phonetics', [])
            phonetic_texts = [phonetic.get('text', 'No phonetic available.') for phonetic in phonetics]
            phonetic_texts = [text for text in phonetic_texts if text != 'No phonetic available.']
            #phonetic_audios = [phonetic.get('audio', 'No audio available.') for phonetic in phonetics]
            #phonetic_audio = phonetic_audios[0] if phonetic_audios else 'No audio available.'
            meanings = data[0]['meanings']
            definitions = []
            types = []
            for meaning in meanings:
                example = meaning['definitions'][0].get('example', 'No example available.')
                print(example)
                definitions.append(f"{meaning['definitions'][0]['definition']}")
                types.append(f"{meaning['partOfSpeech']}")
                # print(definitions)

            return phonetic_texts, types, definitions
        else:
            return ["No phonetic."], ["No type found."], ["No definition found."]
    else:
        return ["Error"], ["Error"], ["Error: Unable to retrieve definition."]

# pass phonetic to get audio
def get_audio_base64(text):
    if not text:
        raise ValueError("The text input is empty")

    tts = gTTS(text)

    # Create a temporary file for the audio
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    temp_audio_name = temp_audio.name
    tts.save(temp_audio_name)
    temp_audio.close()

    # Read the file and encode it in base64
    with open(temp_audio_name, "rb") as audio_file:
        audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')

    # Remove the temporary file
    os.remove(temp_audio_name)

    return audio_base64

#Keywords extraction using NLP spacy
nlp = spacy.load("en_core_web_sm")
def get_keywords(paragraph):
    # https://www.geeksforgeeks.org/keyword-extraction-methods-in-nlp/
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN']  # Only considering proper nouns, adjectives, and nouns
    doc = nlp(paragraph.lower())  # Process the paragraph
    for token in doc:
        if token.text in nlp.Defaults.stop_words or token.text in punctuation:
            continue
        if token.pos_ in pos_tag:
            result.append(token.text)
    return result

'''def create_folder(folder_name):
    if os.path.exists(folder_name):
        return False
    else:
        df = pd.DataFrame(columns=['Word', 'Type', 'Translation', 'Definition'])
        df.to_excel(folder_name, index=False)
        return True
    
def delete_folder(folder_name):
    if os.path.exists(folder_name):
        os.remove(folder_name)
        return True
    else:
        return False

def rename_folder(folder_name, folder_rename):
    if os.path.exists(folder_name):
        os.rename(folder_name, folder_rename)
        return True
    else:
        return False
'''

def dest_language_code(dest_language):
    language_name_to_code = {
        'Afrikaans': 'af',
        'Albanian': 'sq',
        'Amharic': 'am',
        'Arabic': 'ar',
        'Armenian': 'hy',
        'Azerbaijani': 'az',
        'Basque': 'eu',
        'Belarusian': 'be',
        'Bengali': 'bn',
        'Bosnian': 'bs',
        'Bulgarian': 'bg',
        'Catalan': 'ca',
        'Cebuano': 'ceb',
        'Chinese': 'zh',
        'Corsican': 'co',
        'Croatian': 'hr',
        'Czech': 'cs',
        'Danish': 'da',
        'Dutch': 'nl',
        'English': 'en',
        'Esperanto': 'eo',
        'Estonian': 'et',
        'Finnish': 'fi',
        'French': 'fr',
        'Frisian': 'fy',
        'Galician': 'gl',
        'Georgian': 'ka',
        'German': 'de',
        'Greek': 'el',
        'Gujarati': 'gu',
        'Haitian Creole': 'ht',
        'Hausa': 'ha',
        'Hawaiian': 'haw',
        'Hebrew': 'he',
        'Hindi': 'hi',
        'Hmong': 'hmn',
        'Hungarian': 'hu',
        'Icelandic': 'is',
        'Igbo': 'ig',
        'Indonesian': 'id',
        'Irish': 'ga',
        'Italian': 'it',
        'Japanese': 'ja',
        'Javanese': 'jw',
        'Kannada': 'kn',
        'Kazakh': 'kk',
        'Khmer': 'km',
        'Kinyarwanda': 'rw',
        'Korean': 'ko',
        'Kurdish (Kurmanji)': 'ku',
        'Kyrgyz': 'ky',
        'Lao': 'lo',
        'Latin': 'la',
        'Latvian': 'lv',
        'Lithuanian': 'lt',
        'Luxembourgish': 'lb',
        'Macedonian': 'mk',
        'Malagasy': 'mg',
        'Malay': 'ms',
        'Malayalam': 'ml',
        'Maltese': 'mt',
        'Maori': 'mi',
        'Marathi': 'mr',
        'Mongolian': 'mn',
        'Myanmar (Burmese)': 'my',
        'Nepali': 'ne',
        'Norwegian': 'no',
        'Nyanja (Chichewa)': 'ny',
        'Odia (Oriya)': 'or',
        'Pashto': 'ps',
        'Persian': 'fa',
        'Polish': 'pl',
        'Portuguese': 'pt',
        'Punjabi': 'pa',
        'Romanian': 'ro',
        'Russian': 'ru',
        'Samoan': 'sm',
        'Scots Gaelic': 'gd',
        'Serbian': 'sr',
        'Sesotho': 'st',
        'Shona': 'sn',
        'Sindhi': 'sd',
        'Sinhala': 'si',
        'Slovak': 'sk',
        'Slovenian': 'sl',
        'Somali': 'so',
        'Spanish': 'es',
        'Sundanese': 'su',
        'Swahili': 'sw',
        'Swedish': 'sv',
        'Tajik': 'tg',
        'Tamil': 'ta',
        'Tatar': 'tt',
        'Telugu': 'te',
        'Thai': 'th',
        'Turkish': 'tr',
        'Turkmen': 'tk',
        'Ukrainian': 'uk',
        'Urdu': 'ur',
        'Uyghur': 'ug',
        'Uzbek': 'uz',
        'Vietnamese': 'vi',
        'Welsh': 'cy',
        'Xhosa': 'xh',
        'Yiddish': 'yi',
        'Yoruba': 'yo',
        'Zulu': 'zu'
    }

    language_code = language_name_to_code.get(dest_language)
    return language_code


@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/folder')
def folder():
    return render_template('folder.html')

@app.route('/definition.html')
def definition():
    return render_template('definition.html', zip=zip)

# paragraph button
@app.route('/process_paragraph', methods=['POST'])
def process_paragraph():
    data = request.get_json()
    paragraph = data.get('paragraph', '')
    formatted_paragraph = paragraph.replace('  ', '<br><br>')

    audio_base64 = get_audio_base64(paragraph)

    #spacy
    output = get_keywords(paragraph)
    most_common_list = Counter(output).most_common(10)
    
    # turn tuple to list of words
    keywords = [word for word, count in most_common_list]
    print(keywords)

    '''global dest_language
    keyword_data = []
    for keyword in keywords:
        query = keyword.capitalize()
        phonetic, types, definitions = get_word_definition(query)
        word_translation = [translate_text(query, dest_language)]  # Example language code
        defi_translations = [translate_text(defn, dest_language) for defn in definitions]
        audio_base64 = get_audio_base64(query)

        keyword_data.append({
            'query': query,
            'phonetic': phonetic,
            'phonetic_audio': audio_base64,
            'definitions': definitions,
            'word_translation': word_translation,
            'defi_translations': defi_translations,
            'types': types
        })'''
    # keywords = list of most repeted word, keyword_data=dictionary for definitions
    return render_template('paragraph.html', keywords=keywords, paragraph=formatted_paragraph, paragraph_audio=audio_base64)

# Dummy dictionary for word definitions
definitions = {
    "example": "a representative form or pattern",
    "flask": "a small, flat container for liquor",
    "python": "a large, heavy-bodied snake",
    # Add more definitions as needed
}

@app.route('/get_definition', methods=['POST'])
def get_definition():
    data = request.get_json()
    word = data.get('word', '').lower()
    definition = definitions.get(word, 'Definition not found.')
    return jsonify(definition=definition)

# search button
@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    query = data.get('query')
    query = query.capitalize()

    global dest_language
    language_code = dest_language_code(dest_language)
    phonetic, types, definitions = get_word_definition(query)
    word_translation = [translate_text(query, dest_language)]

    defi_translations = [translate_text(defn, dest_language) for defn in definitions]
    
    # Get the base64 encoded audio
    audio_base64 = get_audio_base64(query)

    # Return the template response
    return render_template('definition.html', 
                           query=query, 
                           phonetic=phonetic, 
                           phonetic_audio=audio_base64, 
                           types=types, 
                           definitions=definitions, 
                           word_translation=word_translation, 
                           defi_translations=defi_translations, 
                           zip=zip)


if __name__ == '__main__':
    app.run(debug=True)

'''if __name__ == "__main__":
    for i in range(2):
        main()'''

