---
title: "Sample: Calculate a credit score with a custom workflow activity (Microsoft Dataverse) | Microsoft Docs"
description: "The sample demonstrates workflow activity calculates the credit score based on the Social Security Number (SSN) and name."
ms.custom: ""
ms.date: 1/28/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "samples"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 9cb7eb41-1a73-44a8-ae58-14120e84243f
caps.latest.revision: 19
author: "JimDaly"
ms.author: "jdaly"
manager: "KumarVivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Calculate a credit score with a custom workflow activity

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

This sample code is for Microsoft Dataverse. Download the complete sample here: [WorkflowActivities](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/WorkflowActivities).

## Prerequisites

[!INCLUDE [sdk-prerequisite](../../../includes/sdk-prerequisite.md)]
  
## Requirements

The following customizations must exist for this custom workflow activity to work:  

-   Entity Schema Name: `new_loanapplication`  
-   Attribute: `new_loanapplicationid` as the primary key  
-   Attribute: `new_creditscore` of type `int` with min of 0 and max of 1000 (if it is to be updated)  
-   Attribute: `new_loanamount` of type money with default min/max  
-   Customize the form to include the attribute `new_loanapplicantid`  
  
The contact entity must have the following customizations:  
  
-   Attribute: `new_ssn` as **Single Line of Text** with max length of 15  
-   One-To-Many Relationship with these properties:  
    -   Relationship Definition Schema Name: `new_loanapplicant`  
    -   Relationship Definition Related Entity Display Name: Loan Application  
    -   Relationship Attribute Schema Name: `new_loanapplicantid`  
    -   Relationship Behavior Type: Referential  
  
## Demonstrates

The following sample workflow activity calculates the credit score based on the Social Security Number (SSN) and name.  
  
## Example  

[RetrieveCreditScore.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/cds/orgsvc/C%23/WorkflowActivities/WorkflowActivities/RetrieveCreditScore.cs)

### See also

[Workflow extensions](workflow-extensions.md)<br />
[Tutorial: Create workflow extension](tutorial-create-workflow-extension.md)<br />
[Sample: Create a custom workflow activity](sample-create-custom-workflow-activity.md)<br />
[Sample: Update next birthday using a custom workflow activity](sample-update-next-birthday-using-custom-workflow-activity.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]