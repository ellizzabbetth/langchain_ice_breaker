from langchain.serpapi import SerpAPIWrapper
import os


def get_profile_url(text: str) -> str:
    """Searches for Linkedin or twitter Profile Page."""
    serpapi_api_key = os.environ.get("SERPAPI_API_KEY")
    # print("serpapi_api_key",serpapi_api_key)
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    print("res", res)
    return res
