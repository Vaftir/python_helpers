import getpass
import os

from modules.config.ConfigHandler import ConfigHandler

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


  """
  Author: Yago Faria
  Date: 2023-10-03
  Description: Essa classe é responsável por gerar 
  o texto do chamado que será enviado para o suporte da Zanthus.
  
  input: str
  output: str
  
  Dependências:
  - langchain
  - dotenv
  - getpass
  - os
  
  
  """


class AssistenteChamado:
  
  
      
  def _prompt(self):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "{prompt}"),
        ("user", "{input}"),
    ])
    return prompt  
  
  def _llm_model(self):
    llm = ChatOpenAI(
        model=self.model, 
        temperature=self.temperature,
        openai_api_key=self.api_key,
        max_tokens=self.max_tokens
    )
    return llm
  
  def _chain(self):
    chain = self.prompt | self.llm | self.parser
    return chain
  
  
  def __init__(self, config_path = 'config/config.json'):
    self.config = ConfigHandler(config_path).load_config()
    self.api_key = self.config['api_keys']['OPENAI_API_KEY']
    self.model = self.config['model']['model']
    self.temperature = self.config['model']['temperature']
    self.max_tokens = self.config['model']['max_tokens']
    self.prompt_template = self.config['model']['prompt']
    self.prompt = self._prompt()
    self.llm = self._llm_model()
    self.parser = StrOutputParser()
    self.chain = self._chain()
    
    
  def gerar_texto_chamado(self, input_text):
    resultado = self.chain.invoke({
        "prompt": self.prompt_template,
        "input": input_text
    })
    return resultado
    


    """
    if __name__ == "__main__":
    openai = AssistenteChamado()
    resultado = openai.gerar_texto_chamado("O serviço mirage não está funcionando corretamente, já tentei reiniciá-lo e não funcionou. O que eu faço?")
    print(resultado)
    
    """
    
    

    
  
    
  
  
    

   