# 🔎 Multi-Agent AI Research Assistant

A powerful multi-agent research system built using **LangChain**, **Ollama**, **Tavily Search**, and **Agentic AI workflows**.

This project demonstrates how multiple AI agents can collaborate to perform web research, generate structured reports, and critique their own outputs.

---

# 🚀 Features

## 🤖 Multi-Agent Architecture

The system uses specialized AI agents for different tasks:

### 1. Search Agent

Responsible for:

* Searching the web using Tavily
* Gathering recent and reliable information
* Extracting relevant URLs
* Collecting article snippets

### 2. Reader Agent *(Work in Progress)*

Responsible for:

* Identifying relevant URLs
* Reading full article content
* Extracting detailed information from webpages

### 3. Writer Agent

Responsible for:

* Combining research findings
* Generating professional reports
* Structuring content logically
* Producing detailed analysis

### 4. Critic Agent

Responsible for:

* Evaluating report quality
* Identifying strengths
* Suggesting improvements
* Assigning a quality score

---

# 🏗️ Architecture

```text
User Topic
     │
     ▼
Search Agent
     │
     ▼
Web Search Tool (Tavily)
     │
     ▼
Search Results + URLs
     │
     ▼
Writer Agent
     │
     ▼
Research Report
     │
     ▼
Critic Agent
     │
     ▼
Feedback & Score
```

---

# 🛠️ Tech Stack

### AI & LLM

* LangChain
* Ollama
* Gemma 4

### Search

* Tavily Search API

### Web Scraping

* Requests
* BeautifulSoup
* Playwright (optional)

### Utilities

* Python
* dotenv
* Rich

---

# 📂 Project Structure

```bash
research-assistant/
│
├── main.py
├── agents.py
├── tools.py
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/multi-agent-research-assistant.git

cd multi-agent-research-assistant
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama:

https://ollama.com

Pull the required model:

```bash
ollama pull gemma4:e4b
```

---

## 5. Configure Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_tavily_api_key
```

Get a Tavily API key from:

https://tavily.com

---

# ▶️ Running the Project

Execute:

```bash
python main.py
```

Example:

```python
topic = "The impact of AI on the job market"

search_pipeline(topic)
```

---

# 🔍 Workflow

## Step 1: Search Agent

Uses Tavily to search the web:

```python
search_results = agent.invoke(
    {
        "messages": [
            ("user",
             f"Search the web for recent and reliable information on {topic}")
        ]
    }
)
```

Returns:

* Article titles
* URLs
* Snippets

---

## Step 2: URL Extraction

URLs are automatically extracted:

```python
urls = extract_urls(search_results)
```

Example:

```text
https://www.example.com/article
https://another-source.com/report
```

---

## Step 3: Writer Agent

Generates a structured report using:

* Search results
* URLs
* Retrieved information

Output format:

```text
Introduction

Key Findings

Conclusion

Sources
```

---

## Step 4: Critic Agent

Evaluates the report.

Output format:

```text
Score: 8/10

Strengths:
- Well structured
- Good coverage

Areas to Improve:
- Add more sources
- Include statistics

One line verdict:
Strong report with room for deeper analysis.
```

---

# 📜 Example Output

## Research Report

```text
Introduction

Artificial Intelligence is transforming the global job market...

Key Findings

1. Automation of repetitive tasks
2. Creation of new AI-related roles
3. Increased demand for digital skills

Conclusion

AI will reshape employment rather than simply replace jobs.
```

---

## Critic Review

```text
Score: 9/10

Strengths:
- Comprehensive
- Fact-based

Areas to Improve:
- Include more quantitative evidence

One line verdict:
Excellent report with strong research depth.
```

---

# 🔧 Available Tools

## Web Search Tool

```python
@tool
def web_search(query, max_results=3):
```

Capabilities:

* Searches the web
* Returns reliable sources
* Provides snippets and URLs

---

## Content Fetch Tool

```python
@tool
def fetch_full_content(url):
```

Capabilities:

* Fetches webpage content
* Removes navigation and styling elements
* Extracts readable text

---

# 🔮 Future Improvements

* Full Reader Agent implementation
* Multi-source article synthesis
* Source credibility scoring
* Report export to PDF
* Streamlit user interface
* LangGraph workflow orchestration
* Citation generation
* Multi-model support
* Research memory system

---

# 📚 Learning Concepts Demonstrated

This project demonstrates:

* Agentic AI
* Multi-Agent Systems
* Tool Calling
* LLM Orchestration
* Web Search Integration
* Automated Research Pipelines
* Self-Critiquing AI Systems
* LangChain Agents

---

# 👨‍💻 Author

**Arpit Jain**

B.Tech (CSIT)
KIET Group of Institutions

Areas of Interest:

* Generative AI
* AI Agents
* Agentic Workflows

---

# ⭐ If You Like This Project

Consider giving the repository a star and contributing to future improvements.

Happy Researching! 🚀
