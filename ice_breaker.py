from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

information = """
Elon Reeve Musk (born June 28, 1971) is a business magnate, industrial designer, and engineer. He is the founder, CEO, and chief engineer of SpaceX; angel investor, CEO, and product architect of Tesla, Inc.; owner and CEO of X (formerly Twitter); owner of The Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation.
Key aspects of his life and career often highlighted in his Wikipedia entry (and general public knowledge) include:

	•	Early Life and Education: Born in South Africa, Musk showed an early aptitude for computers and programming. He emigrated to Canada and later attended the University of Pennsylvania, where he earned degrees in physics and economics.
	•	Entrepreneurial Ventures:
	▪	Zip2:  An early web software company that provided business directories and mapping services to online newspapers.
	▪	X.com and PayPal:  Musk co-founded X.com, an online financial services and email payment company, which later merged with Confinity to form PayPal.  PayPal was subsequently acquired by eBay.
	▪	SpaceX:  Founded with the goal of reducing space transportation costs and enabling the colonization of Mars. SpaceX has achieved significant milestones in rocketry and space travel.
	▪	Tesla, Inc.:  Joined Tesla Motors (now Tesla, Inc.) as an investor and later became CEO. Tesla designs and manufactures electric vehicles, battery energy storage from home to grid-scale, solar panels and solar roof tiles, and related products and services.
	▪	SolarCity:  Played a key role in the development of SolarCity, a solar energy services company that was later acquired by Tesla.
	▪	The Boring Company:  Founded to develop infrastructure and tunnel-boring technologies.
	▪	Neuralink:  A nurotechnology company developing implantable brain-machine interfaces.
	▪	OpenAI:  Co-founded OpenAI, an artificial intelligence research company, but later resigned from its board.
	▪	X (formerly Twitter): Acquired Twitter in 2022 and rebranded it to X in 2023.
	•	Wealth and Influence: Musk is one of the world’s richest individuals. His business ventures and public pronouncements have made him a highly influential figure in technology, business, and popular culture.
	•	Controversies:  Musk has been involved in several controversies related to his business practices, public statements, and social media activity.  These are often covered extensively in his Wikipedia biography.
	•	Personal Life:  Information about his personal life, including marriages, children, and relationships, is also typically included in his biography.
To get the most up-to-date and detailed information, it’s always best to refer directly to Wikipedia or other reliable biographical sources.  Just search for “Elon Musk Wikipedia.”

"""

if __name__ == "__main__":
    print("Hello Genai!")

    summary_template = """
        given the information {information} about a person from I want to create:
        1. a short summary in one sentence
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )


    llm = ChatGoogleGenerativeAI( model="gemini-1.5-pro")

    formatted_prompt = summary_prompt_template.format(information=information)

    chain = summary_prompt_template | llm
    res = llm.invoke(input=formatted_prompt)

    print(res)
