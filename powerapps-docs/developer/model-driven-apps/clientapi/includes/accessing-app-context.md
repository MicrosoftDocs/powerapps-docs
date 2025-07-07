## Accessing app context

When an Agent API is called, context for the app is passed to the MCS topic through a set of variables. The following are context variables:

| Variable | Description |
| --- | --- |
| `Global.PA__Copilot_Model_PageContext.pageContext.id.guid` | ID of the table record on the main form |
| `Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName` | Logical name of the table in the main page |
| `Global.PA__Copilot_Model_PageContext.pageContext.pageName` | Name of the main page |
| `Global.PA__Copilot_Model_PageContext.pageContext.pageType` | Type of the main page |
| `Global.PA__Copilot_Model_AppUniqueNameContext.appUniqueNameContext.appUniqueName` | Unique name of the model-driven app |

For example, using `Global.PA__Copilot_Model_PageContext.pageContext.id.guid` and `Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName`, the form's record can be retrieved from Dataverse.