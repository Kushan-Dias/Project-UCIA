# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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