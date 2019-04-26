import requests

def get_movie_scores(browser):
    """Return all movie scores on the page"""
    sel = "div.mb-movies div.mb-movie div.movie_info a div"
    scores = browser.find_elements_by_css_selector(sel)
    return scores

def get_all_titles(browser):
    """Return a movie's title"""
    sel = "div.mb-movies div.mb-movie h3.movieTitle"
    title = browser.find_elements_by_css_selector(sel)
    return title