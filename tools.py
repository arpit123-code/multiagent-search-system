from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
from playwright.sync_api import sync_playwright
load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# ALLOWED_DOMAINS = ["economictimes.indiatimes.com"]

# def correct_domain(url:str) ->bool:
#     return any(domin in url for domin in ALLOWED_DOMAINS)

@tool
def web_search(query:str ,max_results:int=3) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets.
        
    """
    results=tavily.search(query=query,max_results=max_results)
    out=[]
    for res in results['results']:
        # url=res['url']
        # if not correct_domain(url):
        #     continue

        #for res in results['results']:
        out.append(f"TITLE: {res['title']}\nURL: {res['url']}\n SNIPPET: {res['content'][:300]}\n") 

    # if not out:
    #     return "No Economic Times results found."

    


    # for res in results['results']:
    #     out.append(f"Title: {res['title']}\nUrl: {res['url']}\n Snippet: {res['content'][:300]}\n")

    return "\n-----\n".join(out)

#print (web_search.invoke({"query": "What is the latest news on AI?"}))





# def web_scrape_js(url: str) -> str:
#     """Scrape and return clean text content from a given URL for deeper reading.
#         Uses Playwright to handle JavaScript-rendered content, ensuring we get the full text.
#     """
#     try:
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=True)

#             context = browser.new_context(
#                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
#                 locale="en-US"
#             )

#             page = context.new_page()

#             # ✅ Increase timeout
#             page.goto(url, timeout=60000, wait_until="domcontentloaded")

#             # ✅ Wait for body instead of networkidle
#             page.wait_for_selector("body", timeout=10000)

#             html = page.content()
#             browser.close()

#         soup = BeautifulSoup(html, "html.parser")

#         # Remove noise
#         for e in soup(['script','style','nav','footer','header','aside']):
#             e.decompose()

#         # Focus on article
#         article = soup.find("article")
#         text = article.get_text(" ", strip=True) if article else soup.get_text(" ", strip=True)

#         if len(text) < 300:
#             return "Content not properly extracted (JS-heavy or blocked)."

#         return text[:3000]

#     except Exception as e:
#         return f"Error: {e}"
    
@tool
def fetch_full_content(url):
    """Scrape and return clean text content from a given URL for deeper reading.
    Uses Playwright to handle JavaScript-rendered content, ensuring we get the full text.
#    """
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for e in soup(['script','style','nav','footer','header','aside']):
            e.decompose()
        return soup.get_text()[:1000]
    except:
        return "Could not fetch content"
    

#print (fetch_full_content(" https://enterpriseai.economictimes.indiatimes.com/news/industry"))