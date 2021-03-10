---
title: "Troubleshoot plug-ins (Microsoft Dataverse for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Contains information on errors that can occur due to plug-ins and how to fix them." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/06/2020
ms.reviewer: "pehecke"
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

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

This topic contains information about errors that can occur due to plug-ins and how to fix them.

## Transaction errors

There are two common types of errors related to transactions: 

Error Code: `-2146893812`<br />
Error Message: `ISV code reduced the open transaction count. Custom plug-ins should not catch exceptions from OrganizationService calls and continue processing.`

Error Code: `-2147220911`<br />
Error Message: `There is no active transaction. This error is usually caused by custom plug-ins that ignore errors from service calls and continue processing.`

> [!NOTE]
> The top error was added most recently. It should occur immediately and in the context of the plug-in that contains the problem. The bottom error can still occur in different circumstances, typically involving custom workflow activities. It may be due to problems in another plug-in.

To understand the message, you need to appreciate that any time an error related to a data operation occurs within a synchronous plug-in the transaction for the entire operation will be ended.

More information: [Scalable Customization Design in Microsoft Dataverse](scalable-customization-design/overview.md)

The most common cause is simply that a developer might believe they can attempt to perform an operation that *might* succeed so they wrap that operation in a try/catch block and attempt to swallow the error if it fails.

While this may work for a client application, within the execution of a plug-in any data operation failure will result in rolling back the entire transaction. You can't swallow the error, so you must make sure to always return an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException>.

## Error: Sql error: Execution Timeout Expired

Error Code: `-2147204783`<br />
Error Message: `Sql error: 'Execution Timeout Expired.  The timeout period elapsed prior to completion of the operation or the server is not responding.'`

There are a wide variety of reasons that a SQL timeout error may occur.

### Blocking

Blocking is the most common cause for a SQL Timeout error is that the operation is waiting for resources that are being locked by another SQL transaction. The error is the result of the system protecting the integrity of the data and from long running requests that impact performance for users.

Blocking may be due to other concurrent operations. Your code may work fine in isolation in a test environment and still be susceptible to conditions that will only occur when multiple users are initiating the logic in your plug-in.

When writing plug-ins, it is essential to understand how to design customizations that are scalable. More information: [Scalable Customization Design in Dataverse](scalable-customization-design/overview.md)

### Cascade operations

Certain actions you make in your plug-in, such as assigning or deleting a record, can initiate cascading operations on related records. These actions could apply locks on related records causing subsequent data operations to be blocked which in turn can lead to a SQL timeout. 

You should consider the possible impact of these cascading operations on data operations in your plug-in. More information: [Entity relationship behavior](../../maker/data-platform/entity-relationship-behavior.md)

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

## Error: Message size exceeded when sending context to Sandbox

<!-- This is the error code for an unexpected error we should be providing a specific error code. Bug 1470173 is tracking this. -->
Error Code: `-2147220970`<br />
Error Message: `Message size exceeded when sending context to Sandbox. Message size: ### Mb`

This error occurs when a message payload is greater than 116.85 MB **AND** a plug-in is registered for the message. The error message will include the size of the payload that caused this error.
 
The limit will help ensure that users running applications cannot interfere with each other based on resource constraints. The limit will help provide a level of protection from unusually large message payloads that threaten the availability and performance characteristics of the Dataverse platform.
 
116.85 MB is large enough that it should be rare to encounter this case. The most likely situation where this case might occur is when you retrieve a record with multiple related records which include large binary files.
 
If you encounter this error you can:

1.	Remove the plug-in for the message. If there are no plug-ins registered for the message, the operation will complete without an error.
2.	If the error is occurring in a custom client, you can modify your code so that it doesn't attempt to perform the work in a single operation. Instead, write code to retrieve the data in smaller parts.

## Error: The given key was not present in the dictionary

Dataverse frequently uses classes derived from the abstract <xref:Microsoft.Xrm.Sdk.DataCollection`2> class that represents a collection of keys and values. For example, with plug-ins the  <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> property is a <xref:Microsoft.Xrm.Sdk.ParameterCollection> derived from the <xref:Microsoft.Xrm.Sdk.DataCollection`2> class. These classes are essentially dictionary objects where you access a specific value using the key name.

### Error codes

This error occurs when the key value in code doesn't exist in the collection. This is a run-time error rather a platform error. When this error occurs within a plug-in, the error code will depend on whether the error was caught.

If the developer caught the exception and returned an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> as described in [Handle exceptions in plug-ins](handle-exceptions.md), the following error will be returned:

Error Code: `-2147220891`<br />
Error Message: `ISV code aborted the operation.`

However, with this error it is common that the developer doesn't catch it properly and the following error will be returned:

Error Code: `-2147220956`<br />
Error Message: `An unexpected error occurred from ISV code.`

> [!NOTE]
> "ISV" stands for *Independent Software Vendor*.

### Causes

This error frequently occurs at design time and can be due to a misspelling or using the incorrect casing. The key values are case sensitive.

At run-time the error is frequently due to the developer assuming that the value will be present when it isn't. For example, in a plug-in that is registered for the update of an entity, only those values which are changed will be included in the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Attributes> collection.

### Prevention

To prevent this error you must check that the key exists before attempting to use it to access a value. 

For example, when accessing an entity attribute, you can use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Contains(System.String)> method to check whether an attribute exists in an entity as shown in the following code.

```csharp
// Obtain the execution context from the service provider.  
IPluginExecutionContext context = (IPluginExecutionContext)
    serviceProvider.GetService(typeof(IPluginExecutionContext));

// The InputParameters collection contains all the data passed in the message request.  
if (context.InputParameters.Contains("Target") &&
    context.InputParameters["Target"] is Entity)
    {
    // Obtain the target entity from the input parameters.  
    Entity entity = (Entity)context.InputParameters["Target"];

    //Check whether the name attribute exists.
    if(entity.Contains("name"))
    {
        string name = entity["name"];
    }
```

Some developers use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue``1(System.String)> method to avoid this error when accessing entity attributes, but be aware that this method will return the default value of the type if the attribute doesn't exist. If the default value is null, this works as expected. But if the default value doesn't return null, such as with a `DateTime`, the value returned will be `1/1/0001 00:00` rather than null.

## Error: You cannot start a transaction with a different isolation level than is already set on the current transaction

Error Code: `-2147220989`<br />
Error Message: `You cannot start a transaction with a different isolation level than is already set on the current transaction`

Plug-ins are intended to support business logic. Modifying any part of the data schema within synchronous plug-in is not supported. These operations frequently take longer and may cause cached metadata used by applications to become out of sync. However, these operations can be performed in a plug-in step registered to run asynchronously.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]