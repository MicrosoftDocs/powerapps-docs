---
title: "Sample: Calculate a credit score with a custom workflow activity (Microsoft Dataverse) | Microsoft Docs"
description: "The sample demonstrates workflow activity calculates the credit score based on the Social Security Number (SSN) and name."
ms.date: 04/06/2022
author: MsSQLGirl
ms.author: sriknair
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Sample: Calculate a credit score with a custom workflow activity

This sample code is for Microsoft Dataverse. Download the complete sample here: [WorkflowActivities](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/WorkflowActivities).

## Prerequisites

[!INCLUDE [sdk-prerequisite](../../../includes/sdk-prerequisite.md)]

## Requirements

The following customizations must exist for this custom workflow activity to work:

- Entity Schema Name: `new_loanapplication`
- Attribute: `new_loanapplicationid` as the primary key
- Attribute: `new_creditscore` of type `int` with min of 0 and max of 1000 (if it is to be updated)
- Attribute: `new_loanamount` of type money with default min/max
- Customize the form to include the attribute `new_loanapplicantid`

The contact entity must have the following customizations:

- Attribute: `new_ssn` as **Single Line of Text** with max length of 15
- One-To-Many Relationship with these properties:
  - Relationship Definition Schema Name: `new_loanapplicant`
  - Relationship Definition Related Entity Display Name: Loan Application
  - Relationship Attribute Schema Name: `new_loanapplicantid`
  - Relationship Behavior Type: Referential

## Demonstrates

The following sample workflow activity calculates the credit score based on the Social Security Number (SSN) and name.

## Example

[RetrieveCreditScore.cs](https://github.com/Microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp/WorkflowActivities/WorkflowActivities/RetrieveCreditScore.cs)

### See also

[Workflow extensions](workflow-extensions.md)<br />
[Tutorial: Create workflow extension](tutorial-create-workflow-extension.md)<br />
[Sample: Create a custom workflow activity](sample-create-custom-workflow-activity.md)<br />
[Sample: Update next birthday using a custom workflow activity](sample-update-next-birthday-using-custom-workflow-activity.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
