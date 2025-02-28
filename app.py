import os

from flask import Flask, request, render_template
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
from bs4 import BeautifulSoup

# Create flask app
app = Flask(__name__)

# Get index page
@app.route('/')
def index():
    return render_template('index.html')

# Search google
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '')
    return google_search(query)

# Crawl google search
def google_search(query):
    page = browser.new_page()
    stealth_sync(page)
    page.goto('http://google.com/')

    page.type('textarea', query)
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    page.wait_for_load_state("domcontentloaded")

    soup = BeautifulSoup(page.content(), 'html.parser')

    output = []
    for result in soup.select('div.g'):
        try:
            title = result.find('h3').text
            link = result.find('a')['href']
            output.append({ 'title': title, 'link': link })
        except Exception as e:
            print(f'Error - {e}')
        
    page.close()
    return output

# Create browser
def get_browser():
    if os.getenv('HEADLESS', 'True') == 'True':
        return playwright.firefox.launch(headless=True)
    else:
        return playwright.chromium.launch(headless=False)
    
playwright = sync_playwright().start()
browser = get_browser()

# Run app
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5394, threaded=False, use_reloader=False)
    finally:
        browser.close()
        playwright.stop()