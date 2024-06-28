
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class CalendarEventModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Meeting Subject", description="")
    privacy: Any = Field(None, alias="privacy", title="Privacy", description="People to whom this event will be visible.")
    show_as: Any = Field(None, alias="show_as", title="Show as", description="If the time is shown as 'busy', this event will be visible to other people with either the full         information or simply 'busy' written depending on its privacy. Use this option to let other people know         that you are unavailable during that period of time. \n If the event is shown as 'free', other users know         that you are available during that period of time.")
    start: str = Field("", alias="start", title="Start", description="Start date of an event, without time for full days events")
    stop: str = Field("", alias="stop", title="Stop", description="Stop date of an event, without time for full days events")
    user_id: Optional[int] = Field(None, alias="user_id", title="Organizer", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Scheduled by", description="Partner-related data of the user")
    videocall_channel_id: Optional[int] = Field(None, alias="videocall_channel_id", title="Discuss Channel", description="")
    res_id: Optional[Any] = Field(None, alias="res_id", title="Document ID", description="")
    res_model_id: Optional[int] = Field(None, alias="res_model_id", title="Document Model", description="")
    recurrence_id: Optional[int] = Field(None, alias="recurrence_id", title="Recurrence Rule", description="")
    message_follower_ids: Optional[List[int]] = Field(None, alias="message_follower_ids", title="Followers", description="")
    message_partner_ids: Optional[List[int]] = Field(None, alias="message_partner_ids", title="Followers (Partners)", description="")
    message_ids: Optional[List[int]] = Field(None, alias="message_ids", title="Messages", description="")
    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    website_message_ids: Optional[List[int]] = Field(None, alias="website_message_ids", title="Website Messages", description="Website communication history")
    categ_ids: Optional[List[int]] = Field(None, alias="categ_ids", title="Tags", description="")
    activity_ids: Optional[List[int]] = Field(None, alias="activity_ids", title="Activities", description="")
    attendee_ids: Optional[List[int]] = Field(None, alias="attendee_ids", title="Participant", description="")
    partner_ids: Optional[List[int]] = Field(None, alias="partner_ids", title="Attendees", description="")
    invalid_email_partner_ids: Optional[List[int]] = Field(None, alias="invalid_email_partner_ids", title="Invalid Email Partner", description="")
    alarm_ids: Optional[List[int]] = Field(None, alias="alarm_ids", title="Reminders", description="Notifications sent to all attendees to remind of the meeting.")
    message_is_follower: Optional[bool] = Field(None, alias="message_is_follower", title="Is Follower", description="")
    has_message: Optional[bool] = Field(None, alias="has_message", title="Has Message", description="")
    message_needaction: Optional[bool] = Field(None, alias="message_needaction", title="Action Needed", description="If checked, new messages require your attention.")
    message_needaction_counter: Optional[int] = Field(None, alias="message_needaction_counter", title="Number of Actions", description="Number of messages requiring action")
    message_has_error: Optional[bool] = Field(None, alias="message_has_error", title="Message Delivery error", description="If checked, some messages have a delivery error.")
    message_has_error_counter: Optional[int] = Field(None, alias="message_has_error_counter", title="Number of errors", description="Number of messages with delivery error")
    message_attachment_count: Optional[int] = Field(None, alias="message_attachment_count", title="Attachment Count", description="")
    message_has_sms_error: Optional[bool] = Field(None, alias="message_has_sms_error", title="SMS Delivery error", description="If checked, some messages have a delivery error.")
    description: Optional[Any] = Field(None, alias="description", title="Description", description="")
    location: Optional[str] = Field(None, alias="location", title="Location", description="")
    videocall_location: Optional[str] = Field(None, alias="videocall_location", title="Meeting URL", description="")
    access_token: Optional[str] = Field(None, alias="access_token", title="Invitation Token", description="")
    videocall_source: Optional[Any] = Field(None, alias="videocall_source", title="Videocall Source", description="")
    is_highlighted: Optional[bool] = Field(None, alias="is_highlighted", title="Is the Event Highlighted", description="")
    is_organizer_alone: Optional[bool] = Field(None, alias="is_organizer_alone", title="Is the Organizer Alone", description="Check if the organizer is alone in the event, i.e. if the organizer is the only one that hasn't declined\n        the event (only if the organizer is not the only attendee)")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="If the active field is set to false, it will allow you to hide the event alarm information without removing it.")
    display_time: Optional[str] = Field(None, alias="display_time", title="Event Time", description="")
    allday: Optional[bool] = Field(None, alias="allday", title="All Day", description="")
    start_date: Optional[str] = Field(None, alias="start_date", title="Start Date", description="")
    stop_date: Optional[str] = Field(None, alias="stop_date", title="End Date", description="")
    duration: Optional[Any] = Field(None, alias="duration", title="Duration", description="")
    res_model: Optional[str] = Field(None, alias="res_model", title="Document Model Name", description="")
    res_model_name: Optional[str] = Field(None, alias="res_model_name", title="Model Description", description="")
    current_attendee: Optional[int] = Field(None, alias="current_attendee", title="Current Attendee", description="")
    current_status: Optional[Any] = Field(None, alias="current_status", title="Attending?", description="")
    should_show_status: Optional[bool] = Field(None, alias="should_show_status", title="Should Show Status", description="")
    recurrency: Optional[bool] = Field(None, alias="recurrency", title="Recurrent", description="")
    follow_recurrence: Optional[bool] = Field(None, alias="follow_recurrence", title="Follow Recurrence", description="")
    recurrence_update: Optional[Any] = Field(None, alias="recurrence_update", title="Recurrence Update", description="Choose what to do with other events in the recurrence. Updating All Events is not allowed when dates or time is modified")
    rrule: Optional[str] = Field(None, alias="rrule", title="Recurrent Rule", description="")
    rrule_type_ui: Optional[Any] = Field(None, alias="rrule_type_ui", title="Repeat", description="Let the event automatically repeat at that interval")
    rrule_type: Optional[Any] = Field(None, alias="rrule_type", title="Recurrence", description="Let the event automatically repeat at that interval")
    event_tz: Optional[Any] = Field(None, alias="event_tz", title="Timezone", description="")
    end_type: Optional[Any] = Field(None, alias="end_type", title="Recurrence Termination", description="")
    interval: Optional[int] = Field(None, alias="interval", title="Repeat On", description="Repeat every (Days/Week/Month/Year)")
    count: Optional[int] = Field(None, alias="count", title="Number of Repetitions", description="Repeat x times")
    mon: Optional[bool] = Field(None, alias="mon", title="Mon", description="")
    tue: Optional[bool] = Field(None, alias="tue", title="Tue", description="")
    wed: Optional[bool] = Field(None, alias="wed", title="Wed", description="")
    thu: Optional[bool] = Field(None, alias="thu", title="Thu", description="")
    fri: Optional[bool] = Field(None, alias="fri", title="Fri", description="")
    sat: Optional[bool] = Field(None, alias="sat", title="Sat", description="")
    sun: Optional[bool] = Field(None, alias="sun", title="Sun", description="")
    month_by: Optional[Any] = Field(None, alias="month_by", title="Option", description="")
    day: Optional[int] = Field(None, alias="day", title="Date of month", description="")
    weekday: Optional[Any] = Field(None, alias="weekday", title="Weekday", description="")
    byday: Optional[Any] = Field(None, alias="byday", title="By day", description="")
    until: Optional[str] = Field(None, alias="until", title="Until", description="")
    display_description: Optional[bool] = Field(None, alias="display_description", title="Display Description", description="")
    attendees_count: Optional[int] = Field(None, alias="attendees_count", title="Attendees Count", description="")
    accepted_count: Optional[int] = Field(None, alias="accepted_count", title="Accepted Count", description="")
    declined_count: Optional[int] = Field(None, alias="declined_count", title="Declined Count", description="")
    tentative_count: Optional[int] = Field(None, alias="tentative_count", title="Tentative Count", description="")
    awaiting_count: Optional[int] = Field(None, alias="awaiting_count", title="Awaiting Count", description="")
    user_can_edit: Optional[bool] = Field(None, alias="user_can_edit", title="User Can Edit", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'CalendarEventModel':
        filtered_item = {}
        schema = CalendarEventModel.model_json_schema()

        for key in item.keys():
            value = item[key]
            model_type = 'any'

            if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                model_type = schema['properties'][key]['anyOf'][0]['type']
            elif 'type' in schema['properties'][key]:
                model_type = schema['properties'][key]['type']

            if isinstance(value, list) and model_type != 'array':
                value = value[0] if item[key] else None
            
            if isinstance(value, bool) and model_type == 'string':
                value = ''

            if value is not None:
                filtered_item[key] = value

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CalendarEventModel']:
        transformed = []
        schema = CalendarEventModel.model_json_schema()
        
        for item in data:
            filtered_item = {}

            if len(fields) == 0:
                fields = item.keys()

            for key in fields:
                if key in item:
                    value = item[key]
                    model_type = 'any'

                    if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                        model_type = schema['properties'][key]['anyOf'][0]['type']
                    elif 'type' in schema['properties'][key]:
                        model_type = schema['properties'][key]['type']

                    if isinstance(value, list) and model_type != 'array':
                        value = value[0] if item[key] else None
                    
                    if isinstance(value, bool) and model_type == 'string':
                        value = ''

                    if value is not None:
                        filtered_item[key] = value

            transformed.append(cls(**filtered_item).model_dump(by_alias=True))
        return transformed
