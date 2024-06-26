
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class RatingParentMixinModel(BaseModel):

    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    rating_percentage_satisfaction: Optional[int] = Field(None, alias="rating_percentage_satisfaction", title="Rating Satisfaction", description="Percentage of happy ratings")
    rating_count: Optional[int] = Field(None, alias="rating_count", title="# Ratings", description="")
    rating_avg: Optional[Any] = Field(None, alias="rating_avg", title="Average Rating", description="")
    rating_avg_percentage: Optional[Any] = Field(None, alias="rating_avg_percentage", title="Average Rating (%)", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'RatingParentMixinModel':
        filtered_item = {}
        schema = RatingParentMixinModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['RatingParentMixinModel']:
        transformed = []
        schema = RatingParentMixinModel.model_json_schema()
        
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
