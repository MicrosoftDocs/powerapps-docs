---
title: "Troubleshoot plug-ins (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Contains information on errors that can occur due to plug-ins and how to fix them." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/26/2019
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Troubleshoot plug-ins 

This topic contains information about errors that can occur due to plug-ins and how to fix them.

## Error: There is no active transaction. 

Error Code: `-2147220911`<br />
Error Message: `There is no active transaction. This error is usually caused by custom plug-ins that ignore errors from service calls and continue processing.`

This can be a difficult error to address because the cause can be in someone else's code. To understand the message, you need to appreciate that any time an error related to a data operation occurs within a synchronous plug-in the transaction for the entire operation will be ended.

More information: [Scalable Customization Design in Common Data Service](scalable-customization-design/overview.md)

The most common cause is simply that a developer might believe they can attempt to perform an operation that *might* succeed so they wrap that operation in a try/catch block and attempt to swallow the error if it fails.

While this may work for a client application, within the execution of a plug-in any data operation failure will result in rolling back the entire transaction. You can't swallow the error, so you must make sure to always return an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException>.

## Error: Sql error: Execution Timeout Expired

Error Code: `-2147204783`<br />
Error Message: `Sql error: 'Execution Timeout Expired.  The timeout period elapsed prior to completion of the operation or the server is not responding.'`

There are a wide variety of reasons that a SQL timeout error may occur.

### Blocking

Blocking is the most common cause for a SQL Timeout error is that the operation is waiting for resources that are being locked by another SQL transaction. The error is the result of the system protecting the integrity of the data and from long running requests that impact performance for users.

Blocking may be due to other concurrent operations. Your code may work fine in isolation in a test environment and still be susceptible to conditions that will only occur when multiple users are initiating the logic in your plug-in.

When writing plug-ins, it is essential to understand how to design customizations that are scalable. More information: [Scalable Customization Design in Common Data Service](scalable-customization-design/overview.md)

### Cascade operations

Certain actions you make in your plug-in, such as assigning or deleting a record, can initiate cascading operations on related records. These actions could apply locks on related records causing subsequent data operations to be blocked which in turn can lead to a SQL timeout. 

You should consider the possible impact of these cascading operations on data operations in your plug-in. More information: [Entity relationship behavior](../../maker/common-data-service/entity-relationship-behavior.md)

Because these behaviors can be configured differently between environments, the behavior may be difficult to reproduce unless the environments are configured in the same way.

### Indexes on new entities

If the plug-in is performing operations using an entity or attribute that has been created recently, some Azure SQL capabilities to manage indexes might make a difference after a few days.

## Errors due to user privileges

In a client application you can disable commands that users are not allowed to perform. Within a plug-in you don't have this. Your code may include some automation that the calling user doesn't have the privileges to perform.

You can register the plug-in to run in the context of a user known to have the correct privileges by setting the **Run in User's Context** value to that user. Or you can execute the operation impersonating another user. More information:
 - [Register a plug-in](register-plug-in.md)
 - [Impersonate a user](impersonate-a-user.md)

<!-- But if you prefer that the logic in your plug-in adapt to the privileges that the calling user has, you really need to verify the user's privileges in your code.

TODO: Add content that shows how to do this -->
