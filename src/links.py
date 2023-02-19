import dash
from dash import html
import dash_bootstrap_components as dbc

def get_links():
    for page in dash.page_registry.values():
        if page["path"].endswith("/") and pg_name="home":
	    return page["path"]
