import requests

def get_theater_title(browser,id):
    """Return the theater title text"""
    sel = "li[data-theater-id=" + id + "] a.light"
    title = browser.find_element_by_css_selector(sel)
    return title.text

def get_theater_ids(browser):
    """Return the theater ids"""
    sel = "li.fd-theater"
    titles = browser.find_elements_by_css_selector(sel)
    return [t.get_attribute('data-theater-id') for t in titles]

def get_movie_titles(browser,theaters):
    """Return the movie title text"""
    movies = {}
    for id in theaters:
        sel = "li[data-theater-id=" + id + "] a.dark"
        titles = browser.find_elements_by_css_selector(sel)
        titles_text = [t.text for t in titles]
        sel2 = "li[data-theater-id=" + id + "] a.dark, li[data-theater-id=" + id + "] a.btn.showtime-btn.showtime-btn--available"
        movies_and_times = browser.find_elements_by_css_selector(sel2)
        movie_times = {}
        times = []
        for m in movies_and_times:
                if m.text in titles_text:
                        if len(movies) > 0:
                              movie_times[m.text] = times  
                        times = [] 
                times.append(m.text)
        #movies[get_theater_title(browser,id)] = [{'title': m,'times': t} for m,t in zip(movie_times)]       
    return [t.text for t in movies_and_times]

def get_next(browser):
    """Go to the next title"""
    #nav_buttons = browser.find_elements_by_css_selector(sel)
    #prev_button = nav_buttons[1]
    prev_button = browser.find_element_by_link_text("< Prev")
    prev_button.click()

def scrape_image(img, filename):
    """Save an image element as filename"""
    response = requests.get(img.get_attribute('src'))
    img_data = response.content
    with open(filename, 'wb') as f:
        f.write(img_data)

def find_image(browser):
    """Return the image element of the xkcd page."""
    sel = "div#comic img"
    img = browser.find_element_by_css_selector(sel)
    return img