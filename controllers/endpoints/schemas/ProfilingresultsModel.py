
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProfilingresultsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    create_date: Optional[str] = Field(None, title="Creation Date", description="")
    session: Optional[str] = Field(None, title="Session", description="")
    name: Optional[str] = Field(None, title="Description", description="")
    duration: Optional[Any] = Field(None, title="Duration", description="")
    init_stack_trace: Optional[Any] = Field(None, title="Initial stack trace", description="")
    sql: Optional[Any] = Field(None, title="Sql", description="")
    sql_count: Optional[int] = Field(None, title="Queries Count", description="")
    traces_async: Optional[Any] = Field(None, title="Traces Async", description="")
    traces_sync: Optional[Any] = Field(None, title="Traces Sync", description="")
    qweb: Optional[Any] = Field(None, title="Qweb", description="")
    entry_count: Optional[int] = Field(None, title="Entry count", description="")
    speedscope: Optional[Any] = Field(None, title="Speedscope", description="")
    speedscope_url: Optional[Any] = Field(None, title="Open", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

