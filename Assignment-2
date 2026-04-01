# Autonomous Research Agent using LangChain

This project is a powerful AI research agent built using Python and LangChain. It can autonomously search the web, analyze information, and generate a structured research report on any given topic.

## Features
- **Web Search Tool**: Uses DuckDuckGo to search for real-time information.
- **Knowledge Tool**: Uses Wikipedia for background information and factual data.
- **ReAct Agent**: Utilizes LangChain's Zero-Shot ReAct Agent for decision making.
- **Structured Reports**: Generates professional research reports with clear sections.
- **Automated Saving**: Automatically saves the research report as a text file in the `sample_outputs/` directory.

## Prerequisites
- Python 3.8+
- Groq API Key (Free tier available)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Autonomous-Research-Agent.git
   cd Autonomous-Research-Agent
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your API key:
   - Create a `.env` file in the project root.
   - Obtain a free API key from [Groq Console](https://console.groq.com/keys).
   - Add the following to your `.env`:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage
### CLI Interface
Run the agent from the command line:
```bash
python app.py
```
Then, enter your desired research topic when prompted.

### Command Line Arguments
Alternatively, you can provide the topic directly as a command-line argument:
```bash
python app.py "Impact of AI in Healthcare"
```

## Project Structure
- `app.py`: Main entry point for the agent.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.
- `sample_outputs/`: Directory where generated reports are saved.

## Output Format
Each generated report follows a strict structure:
1. Cover Page
2. Title
3. Introduction
4. Key Findings (bullet points)
5. Challenges
6. Future Scope
7. Conclusion

## Example Usage
- **Topic**: "Impact of AI in Healthcare"
- **Topic**: "Blockchain in Supply Chain"

## License
This project is open-source and available under the MIT License.
