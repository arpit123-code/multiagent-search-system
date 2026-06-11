from agents import *

#state={}

import re

def extract_urls(text):
    return re.findall(r'https?://\S+', text)

def search_pipeline(topic:str) -> dict:

    state={}

    agent=build_search_agent()
    search_results=agent.invoke({
        "messages":[("user", f"Search the web for recent and reliable information on the topic: {topic}. ")]
    })
    state['search_results']=search_results['messages'][-1].content
    urls = extract_urls(state['search_results'])
    state['urls'] = urls
    print("extracted urls:", urls)
    print('search results:', state['search_results'])

    print ("reader agent is reading the search results...")

    # agent2=build_read_agent()
    # read_results=agent2.invoke({
    #      "messages": [("user",
    #         f"Based on the following search results about '{topic}', "
    #         f"""
    #             Extract the BEST Economic Times URL from the search results below.

    #             Then call the fetch_full_content tool with that URL.

    #             Search Results:
    #             {state['search_results']}
    #             """
    #     )]
    # })

    # state['read_results']=read_results['messages'][-1].content
    # print('read results:', state['read_results'])

    print ("writer agent is writing the report...")

    research_combined=(
        f"Search Results:\n{state['search_results']}\n\n"
        f"URLs:\n" + "\n".join(state['urls']) + "\n\n"
    )

    report=writer_chain.invoke({
        "topic":topic,
        "research":research_combined,
    })

    state['report']=report
    print('final report:', state['report'])

    print ("critic agent is evaluating the report...")

    state['feedback']=critic_chain.invoke({
        "report":state['report'],
    })
    print('report feedback:', state['feedback'])

    return state


if __name__=="__main__":
    topic="The impact of AI on the job market"
    search_pipeline(topic)
    
