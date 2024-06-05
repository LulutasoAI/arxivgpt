import requests
from bs4 import BeautifulSoup

def get_links(query):
    # Use Bing Search
    query = query.replace(" ","%20")
    url = f"https://www.bing.com/search?q={query}"
    print(url)
    # Send a GET request
    response = requests.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the search result entries
    search_results = soup.find_all('li', class_='b_algo')

    # Extract the URLs of the search results
    links = [result.find('a')['href'] for result in search_results]
    return links

def link_to_content(link):
    # Send a GET request to the link
    response = requests.get(link)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and return the text of the page
    content = soup.get_text()
    return content

def gather_info(query):
    # Get the links from the search results
    #print(query, "query")
    links = get_links(query)
    #print(links, "links")

    # Extract the content from each link
    contents = [link_to_content(link) for link in links]
    #print(contents)

    # Join the contents into one string 
    info = ' '.join(contents[:min(len(contents),2)])
    info.replace("\n","")
    #print(info)
    return info

if __name__ == "__main__":
    # Example usage:
    query = "world economy"
    info = gather_info(query)
    print(info)
