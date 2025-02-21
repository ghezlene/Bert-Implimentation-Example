# Hugging Face API Implementation

This is a simple project that implements the Hugging Face library using Python, specifically utilizing the BERT algorithm for natural language processing tasks. The project includes:

- A Python backend that interacts with the Hugging Face API
- A frontend built with HTML
- An SVG image (logo of ISG Tunis)

## Features

- Uses the BERT algorithm for NLP tasks such as text classification, sentiment analysis, or named entity recognition
- Calls Hugging Face API to process data
- Displays results on a simple web interface

## Installation

### Prerequisites

- Python 3.x installed
- `pip` package manager

### Clone the Repository

```bash
git clone https://github.com/ghezlene/Bert-Implimentation-Example.git
cd Bert-Implimentation-Example
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Backend

```bash
uvicorn app:app --reload
```

### Open the Frontend

```bash
python -m http.server 8001
```

## Project Structure

```
📂 Bert-Implimentation-Example
├── 📄 app.py          # Python backend file (FastAPI)
├── 📄 index.html      # Frontend HTML file
├── 📄 requirements.txt # Dependencies
├── 🖼️ logo.svg       # SVG logo of ISG Tunis
└── 📄 README.md       # Documentation
```

 
## License

This project is licensed under the MIT License.

## Author

[Ghezlene El Hajoui](https://github.com/ghezlene)

