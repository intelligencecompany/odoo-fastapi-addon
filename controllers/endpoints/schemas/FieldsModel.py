
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class FieldsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Field Name", description="")
    model: str = Field("", alias="model", title="Model Name", description="The technical name of the model this field belongs to")
    field_description: str = Field("", alias="field_description", title="Field Label", description="")
    ttype: Any = Field(None, alias="ttype", title="Field Type", description="")
    state: Any = Field(None, alias="state", title="Type", description="")
    relation_field_id: Optional[int] = Field(None, alias="relation_field_id", title="Relation field", description="")
    x_model_id: int = Field(0, alias="x_model_id", title="Model", description="The model this field belongs to")
    related_field_id: Optional[int] = Field(None, alias="related_field_id", title="Related field", description="")
    selection_ids: Optional[List[int]] = Field(None, alias="selection_ids", title="Selection Options", description="")
    complete_name: Optional[str] = Field(None, alias="complete_name", title="Complete Name", description="")
    relation: Optional[str] = Field(None, alias="relation", title="Related Model", description="For relationship fields, the technical name of the target model")
    relation_field: Optional[str] = Field(None, alias="relation_field", title="Relation Field", description="For one2many fields, the field on the target model that implement the opposite many2one relationship")
    help: Optional[Any] = Field(None, alias="help", title="Field Help", description="")
    selection: Optional[str] = Field(None, alias="selection", title="Selection Options (Deprecated)", description="")
    copied: Optional[bool] = Field(None, alias="copied", title="Copied", description="Whether the value is copied when duplicating a record.")
    related: Optional[str] = Field(None, alias="related", title="Related Field", description="The corresponding related field, if any. This must be a dot-separated list of field names.")
    required: Optional[bool] = Field(None, alias="required", title="Required", description="")
    readonly: Optional[bool] = Field(None, alias="readonly", title="Readonly", description="")
    index: Optional[bool] = Field(None, alias="index", title="Indexed", description="")
    translate: Optional[bool] = Field(None, alias="translate", title="Translatable", description="Whether values for this field can be translated (enables the translation mechanism for that field)")
    size: Optional[int] = Field(None, alias="size", title="Size", description="")
    on_delete: Optional[Any] = Field(None, alias="on_delete", title="On Delete", description="On delete property for many2one fields")
    domain: Optional[str] = Field(None, alias="domain", title="Domain", description="The optional domain to restrict possible values for relationship fields, specified as a Python expression defining a list of triplets. For example: [('color','=','red')]")
    groups: Optional[List[int]] = Field(None, alias="groups", title="Groups", description="")
    group_expand: Optional[bool] = Field(None, alias="group_expand", title="Expand Groups", description="If checked, all the records of the target model will be included\nin a grouped result (e.g. 'Group By' filters, Kanban columns, etc.).\nNote that it can significantly reduce performance if the target model\nof the field contains a lot of records; usually used on models with\nfew records (e.g. Stages, Job Positions, Event Types, etc.).")
    selectable: Optional[bool] = Field(None, alias="selectable", title="Selectable", description="")
    modules: Optional[str] = Field(None, alias="modules", title="In Apps", description="List of modules in which the field is defined")
    relation_table: Optional[str] = Field(None, alias="relation_table", title="Relation Table", description="Used for custom many2many fields to define a custom relation table name")
    column1: Optional[str] = Field(None, alias="column1", title="Column 1", description="Column referring to the record in the model table")
    column2: Optional[str] = Field(None, alias="column2", title="Column 2", description="Column referring to the record in the comodel table")
    compute: Optional[Any] = Field(None, alias="compute", title="Compute", description="Code to compute the value of the field.\nIterate on the recordset 'self' and assign the field's value:\n\n    for record in self:\n        record['size'] = len(record.name)\n\nModules time, datetime, dateutil are available.")
    depends: Optional[str] = Field(None, alias="depends", title="Dependencies", description="Dependencies of compute method; a list of comma-separated field names, like\n\n    name, partner_id.name")
    store: Optional[bool] = Field(None, alias="store", title="Stored", description="Whether the value is stored in the database.")
    currency_field: Optional[str] = Field(None, alias="currency_field", title="Currency field", description="Name of the Many2one field holding the res.currency")
    sanitize: Optional[bool] = Field(None, alias="sanitize", title="Sanitize HTML", description="")
    sanitize_overridable: Optional[bool] = Field(None, alias="sanitize_overridable", title="Sanitize HTML overridable", description="")
    sanitize_tags: Optional[bool] = Field(None, alias="sanitize_tags", title="Sanitize HTML Tags", description="")
    sanitize_attributes: Optional[bool] = Field(None, alias="sanitize_attributes", title="Sanitize HTML Attributes", description="")
    sanitize_style: Optional[bool] = Field(None, alias="sanitize_style", title="Sanitize HTML Style", description="")
    sanitize_form: Optional[bool] = Field(None, alias="sanitize_form", title="Sanitize HTML Form", description="")
    strip_style: Optional[bool] = Field(None, alias="strip_style", title="Strip Style Attribute", description="")
    strip_classes: Optional[bool] = Field(None, alias="strip_classes", title="Strip Class Attribute", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    tracking: Optional[int] = Field(None, alias="tracking", title="Enable Ordered Tracking", description="If set every modification done to this field is tracked. Value is used to order tracking values.")
    website_form_blacklisted: Optional[bool] = Field(None, alias="website_form_blacklisted", title="Blacklisted in web forms", description="Blacklist this field for web forms")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'FieldsModel':
        filtered_item = {}
        schema = FieldsModel.model_json_schema()

        for key in item:
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['FieldsModel']:
        transformed = []
        schema = FieldsModel.model_json_schema()
        
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
