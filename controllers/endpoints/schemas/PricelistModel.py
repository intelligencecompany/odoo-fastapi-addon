
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PricelistModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Pricelist Name", description="")
    discount_policy: Any = Field(None, alias="discount_policy", title="Discount Policy", description="")
    activity_user_id: Optional[int] = Field(None, alias="activity_user_id", title="Responsible User", description="")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Next Activity Type", description="")
    currency_id: int = Field(0, alias="currency_id", title="Currency", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    activity_ids: Optional[List[int]] = Field(None, alias="activity_ids", title="Activities", description="")
    message_follower_ids: Optional[List[int]] = Field(None, alias="message_follower_ids", title="Followers", description="")
    message_partner_ids: Optional[List[int]] = Field(None, alias="message_partner_ids", title="Followers (Partners)", description="")
    message_ids: Optional[List[int]] = Field(None, alias="message_ids", title="Messages", description="")
    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    website_message_ids: Optional[List[int]] = Field(None, alias="website_message_ids", title="Website Messages", description="Website communication history")
    country_group_ids: Optional[List[int]] = Field(None, alias="country_group_ids", title="Country Groups", description="")
    item_ids: Optional[List[int]] = Field(None, alias="item_ids", title="Pricelist Rules", description="")
    activity_state: Optional[Any] = Field(None, alias="activity_state", title="Activity State", description="Status based on activities\nOverdue: Due date is already passed\nToday: Activity date is today\nPlanned: Future activities.")
    activity_type_icon: Optional[str] = Field(None, alias="activity_type_icon", title="Activity Type Icon", description="Font awesome icon e.g. fa-tasks")
    activity_date_deadline: Optional[str] = Field(None, alias="activity_date_deadline", title="Next Activity Deadline", description="")
    my_activity_date_deadline: Optional[str] = Field(None, alias="my_activity_date_deadline", title="My Activity Deadline", description="")
    activity_summary: Optional[str] = Field(None, alias="activity_summary", title="Next Activity Summary", description="")
    activity_exception_decoration: Optional[Any] = Field(None, alias="activity_exception_decoration", title="Activity Exception Decoration", description="Type of the exception activity on record.")
    activity_exception_icon: Optional[str] = Field(None, alias="activity_exception_icon", title="Icon", description="Icon to indicate an exception activity.")
    message_is_follower: Optional[bool] = Field(None, alias="message_is_follower", title="Is Follower", description="")
    has_message: Optional[bool] = Field(None, alias="has_message", title="Has Message", description="")
    message_needaction: Optional[bool] = Field(None, alias="message_needaction", title="Action Needed", description="If checked, new messages require your attention.")
    message_needaction_counter: Optional[int] = Field(None, alias="message_needaction_counter", title="Number of Actions", description="Number of messages requiring action")
    message_has_error: Optional[bool] = Field(None, alias="message_has_error", title="Message Delivery error", description="If checked, some messages have a delivery error.")
    message_has_error_counter: Optional[int] = Field(None, alias="message_has_error_counter", title="Number of errors", description="Number of messages with delivery error")
    message_attachment_count: Optional[int] = Field(None, alias="message_attachment_count", title="Attachment Count", description="")
    message_has_sms_error: Optional[bool] = Field(None, alias="message_has_sms_error", title="SMS Delivery error", description="If checked, some messages have a delivery error.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="If unchecked, it will allow you to hide the pricelist without removing it.")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'PricelistModel':
        filtered_item = {}
        schema = PricelistModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PricelistModel']:
        transformed = []
        schema = PricelistModel.model_json_schema()
        
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
