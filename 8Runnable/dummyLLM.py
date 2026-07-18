from abc import ABC, abstractmethod 
class Runnable(ABC):
    def invoke(input_data):
        pass
    
import random 
class NakliLLM(Runnable):
    def __init__(self):
        print("LLM Created")
    
    def invoke(self,prompt):
        response_list=["DElhi is the capital of india",
                   'AI stands for artificial inteligence' ]
        return {'response': random.choise(response_list)}
    def predict(self,prompt):
        response_list=["DElhi is the capital of india",
                   'AI stands for artificial inteligence' ]
        return {'response': random.choise(response_list)}



class NakliPromptTemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

template.format({'length': 'short', 'topic': 'india'})

class NakliLLMChain:
    def __init__(self,llm,prompt):
        self.llm=llm
        self.prompt=prompt
    def run(self,input_dict):
        final_prompt=self.prompt.formate(input_dict)
        result=self.llm.predict(final_prompt)
        return result['response']
llm=NakliLLM()
chain=NakliLLMChain(llm,template)
chain.run({'length':'short','topic':'india'})

class RunnableConnection(Runnable):
    def __init(self,runnable_list):
        self.runnable_list=runnable_list
    def invoke(self,input_data):
        for runnable in self.runnable_list:
            runnable.invoke(input_data)
    chain=RunnableConnector([template,llm])
    chain.invoke('length')
            