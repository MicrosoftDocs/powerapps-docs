---
title: "Sample: Update next birthday using a custom workflow activity (Microsoft Dataverse) | Microsoft Docs"
description: "The sample demonstrates workflow activity returns the next birthday. Use this in a workflow that sends a birthday greeting to a customer. "
ms.date: 04/06/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
manager: sunilg
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
---
# Sample: Update next birthday using a custom workflow activity



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
