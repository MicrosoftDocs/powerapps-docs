# How to Identify Purge Failures Caused by a Custom Plugin

## When to Start the Investigation
Start investigating if the "Retention Failed" count increases within the pending delete state.

## Steps to Follow:

### 1. Verify if the Failure is Due to a Custom Plugin
Confirm whether the failure is triggered by a custom plugin that executes on the "Delete" message for the specific entities. Check the `RetentionFailureDetail` table to see if the `OperationID` matches `RetentionOperationId`, and the `OperationType` equals `30` (indicating Purge).

```
<OrgUrl>/api/data/v9.0/retentionfailuredetails?$filter=operationid%20eq%20%27<RetentionOperationID>%27%20and%20operation%20eq%2030
```

![image.png](/.attachments/image-d4cfc4a8-f295-4083-8128-30e533cc6721.png)

We can also review the Plugin Trace Logs to identify the failure point.

![image2.PNG](/.attachments/image2-d68cc343-d8d4-4ea7-9409-bd09ac08daea.PNG)
### 2. Bypassing the Validation for Deletes Triggered by Retention
If you want to bypass validation for deletes initiated during retention, modify your plugin logic as shown below:

```csharp
class SampleDeletePlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        if (IsDeleteDueToRetention(serviceProvider))
        {
            // Insert logic to handle deletes triggered by retention
        }
        else
        {
            // Insert logic to handle regular deletes not related to retention
        }
    }

    private bool IsDeleteDueToRetention(IServiceProvider serviceProvider)
    {
        IPluginExecutionContext currentContext = (IPluginExecutionContext)
                            serviceProvider.GetService(typeof(IPluginExecutionContext));
        while (currentContext != null)
        {
            if (currentContext.InputParameters.TryGetValue<bool>("DeleteInvokedByRetention", out var isDeleteByRetention) && isDeleteByRetention)
            {
                return true;
            }
        }
        return false;
    }
}
```

### 3. Apply Similar Validation for Retain Messages
To apply similar validation for retention, you can create a plugin on the "Retain" message. Follow the same approach as described above for handling retention-based logic, but ensure the logic is suited to the "Retain" message.

### 4. Additional Resources
- [Reference to Long-term data retention
](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/long-term-retention?tabs=sdk#custom-logic-while-retention-executes)
