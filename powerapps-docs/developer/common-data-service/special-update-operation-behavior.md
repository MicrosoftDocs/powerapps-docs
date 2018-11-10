---
title: "Behavior of specialized update operations (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes special behavior in plug-ins and workflows for update events due to deprecated messages." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Behavior of specialized update operations

There are several deprecated specialized messages that perform update operations. In earlier versions it was required to use these messages, but now the same operations should be performed using <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> class with <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>

[!INCLUDE [cc-legacy-update-messages](includes/cc-legacy-update-messages.md)]

More information: [Legacy update messages](org-service/entity-operations-update-delete.md#legacy-update-messages) 

This change introduced some special behaviors that should be noted for plug-ins and workflows. 

## For Plug-ins

When update requests are processed that include both owner fields plus other standard fields for business owned entities, plug-ins registered for the **Update** message in **PreOperation** and/or **PostOperation** stages execute once for all non-owner fields, and then once for the owner fields. Examples of owner fields would be `businessunit` and `manager` (for a [SystemUser Entity](reference/entities/systemuser.md)). Examples of business owned entities include [SystemUser](reference/entities/systemuser.md), [BusinessUnit](reference/entities/businessunit.md),[Equipment](/dynamics365/customer-engagement/developer/entities/equipment) and [Team](reference/entities/team.md).

When update requests are processed that include both state/status fields plus other standard fields, plug-ins registered for the **Update** message in **PreOperation** and/or **PostOperation** stages execute once for all non-state/status fields, and then once for the state/status fields.

In order for plug-in code to receive the full data changes of the update, you must register the plug-in in the **PreOperation** and then store relevant information in <xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables> in the plug-in context for later plug-ins (in the pipeline) to consume.

## For Workflows

When update requests are processed that include both owner fields plus other standard fields, workflows registered for the **Update** message execute once for all non-owner fields, and then once for the owner fields. Workflows registered for the **Assign** message by users continue to be triggered by updates to owner fields.

When update requests are processed that include both state/status fields plus other standard fields, workflows registered for the **Update** message execute once for all non-state/status fields, and then once for the state/status fields. Workflows registered for the **Change Status** step continue to be triggered by updates to state/status fields.

### See also

[Update and Delete entities using the Organization Service](org-service/entity-operations-update-delete.md)<br />
[Event Framework](event-framework.md)