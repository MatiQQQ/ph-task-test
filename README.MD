
# OpenAI HTML Article Transformer

This project is a Python script that reads content from a text file, transforms the content into a structured HTML article using the OpenAI API, and saves the generated HTML to an output file. It leverages OpenAI's capabilities for content transformation while providing customizable parameters for specifying the system role and user prompt.

## Prerequisites

- Python 3.9 or higher
- `OPENAI_API_KEY` environment variable set up with your OpenAI API key to authenticate requests to the OpenAI API.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate dependencies.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- On **Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

- On **macOS** and **Linux**:

  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

Make sure you have `pip` installed, then install the necessary dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Ensure you have the `OPENAI_API_KEY` environment variable set up. You can do this by exporting it in your terminal session:

- On **Windows** (Command Prompt):

  ```cmd
  set OPENAI_API_KEY=your_openai_api_key
  ```

- On **macOS** and **Linux**:

  ```bash
  export OPENAI_API_KEY=your_openai_api_key
  ```

## Usage

1. Place the input text file (e.g., `plik.txt`) in the same directory as the script or specify the path to your input file.
2. Run the script by executing the following command:

```bash
python script.py
```

### Script Description

The script performs the following tasks:

- **Read Content from a File**: It retrieves text from a specified input file (`plik.txt` by default).
- **Transform Content to HTML**: It uses the OpenAI API to transform the text into structured HTML content based on specified guidelines and parameters. This includes appropriate tagging, image placeholders, and more.
- **Save HTML Content**: The transformed HTML content is saved to an output file (`artykul.html`).

## File Structure

- `plik.txt`: Input file containing the text to be transformed.
- `artykul.html`: Output file containing the transformed HTML content.

## Example

Given an input text file `plik.txt`, the script will produce structured HTML content with appropriate tags and placeholders, and write the content to `artykul.html`.

