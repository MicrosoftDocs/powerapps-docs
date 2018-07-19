---
title: "Sample: Use Dynamics 365 for Outlook methods (Common Data Service for Apps)| Microsoft Docs"
description: "This sample shows how to use the methods available in the `Microsoft.Crm.Outlook.Sdk.dll` assembly."
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "sriharibs" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Use Dynamics 365 for Outlook methods

This sample code is for Common Data Service for Apps. To download the sample, refer [Sample: Use Dynamics 365 for Outlook methods](https://msdn.microsoft.com/en-us/library/gg309513.aspx).

## Prerequisites

[!INCLUDE [sdk-prerequisite](../../../includes/sdk-prerequisite.md)]
  
## Demonstrates  
 This sample shows how to use the methods available in the `Microsoft.Crm.Outlook.Sdk.dll` assembly.  
  
## Example  

```csharp
// Set up the CRM Service.  
CrmOutlookService outlookService = new CrmOutlookService();

// Determine if the Outlook client is running
if (outlookService.IsCrmClientLoaded)
{
    if (outlookService.IsCrmDesktopClient)
    {
        // The desktop client cannot go offline
        Console.WriteLine("CRM Client Desktop URL: " +
            outlookService.ServerUri.AbsoluteUri);
        Console.WriteLine("CRM Client state: " +
            outlookService.State.ToString());
    }
    else
    {
        // See if laptop client is offline
        if (outlookService.IsCrmClientOffline)
        {
            Console.WriteLine("CRM Client Offline URL: " +
                outlookService.ServerUri.AbsoluteUri);
            Console.WriteLine("CRM Client state: " +
                outlookService.State.ToString());

            // Take client online
            // NOTE: GoOnline() will automatically Sync up with CRM
            // database, no need to call Sync() manually
            Console.WriteLine("Going Online...");
            outlookService.GoOnline();

            Console.WriteLine("CRM Client state: " +
                outlookService.State.ToString());
        }
        else
        {
            Console.WriteLine("CRM Client Online URL: " +
                outlookService.ServerUri.AbsoluteUri);
            Console.WriteLine("CRM Client state: " +
                outlookService.State.ToString());

            // Take client offline 
            // NOTE: GoOffline triggers a synchronization of the
            // offline database with the online server.
            // If a sync is not required, you can use SetOffline().
            Console.WriteLine("Going Offline...");
            outlookService.GoOffline();

            Console.WriteLine("CRM Client state: " +
                outlookService.State.ToString());
        }
    }
}
```
  
### See also  

[Extend Dynamics 365 for Outlook](extend-dynamics-365-outlook.md)<br />
<xref:Microsoft.Crm.Outlook.Sdk.CrmOutlookService><br />
<xref:Microsoft.Crm.Outlook.Sdk.CrmOutlookService.GoOnline><br />
<xref:Microsoft.Crm.Outlook.Sdk.CrmOutlookService.GoOffline>