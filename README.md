# AI-Marketing-Crew

An AI-powered, agentic marketing team built with **CrewAI**.  
This Crew includes agents with roles like Head of Marketing, Content Creators, Content Writer, and SEO Specialist, capable of tasks such as market research, content drafting, SEO optimization, and strategy framing—all orchestrated within a Streamlit interface or standalone script.

---

##  Project Structure

```TEXT
├── app.py # Streamlit-based UI to run the Crew interactively
├── crew.py # Defines the TheMarketingCrew class, agents, and tasks
├── config/
│ ├── agents.yaml # Agent configurations (roles, goals, etc.)
│ └── tasks.yaml # Task configurations (descriptions, expectations)
├── resources/
│ └── drafts/
│ └── blogs/ # Used by DirectoryReadTool/FileWriterTool
├── requirements.txt # Python dependencies.
```


---

## 🔧 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/vikranth007/AI-Marketing-Crew.git
   cd AI-Marketing-Crew
   ```
2. **Create and activate a virtual environment (recommended)**
   ```
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
     ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set environment variables**

   Create a `.env` file in the project root:
   ```bash
    GEMINI_API_KEY=your_gemini_key_here
    SERPER_API_KEY=your_serper_key_here   # optional for web search tools

   ```
5. **Ensure required directories exist**
   ```bash
     mkdir -p resources/drafts/blogs
   ```
---
### 🎯 Usage

  **Run Through Streamlit UI**
    
      streamlit run app.py
**Then open in your browser: http://localhost:8501**

  You’ll see input fields for:

  - Gemini API key (or read from `.env`)
  
  - Optional Serper API key
  
  - Product details (name, audience, description, budget)
  
  - A Run Marketing Crew button
  
  The Crew will then run and display results in structured output.

## ⚙️ Configuration Notes

  - `config/agents.yaml` → defines each agent (roles/goals)

  -  `config/tasks.yaml` → defines the marketing tasks (research, blogs, SEO, etc.)

  -  Agent/task keys must match `crew.py` definitions.

  -  Tools like Serper are optional (used only if you set `SERPER_API_KEY`).

## 🤝 Contributing

  - Add new agents or tasks by editing YAML files and extending methods in `crew.py`.

  -  Improve Streamlit UI, add logging, or integrate external APIs.

  -  Contributions and suggestions are welcome!

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.
