
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityTypeModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    delay_unit: Any = Field(None, title="Delay units", description="Unit of delay")
    delay_from: Any = Field(None, title="Delay Type", description="Type of delay")
    chaining_type: Any = Field(None, title="Chaining Type", description="")
    triggered_next_type_id: Optional[int] = Field(None, title="Trigger", description="Automatically schedule this activity once the current one is marked as done.")
    default_user_id: Optional[int] = Field(None, title="Default User", description="")
    suggested_next_type_ids: Optional[List[int]] = Field(None, title="Suggest", description="Suggest these activities once the current one is marked as done.")
    previous_type_ids: Optional[List[int]] = Field(None, title="Preceding Activities", description="")
    mail_template_ids: Optional[List[int]] = Field(None, title="Email templates", description="")
    summary: Optional[str] = Field(None, title="Default Summary", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    create_uid: Optional[int] = Field(None, title="Create Uid", description="")
    delay_count: Optional[int] = Field(None, title="Schedule", description="Number of days/week/month before executing the action. It allows to plan the action deadline.")
    delay_label: Optional[str] = Field(None, title="Delay Label", description="")
    icon: Optional[str] = Field(None, title="Icon", description="Font awesome icon e.g. fa-tasks")
    decoration_type: Optional[Any] = Field(None, title="Decoration Type", description="Change the background color of the related activities of this type.")
    res_model: Optional[Any] = Field(None, title="Model", description="Specify a model if the activity should be specific to a model and not available when managing activities for other models.")
    category: Optional[Any] = Field(None, title="Action", description="Actions may trigger specific behavior like opening calendar view or automatically mark as done when a document is uploaded")
    default_note: Optional[Any] = Field(None, title="Default Note", description="")
    keep_done: Optional[bool] = Field(None, title="Keep Done", description="Keep activities marked as done in the activity view")
    initial_res_model: Optional[Any] = Field(None, title="Initial model", description="Technical field to keep track of the model at the start of editing to support UX related behaviour")
    res_model_change: Optional[bool] = Field(None, title="Model has change", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

