from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from typing import Tuple
import os
import sys

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
from output_parsers import person_intel_parser, PersonIntel

information = """

"""
name = "Harrison Chase"
def ice_break(name:str) -> Tuple[PersonIntel, str]:


    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_lookup_agent(name=name)
    print(twitter_username)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=5)
    #scrape_user_tweets(username="Elon Musk", num_tweets=100)


    # Linkedin information {linkedin_information} and
    summary_template = """
         given the Linkedin information {linkedin_information} and twitter {twitter_information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
         3. A topic that may interest them
         4. 2 creative Ice breakers to open a conversation with them
         \n{format_instructions}
     """


    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
        partial_variables = {"format_instructions":person_intel_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")
    # linkedin_data = linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin/in/harrison-chase-961287118/')
    # print(linkedin_data)
    result = chain.run(linkedin_information=linkedin_data, twitter_information=tweets) #linkedin_information=linkedin_data,
    print(result)
    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")

if __name__ == "__main__":

    print("Hello LangChain!")
    ice_break(name="Harrison Chase")