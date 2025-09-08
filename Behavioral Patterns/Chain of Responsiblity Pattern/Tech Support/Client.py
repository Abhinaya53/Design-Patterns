from ChatBot import ChatBot
from TechSupport import TechSupport
from Supervisor import Supervisor
from Manager import Manager

query = "The app is buffering a lot"
chatbot = ChatBot()
techsupport = TechSupport()
supervisor = Supervisor()
manager = Manager()

supervisor.set_next_handler(manager)
techsupport.set_next_handler(supervisor)
chatbot.set_next_handler(techsupport)

chatbot.handle_query(query) 