# VocabHub

VocabHub is a Flask-based web application that combines natural language processing (NLP), translation, and text-to-speech (TTS) functionalities. The app allows users to input text, process it for key insights, translate it into different languages, and convert it to speech. You can also find the most appeared words within a paragraph to ensure you understand the core words!


## Features
- Text Analysis: Extracts keywords and phrases from the input text using NLP (via spaCy).
- Translation: Translates text into multiple languages using Google Translate API.
- Definition: Finds the definition of a word using the Free Dictionary API.
- Text-to-Speech (TTS): Converts text to speech using Google Text-to-Speech (gTTS).
- File Handling: Ability to download the translated text or the generated speech file.

## Technologies Used
- Python: Core language for backend processing.
- Flask: Web framework used to create the web application.
- spaCy: NLP library used for text analysis.
- Pandas: Used for data manipulation.
- Googletrans: Python wrapper for Google Translate.
- gTTS: Google Text-to-Speech API.
- HTML/CSS + Bootstrap: Frontend technologies for rendering templates.


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/I-am-Jiwoo-Seo/VocabHub.git
cd VocabHub
```

### 2. Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages
Ensure pip is updated, then install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 5. Set Up Flask

Ensure that Flask is set up by exporting the FLASK_APP environment variable.

```bash
export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
```

### 6. Run the Application

The application will be available at http://127.0.0.1:5000/.

```bash
flask run
```



## Usage

- Text Input: Enter the text you want to translate in the provided text box.
- Text Analysis: Submit the text to get key insights like the most frequent words.
- Translation: Select a language and translate the text.
- Text-to-Speech: Convert the translated text to speech and download the audio file.


## File Structure

```csharp
├── app.py                 # Main application file
├── templates/             # HTML templates
│   └── dashboard.html     # Main template
│   └── definition.html    # Translation display template
│   └── paragraph.html     # Keyword Extraction template
│   └── folder.html        # Folder Organising template
├── static/                # Static files (CSS, JS, images)
├── requirements.txt       # List of dependencies
├── README.md              # This README file

```

## Dependencies
The required packages are listed in requirements.txt. Here are the main dependencies:


```plaintext
Flask==2.3.2
pandas==2.2.1
googletrans==4.0.0rc1
spacy==3.7.5
gTTS==2.5.1
```
To install these packages, run:
```bash
pip install -r requirements.txt
```

## Contributing

Feel free to contribute by opening issues, suggesting features, or submitting pull requests. As this is my first deployed application, the code is not the best at the moment, but I am constantly working to improve it!

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.

## Acknowledgments
- Creative Tim for open-source frontend dashboard templates. 

## Support the Project
Thank you so much already for using my projects! If you want to go a step further and support my open source work, buy me a coffee:

<a href="https://www.buymeacoffee.com/jiwooseo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
