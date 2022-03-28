
from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict

ALLOWED_level_of_study = [
    "foundation",
    "undergraduate",
    "postgraduate",
    "under",
    "post",
    "found",
    "u",
    "p",
    "f"
]


LEVEL_OF_STUDIES = ["foundation", "undergraduate", "postgraduate"]
LEVEL_TYPES = ["foundation courses", "undergraduate courses", "postgraduate courses"]
UNDERGRADUATE_COURSES = ["computer science", "software engineering", "artificial intelligence","business information systems", "business management", "business data analytics"]
POSTGRADUATE_COURSES = ["advanced software engineering", "cyber security and forensics","big data analytics", "information technology"]
ALLOWED_course_name = ["computer science", "software engineering", "artificial intelligence", "cyber security", "Information technology", "big data analytics", "cs", "se", "ai", "it"]


ALLOWED_contact_detail = [
    "telephone number",
    "number",
    "email",
    "email address",
    "phone number",
    "contact details",
    "contact",
    "contact info"
]

ALLOWED_date_time = [
    "date",
    "time"
]

ALLOWED_contact_registrar = [
    "telephone number",
    "number",
    "email",
    "email address",
    "phone number",
    "contact details",
    "contact",
    "contact info"
]

email_list = ["email", "email address"]

phone_list = ["telephone number", "number", "phone number"]





class ValidateContactDetailForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_contact_detail_form"

    def validate_contact_detail(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `contact_detail` value."""

        if slot_value.lower() not in ALLOWED_contact_detail:
            dispatcher.utter_message(text=f"Sorry it was not clear.. Please spell the words correctly")
            return {"contact_detail": None}
        dispatcher.utter_message(text=f"OK! You want to know about {slot_value} .")

        if slot_value.lower() in email_list:
            dispatcher.utter_message(text=f"General Email: info@iit.ac.lk\n International Email: international@iit.ac.lk")
        elif slot_value.lower() in phone_list:
            dispatcher.utter_message(text=f"Phone: +94766760760")
        else:
            dispatcher.utter_message(text=f"Phone: +94766760760\n General Email: info@iit.ac.lk\n International Email: international@iit.ac.lk")
        
        return {"contact_detail": slot_value}





class ValidateDateTimeForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_date_time_form"

    def validate_date_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `date_time` value."""

        if slot_value.lower() not in ALLOWED_date_time:
            dispatcher.utter_message(text=f"Sorry it was not clear.. Please spell the words correctly")
            return {"date_time": None}
        dispatcher.utter_message(text=f"OK! You want to know about {slot_value} .")

        if slot_value.lower() == "time":
            dispatcher.utter_message(text=f"Time is")
       
        else:
            dispatcher.utter_message(text=f"date is")
        
        return {"date_time": slot_value}

class AskForLevelOfStudyAction(Action):
    
    def name(self) -> Text:
        return "action_ask_level_of_study"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
                text=f"What kind of pizza do you want?",
                buttons=[{"title": p, "payload": p} for p in LEVEL_OF_STUDIES],
            )
           
       
        return []


class ValidateSimpleDegreeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_degree_program_form"

    def validate_level_of_study(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `level_of_study` value."""
        if slot_value.lower() == "foundation":
            dispatcher.utter_message(
                text="I'll remember you prefer foundation. Here are the details of foundation course"
            )
     
        elif slot_value.lower() == "undergraduate":
             dispatcher.utter_message(
                text="I'll remember you prefer foundation."
            )
           
       
        elif slot_value.lower() == "postgraduate":
            dispatcher.utter_message(
                text="I'll remember you prefer foundation."
            )
        return {"level_of_study": slot_value}

    def validate_course_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `course_name` value."""
        if slot_value.lower() == "computer science":
            dispatcher.utter_message(
                text="here are the details of computer science"
            )
     
        elif slot_value.lower() == "software engineering":
             dispatcher.utter_message(
                text="here are the details of software engineering"
            )
           
       
        elif slot_value.lower() == "artificial intelligence":
            dispatcher.utter_message(
                text="I'll remember you prefer foundation."
            )
        return {"course_name": slot_value}


class AskforCourse(Action):
    
    def name(self) -> Text:
        return "action_ask_course_name"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
          if tracker.get_slot("level_of_study") == "undergraduate":
            dispatcher.utter_message(
                text=f"Please select the course",
                buttons=[{"title": p, "payload": p} for p in UNDERGRADUATE_COURSES],
            )
          elif tracker.get_slot("level_of_study") == "postgraduate":
            dispatcher.utter_message(
                text=f"Please select the course",
                buttons=[{"title": p, "payload": p} for p in POSTGRADUATE_COURSES],
            )
       
            return []
        

class AskforLevel(Action):
    
    def name(self) -> Text:
        return "action_ask_level_type"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
                text=f"Please select the level of study?",
                buttons=[{"title": p, "payload": p} for p in LEVEL_TYPES],
            )
           
       
        return []


        
        
class ValidateApplyDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_apply_details_form"

    def validate_level_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `level_type` value."""
        if slot_value.lower() == "foundation courses":
            dispatcher.utter_message(
                text="oh foundation"
            )
     
        elif slot_value.lower() == "undergraduate courses":
             dispatcher.utter_message(
                text="I'll remember you prefer foundation."
            )
           
       
        elif slot_value.lower() == "postgraduate courses":
            dispatcher.utter_message(
                text="I'll remember you prefer foundation."
            )
        return {"level_type": slot_value}


class ActionEvents(Action):

    def name(self) -> Text:
        return "action_events"

    def run(
           self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
       ) -> List[EventType]:
           dispatcher.utter_message(
                   text=f"Please select the event to know more",
                   buttons=[{"payload": '/cutting{"content_type": "cutting"}', "title": "Cutting Edge"},
                   {"payload": '/stagecraft{"content_type": "stage craft"}', "title": "Stage Craft"}]
               )


           return []

