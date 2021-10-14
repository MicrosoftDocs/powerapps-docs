---
title: "Sample: Update next birthday using a custom workflow activity (Microsoft Dataverse) | Microsoft Docs"
description: "The sample demonstrates workflow activity returns the next birthday. Use this in a workflow that sends a birthday greeting to a customer. "
ms.custom: ""
ms.date: 1/28/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "samples"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 1cff83b0-1f7b-4ddb-a2af-b85f9f785529
caps.latest.revision: 21
author: "JimDaly"
ms.author: "jdaly"
manager: "KumarVivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Update next birthday using a custom workflow activity

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

Download the complete sample here: [WorkflowActivities](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/WorkflowActivities).

## Prerequisites

[!INCLUDE [sdk-prerequisite](../../../includes/sdk-prerequisite.md)]
  
## Requirements 
 
The following custom field must exist for this custom workflow activity to work:  
  
-   `Contact`.`new_nextbirthday`  
  
## Demonstrates  
 The following sample workflow activity returns the next birthday. Use this in a workflow that sends a birthday greeting to a customer.  
  
## Example  

[NextBirthday.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/cds/orgsvc/C%23/WorkflowActivities/WorkflowActivities/NextBirthday.cs)
  
### See also

[Workflow extensions](workflow-extensions.md)<br />
[Tutorial: Create workflow extension](tutorial-create-workflow-extension.md)<br />
[Sample: Create a custom workflow activity](sample-create-custom-workflow-activity.md)<br />
[Sample: Calculate a credit score with a custom workflow activity](sample-calculate-credit-score-custom-workflow-activity.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]