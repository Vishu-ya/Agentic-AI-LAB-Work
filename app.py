import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import create_agent

# Load environment variables from .env file
load_dotenv()

def check_api_key():
    """Checks if Groq API key is set in environment variables."""
    if not os.getenv("GROQ_API_KEY"):
        print("\nError: GROQ_API_KEY is missing!")
        print("Please set it in your environment or a .env file.")
        sys.exit(1)

def get_research_agent():
    """Initializes and returns the LangChain agent graph."""
    
    # Initialize tools
    search = DuckDuckGoSearchRun()
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    
    tools = [
        search,
        wikipedia
    ]
    
    # Initialize LLM
    llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)
    
    # Initialize agent graph
    agent = create_agent(llm, tools=tools)
    
    return agent

def save_report(topic, report_content):
    """Saves the generated report to a text file in the sample_outputs directory."""
    # Create directory if it doesn't exist
    if not os.path.exists("sample_outputs"):
        os.makedirs("sample_outputs")
    
    # Clean filename
    filename = f"sample_outputs/{topic.lower().replace(' ', '_')}_report.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"\nReport saved successfully to: {filename}")

def generate_report(topic):
    """Orchestrates the research and report generation process."""
    agent = get_research_agent()
    
    # Define the strict output format
    prompt = f"""
    Conduct a thorough research on the following topic: '{topic}'
    
    Search for relevant information, extract key insights, and organize the content.
    
    STRICT OUTPUT FORMAT:
    The generated report must include the following sections exactly:
    
    1. Cover Page
    2. Title: [Your Title Here]
    3. Introduction
    4. Key Findings (bullet points)
    5. Challenges
    6. Future Scope
    7. Conclusion
    
    Ensure the report is well-structured, professional, and informative.
    """
    
    print(f"\nStarting research on: {topic}...")
    try:
        # Use invoke for the graph-based agent
        # The result of invoke() on this graph is the final state dictionary
        # We need to extract the response from the last message
        result = agent.invoke({"messages": [("user", prompt)]})
        response = result["messages"][-1].content
        
        save_report(topic, response)
        return response
    except Exception as e:
        print(f"\nAn error occurred during agent execution: {e}")
        return None

def main():
    """Main CLI entry point."""
    check_api_key()
    
    print("="*50)
    print("      Autonomous Research Agent using LangChain")
    print("="*50)
    
    if len(sys.argv) > 1:
        # Use command line argument as topic
        topic = " ".join(sys.argv[1:])
    else:
        # Prompt user for input
        topic = input("\nEnter the research topic: ")
    
    if topic:
        report = generate_report(topic)
        if report:
            print("\n" + "="*50)
            print("GENERATED REPORT:")
            print("="*50)
            print(report)
            print("="*50)
    else:
        print("Topic cannot be empty. Exiting.")

if __name__ == "__main__":
    main()
