---
title: "Sample: Audit table data changes (Microsoft Dataverse) | Microsoft Docs" 
description: "This sample showcases how to audit table data changes" 
ms.date: 12/08/2022
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Audit table data changes

This sample shows how to enable and disable auditing on a table and its columns, retrieve the data change history of the audited table, and delete the audit records. You can view the sample [here](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/AuditEntityData).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample does the following:

1. Enable auditing for the organization and the account table if not already enabled.
2. Create an account record.
3. Use the `RetrieveRecordChangeHistory` message via the [RetrieveRecordChangeHistoryRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest) to retrieve the history of the account record created in step 2.
4. Display some of the details information in each audit record.
5. Update the account record, updating a specific column.
6. Retrieve the change history of the changed column using the `RetrieveAttributeChangeHistory` message with the [RetrieveAttributeChangeHistoryRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest).
7. Display the attribute change history.
8. Use the `RetrieveAuditDetails` message via the [RetrieveAuditDetailsRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest) to display some of the audit details.
9. Return the environent auditing to the original state and delete the account record created.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Enables auditing for the organization and account table if necessary.
1. Creates an sample account record.

### Demonstrate

Use of the  `RetrieveRecordChangeHistory`, `RetrieveAttributeChangeHistory`, and `RetrieveAuditDetails` messages to show the kinds of data available through these auditing apis.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
