---
title: "Sample: CreateMultiple and UpdateMultiple plug-ins (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to write plug-ins for the CreateMultiple and UpdateMultiple messages" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 01/28/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
contributors:
  - JimDaly
  - phecke
---
# Sample: CreateMultiple and UpdateMultiple plug-ins

This sample provides several Plug-in types that demonstrate how to write plug-ins for the `CreateMultiple` and `UpdateMultiple` messages.

> [!IMPORTANT]
> The plug-ins in this sample are designed to work together with the operations in [Sample: Use CreateMultiple and UpdateMultiple](create-update-multiple.md). If you want to test these plug-ins, you need to:
>  - Build the solution to create the assembly.
>  - Register the assembly using the Plug-in registration tool (PRT).
>  - Register steps for the plug-in as described below.
>  - Run one or more of the projects in the [Sample: Use CreateMultiple and UpdateMultiple](create-update-multiple.md)

## Prerequisites

- Access to Dataverse with system administrator or system customizer privileges.
- Understanding of how to write and register plug-ins.

## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Run the [Sample: Use CreateMultiple and UpdateMultiple](create-update-multiple.md) with the setting `DeleteTable` set to `false`.

   **Note**: This will create the tables needed for the plug-ins in this sample.

1. Open the [PowerApps-Samples/dataverse/orgsvc/xMultiplePluginSamples/xMultiplePluginSamples.sln](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/xMultiplePluginSamples/xMultiplePluginSamples.sln)
1. Build the solution.
1. Use the Plug-in Registration tool (PRT) to upload the `\xMultiplePluginSamples\bin\Debug\net462\xMultiplePluginSamples.dll` to the environment you ran the sample in step 2.
1. Use the PRT to register the plug-ins listed in the [Plug-in Type list](#plug-in-type-list) below.

   > [!IMPORTANT]
   > Make sure that the following two plug-ins are **not** enabled at the same time:
   >
   > - `FollowupPluginSingle` and `FollowupPluginMultiple`.
   > - `UpdateSingle` and `UpdateMultiple`.
  
  More information:  [Register a plug-in](../../register-plug-in.md)

1. Run any of the projects in the [Sample: Use CreateMultiple and UpdateMultiple](create-update-multiple.md), but set a break point before the records are deleted. This will create records that you can then inspect.
1. To inspect the records:
   1. In [Power Apps](https://make.powerapps.com/), navigate to **Dataverse** > **Tables** and locate the **Example** table. It should be visible under the **Custom** tab.
   1. Click the **Edit** button to view the records created.
   1. Add the **Description** column to the view.
   1. Repeat and observe the differences when different projects in the [Sample: Use CreateMultiple and UpdateMultiple](create-update-multiple.md) are run. The `Description` field should include the name of the project.
1. Turn on tracing and view the traces written to the `PluginTraceLog` Table. The [XrmToolBox Plugin Trace Viewer](https://jonasr.app/ptv/) is recommended for this. More information: [Tracing and logging](../../logging-tracing.md).

## What this sample does

This sample provides an experience where you can observe and interact with plug-ins that are written for the `CreateMultiple` and `UpdateMultiple` messages.

This sample depends on the [Sample: Use CreateMultiple and UpdateMultiple](create-update-multiple.md) so that the merged message processing pipeline behaviors can be verified.

The **Create and Update Multiple Sample** contains 4 separate projects that do the same thing in different ways. The following steps describe what the **Create and Update Multiple Sample** projects do and how the plug-ins in this sample interact with those operations.

1. Create a new custom table named `sample_example` if it doesn't already exist.
1. Prepare a configurable number of `sample_example` entity instances for the custom table representing records to create.

   Each record has the  `sample_name` column value set with an incrementing number. The first value is `sample record 0000001`.

1. Create the `sample_example` records. Each project uses a different method.
   
   > [!NOTE]
   > Each project will pass a `tag` parameter with the name of the project so that it is available as a shared variable to the plug-in. This value will be used by the `CreateMultiplePreOp.cs` plug-in in this sample. More information: [Add a shared variable to the plugin execution context](../../optional-parameters.md#add-a-shared-variable-to-the-plugin-execution-context)
   >
   > The `FollowupPluginSingle.cs` OR `FollowupPluginMultiple.cs` plug-ins in this sample create a follow up task record on create on the `Create` OR `CreateMultiple` message respectively.

1. Update the set of entity instances that were created by appending text to the `sample_name` attribute. The first value is `sample record 0000001 Updated`.
1. Update the `sample_example` records using the same method they were created.

   > [!NOTE]
   > The `UpdateSingle.cs` OR `UpdateMultiple.cs` plug-ins in this sample update the `sample_description` attribute showing the old and new value for the `sample_name` attribute.

1. Use a [BulkDeleteRequest](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) to delete the `sample_example` records created and report on the success of this request.
1. Delete the custom `sample_example` table created in the first step, unless the setting `DeleteTable` is set to `false`.

> [!IMPORTANT]
> To run this sample you must first run the **Create and Update Multiple Sample** with the setting `DeleteTable` set to `false`. This will create the table this sample depends on and allow you to register steps for the plug-ins.

### Plug-in Type list

This sample contains the following plug-in types designed to interact with the operations performed by the **Create and Update Multiple Sample**, or to help capture the changes with each message.

|Plug-in Type|Message|Stage|Description|
|---------|---------|---------|---------|
|`ContextWriter.cs`|Any|Any|Use this plug-in to write details of the [IPluginExecutionContext4](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4) to the trace log so that you can see the values being passed. Add entity images in the step registration to view the content.|
|`CreateMultiplePreOp.cs`|CreateMultiple|PreOperation (20)|Sets the `sample_description` attribute value to `$"'tag' value for Create = '{tagValue}'."` where `tagValue` is the value set using the optional `tag` parameter. |
|`FollowupPluginMultiple.cs`|CreateMultiple|PostOperation (40)|This is the replacement for `FollowupPluginSingle.cs`.<br /><br />Applies the same action as `FollowupPluginSingle.cs`.|
|`FollowupPluginSingle.cs`|Create|PostOperation (40)|Creates a `task` record associated with the `sample_example` record created.|
|`UpdateMultiple.cs`|UpdateMultiple|PreOperation (20)|This is the replacement for `UpdateSingle.cs`.<br /><br />Applies the same action as `UpdateSingle.cs` except it uses an Entity image named `example_preimages` from the matching item in the `PreEntityImagesCollection` to compare the original `sample_name` value with the value in the update operation.|
|`UpdateSingle.cs`|Update|PreOperation (20)|Uses a `PreEntityImage` named `example_preimage` to compare the original `sample_name` value with the value in the update operation.<br /><br />When the values are different, append a message to the `sample_description` attribute value: `$"\\r\\n - 'sample_name' changed from '{oldName}' to '{newName}'."`, where `oldName` is the original value and `newName` is the new value.|

## How this sample works

This sample includes plug-ins written for the `CreateMultiple` and `UpdateMultiple` messages using the guidance provided in [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](../../write-plugin-multiple-operation.md).

Two of the plug-ins, `FollowupPluginSingle.cs` and `UpdateSingle.cs`, represent the 'before' plug-in written for the `Create` and `Update` messages. The `FollowupPluginMultiple.cs` and `UpdateMultiple.cs` plug-ins represent the 'after' plug-ins written for `CreateMultiple` and `UpdateMultiple` messages.

By contrasting these plug-ins, you can observe how logic applied for the single operation can be modified to work with the operation that includes multiple entities.

The `ContextWriter.cs` plug-in captures data from the [IPluginExecutionContext4 Interface](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4) and writes it to the [PluginTraceLog](../../reference/entities/plugintracelog.md) so that you can see the data passed to the plug-in.

<!-- TODO: When the bugs are fixed, include examples of the plug-in trace log here -->

## Demonstrates

- How to write plug-ins for the `CreateMultiple` and `UpdateMultiple` messages
- How to modify existing plug-ins using `Create` and `Update` to use `CreateMultiple` and `UpdateMultiple` messages.
- How to write information about the plug-in execution context to the plug-in trace log.

## Clean up

After you finish running this sample you should unregister the `xMultiplePluginSamples.dll` assembly and delete the `sample_example` table. You will not be able to delete the `sample_example` table if there are any plug-in steps registered on messages for the table.

### See Also

[Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](../../write-plugin-multiple-operation.md)<br />
[Use CreateMultiple and UpdateMultiple (Preview)](../use-createmultiple-updatemultiple.md)<br />
[Sample: Use CreateMultiple and UpdateMultiple](create-update-multiple.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]