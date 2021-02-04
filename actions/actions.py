from typing import Dict, Text, Any, List, Union, Optional
from rasa_core_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from .connection_postgresql import DataUpdate

"""class ActionNombre (Action):
    def name(self) -> Text:
        #Identificador unico del formulario
        return "action_nombre"

    def run (self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_nombre")
        return [SlotSet('nombre', tracker.latest_message['text'])]

class ActionApellido (Action):
    def name(self)-> Text:
        # Identificador unico del formulario
        return "action_apellido"

    def run (self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_apellido")
        return [SlotSet('apellido', tracker.latest_message['text'])]

class ActionComentario (Action):
    def name(self)-> Text:
        # Identificador unico del formulario
        return "action_comentario"

    def run (self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_comentario")
        return [SlotSet('comentario', tracker.latest_message['text'])]"""

class ActionGuardarDB (Action):
    def name(self)-> Text:
        # Identificador unico del formulario
        return "validate_action_guardar"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        print("Tracker ",tracker)
        DataUpdate(tracker.get_slot("nombre"),
                   tracker.get_slot("apellido"),
                   tracker.get_slot("comentario"))
        dispatcher.utter_message("Gracias por guardar su informacion...")
        return [SlotSet('nombre', None), SlotSet('apellido', None),SlotSet('comentario', None)]