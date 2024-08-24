# VocabHub

VocabHub is a Flask-based web application that combines natural language processing (NLP), translation, and text-to-speech (TTS) functionalities. The app allows users to input text, process it for key insights, translate it into different languages, and convert it to speech.


You can also find the most appeared words within a paragraph before proceeding to read to ensure you understand the core words!


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

```bash
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

## Contributing

Pull requests are welcome. As this is my first deployed application, the code is not the best at the moment, but I am willing to improve constantly!

For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
