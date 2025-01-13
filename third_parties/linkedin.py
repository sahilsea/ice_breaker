#Scraping info from linkedn for profile information

import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrapes information from Linkedin profiles,
    Manually scrape the information from Linkedin profiles."""

