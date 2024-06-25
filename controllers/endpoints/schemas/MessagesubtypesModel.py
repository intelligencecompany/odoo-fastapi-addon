
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MessagesubtypesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Message Type", description="Message subtype gives a more precise type on the message, especially for system notifications. For example, it can be a notification related to a new record (New), or to a stage change in a process (Stage change). Message subtypes allow to precisely tune the notifications the user want to receive on its wall.")
    parent_id: Optional[int] = Field(None, title="Parent", description="Parent subtype, used for automatic subscription. This field is not correctly named. For example on a project, the parent_id of project subtypes refers to task-related subtypes.")
    description: Optional[Any] = Field(None, title="Description", description="Description that will be added in the message posted for this subtype. If void, the name will be added instead.")
    internal: Optional[bool] = Field(None, title="Internal Only", description="Messages with internal subtypes will be visible only by employees, aka members of base_user group")
    relation_field: Optional[str] = Field(None, title="Relation field", description="Field used to link the related model to the subtype model when using automatic subscription on a related document. The field is used to compute getattr(related_document.relation_field).")
    res_model: Optional[str] = Field(None, title="Model", description="Model the subtype applies to. If False, this subtype applies to all models.")
    default: Optional[bool] = Field(None, title="Default", description="Activated by default when subscribing.")
    sequence: Optional[int] = Field(None, title="Sequence", description="Used to order subtypes.")
    hidden: Optional[bool] = Field(None, title="Hidden", description="Hide the subtype in the follower options")
    track_recipients: Optional[bool] = Field(None, title="Track Recipients", description="Whether to display all the recipients or only the important ones.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

