from pydantic import BaseModel, ConfigDict

class ClubSchema(BaseModel): 
    id: int  
    name: str
    short_name: str
    abbr: str
    stadium_name: str
    stadium_city: str
    stadium_country: str
    stadium_capacity: int

    model_config = ConfigDict(from_attributes=True)

