---
title: Write plug-ins for CreateMultiple and UpdateMultiple (preview)
description: Learn how to write plug-ins that use the bulk operation messages CreateMultiple and UpdateMultiple to operate on multiple rows of data in a Microsoft Dataverse table.
ms.date: 08/02/2023
ms.topic: how-to
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
  - hakhemic
ms.custom: tap-template
---

# Write plug-ins for CreateMultiple and UpdateMultiple (preview)

> [!NOTE]
> The `CreateMultiple` and `UpdateMultiple` messages are being deployed. All tables that support `Create` and `Update` will eventually support `CreateMultiple` and `UpdateMultiple`, but some tables may not support them yet. [Learn more about bulk operation messages](bulk-operations.md)

You should write plug-ins for the `CreateMultiple` and `UpdateMultiple` messages with tables where records may need to be created or updated in bulk, or when performance in creating and updating large numbers of records is important. Just about every table that stores business data may need to be created or updated in bulk.

If you have existing plug-ins for the `Create` and `Update` messages for tables like these, you should migrate them to use `CreateMultiple` and `UpdateMultiple` instead.

## Is updating plug-ins required?

You're not required to migrate your plug-ins to use `CreateMultiple` and `UpdateMultiple` instead of `Create` and `Update`. Your logic continues to be applied when applications use `CreateMultiple` or `UpdateMultiple`. There's no requirement to migrate your plug-ins because the Dataverse message processing pipeline [merges the logic for plugins](bulk-operations.md#message-pipelines-merged) written for either the single or multiple version of these messages.

However, only plug-ins written for the multiple version of these messages get a significant performance boost. Over time, as more developers choose to optimize performance by using the `CreateMultiple` and `UpdateMultiple` messages, we expect writing plug-ins for multiple operations to become the standard. Plug-ins written for single operations will be the exception.

## What's different?

The following are some of the differences you need to manage when you migrate your plug-ins to the the `CreateMultiple` and `UpdateMultiple` messages.

### Targets instead of Target

The multiple version of these messages has a `Targets` parameter that's an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) rather than a `Target` parameter that's a single [Entity](xref:Microsoft.Xrm.Sdk.Entity). Your plug-in code needs to loop through the entities in the collection and apply logic to each one.

### Entity images

Entity images that are configured in the step registration for your plug-ins are an array of [EntityImageCollection](xref:Microsoft.Xrm.Sdk.EntityImageCollection). These entity images are only available when you use the [IPluginExecutionContext4 Interface](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4), which provides the [PreEntityImagesCollection](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4.PreEntityImagesCollection) and [PostEntityImagesCollection](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4.PostEntityImagesCollection) properties. These arrays provide access to the same entity images in an array that's synchronized with the EntityCollection.

If you're using the `PluginBase` class that's the standard when initializing plug-in projects using Power Platform tools, then in the `PluginBase.cs` file you should replace all instances of `IPluginExecutionContext` with `IPluginExecutionContext4` so that these collections of entity images are available to your plug-in.

> [!IMPORTANT]
> When you [configure entity images](register-plug-in.md#define-entity-images) for plug-in steps for `CreateMultiple` and `UpdateMultiple`, it's important that you carefully select which column data to include. Don't select the default option of all columns. This data is multiplied by the number of entities passed in the `Targets` parameter and contributes to the total size of the message that's sent to the sandbox. You may hit the [limit on message size](bulk-operations.md#message-size-limits).

### Attribute filters

For a plug-in registered on `Update` or `UpdateMultiple`, you can [specify filtering attributes in the step registration](best-practices/business-logic/include-filtering-attributes-plugin-registration.md).

- With `Update`, the plug-in runs only when any of the selected attributes are included with the `Target` entity that's being updated.
- With `UpdateMultiple`, the plug-in runs when any of the selected attributes are included *in any* of the entities in the `Targets` parameter.

> [!IMPORTANT]
> For `UpdateMultiple`, you can't assume that every entity in the `Targets` parameter contains attributes that are used in a filter.

## Example

The following examples, one with some basic logic for `Update` and another with logic for `UpdateMultiple`, access entity images registered with the step.

### [Single](#tab/single)

This example updates the `sample_description` attribute with information about whether the `sample_name` value has changed. It refers to an entity image named `example_preimage` that was registered with the step.

```csharp
// Verify input parameters
if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity entity)
{

   // Verify expected entity image from step registration
   if (context.PreEntityImages.TryGetValue("example_preimage", out Entity preImage))
   {

      bool entityContainsSampleName = entity.Contains("sample_name");
      bool entityImageContainsSampleName = preImage.Contains("sample_name");
      bool entityImageContainsSampleDescription = preImage.Contains("sample_description");

      if (entityContainsSampleName && entityImageContainsSampleName && entityImageContainsSampleDescription)
      {
            // Verify that the entity 'sample_name' values are different
            if (entity["sample_name"] != preImage["sample_name"])
            {
               string newName = (string)entity["sample_name"];
               string oldName = (string)preImage["sample_name"];
               string message = $"\\r\\n - 'sample_name' changed from '{oldName}' to '{newName}'.";

               // If the 'sample_description' is included in the update, do not overwrite it, just append to it.
               if (entity.Contains("sample_description"))
               {

                  entity["sample_description"] = entity["sample_description"] += message;

               }
               else // The sample description is not included in the update, overwrite with current value + addition.
               {
                  entity["sample_description"] = preImage["sample_description"] += message;
               }

               // Success:
               localPluginContext.Trace($"Appended to 'sample_description': \"{message}\" ");
            }
            else
            {
               localPluginContext.Trace($"Expected entity and preImage 'sample_name' values to be different. Both are {entity["sample_name"]}");
            }
      }
      else
      {
            if (!entityContainsSampleName)
               localPluginContext.Trace("Expected entity sample_name attribute not found.");
            if (!entityImageContainsSampleName)
               localPluginContext.Trace("Expected preImage entity sample_name attribute not found.");
            if (!entityImageContainsSampleDescription)
               localPluginContext.Trace("Expected preImage entity sample_description attribute not found.");
      }
   }
   else
   {
      localPluginContext.Trace($"Expected PreEntityImage: 'example_preimage' not found.");
   }
}
else
{
   if (!context.InputParameters.Contains("Target"))
      localPluginContext.Trace($"Expected InputParameter: 'Target' not found.");
   if (!(context.InputParameters["Target"] is Entity))
      localPluginContext.Trace($"Expected InputParameter: 'Target' is not Entity.");
}
```

### [Multiple](#tab/multiple)

This example applies the same logic as the **Single** version, except the `Entity` and the `EntityImageCollection` are synchronized using a `count` variable with a `foreach` loop through the `EntityCollection`. It also includes the `count` when using the `localPluginContext.Trace` method, and is less verbose. Traces are only included when error conditions occur. The amount of data that you can write to the trace log table is limited, so you should try to avoid writing traces for each iteration.

```csharp
// Verify input parameters
if (context.InputParameters.Contains("Targets") && context.InputParameters["Targets"] is EntityCollection entityCollection)
{
   // Verify expected entity images from step registration
   if (context.PreEntityImagesCollection.Length == entityCollection.Entities.Count)
   {
      int count = 0;
      foreach (Entity entity in entityCollection.Entities)
      {
            EntityImageCollection entityImages = context.PreEntityImagesCollection[count];

            // Verify expected entity image from step registration
            if (entityImages.TryGetValue("example_preimage", out Entity preImage))
            {
               bool entityContainsSampleName = entity.Contains("sample_name");
               bool entityImageContainsSampleName = preImage.Contains("sample_name");
               bool entityImageContainsSampleDescription = preImage.Contains("sample_description");

               if (entityContainsSampleName && entityImageContainsSampleName && entityImageContainsSampleDescription)
               {
                  // Verify that the entity 'sample_name' values are different
                  if (entity["sample_name"] != preImage["sample_name"])
                  {
                        string newName = (string)entity["sample_name"];
                        string oldName = (string)preImage["sample_name"];
                        string message = $"\\r\\n - 'sample_name' changed from '{oldName}' to '{newName}'.";

                        // If the 'sample_description' is included in the update, do not overwrite it, just append to it.
                        if (entity.Contains("sample_description"))
                        {
                           entity["sample_description"] = entity["sample_description"] += message;
                        }
                        else // The sample description is not included in the update, overwrite with current value + addition.
                        {
                           entity["sample_description"] = preImage["sample_description"] += message;
                        }

                        // Not tracing Success for brevity. There is a limit to what tracelog can display.
                        // localPluginContext.Trace($"Appended to 'sample_description': \"{message}\" for item {count} ");
                  }
                  else
                  {
                        localPluginContext.Trace($"Expected entity and preImage 'sample_name' values to be different. Both are {entity["sample_name"]} for item {count}");
                  }
               }
               else
               {
                  if (!entityContainsSampleName)
                        localPluginContext.Trace($"Expected entity sample_name attribute not found for item {count}.");
                  if (!entityImageContainsSampleName)
                        localPluginContext.Trace($"Expected preImage entity sample_name attribute not found for item {count}.");
                  if (!entityImageContainsSampleDescription)
                        localPluginContext.Trace($"Expected preImage entity sample_description attribute not found for item {count}.");
               }
            }
            else
            {
               localPluginContext.Trace($"Expected PreEntityImage: 'example_preimage' not found for item {count}.");
            }

            count++;
      }
   }
   else
   {
      localPluginContext.Trace($"Expected PreEntityImagesCollection to contain Entity images for each Entity.");
   }
}
else
{
   if (!context.InputParameters.Contains("Targets"))
      localPluginContext.Trace($"Expected InputParameter: 'Targets' not found.");
   if (!(context.InputParameters["Targets"] is EntityCollection))
      localPluginContext.Trace($"Expected InputParameter: 'Targets' is not EntityCollection.");
}
```

---

## Handling exceptions

All errors that occur in your plug-ins should be returned using [InvalidPluginExecutionException](best-practices/business-logic/use-invalidpluginexecutionexception-plugin-workflow-activities.md). When your plug-in throws an exception for steps registered on the `CreateMultiple` and `UpdateMultiple` messages, it should identify which record caused the plug-in to fail. To capture this information, use one of the following constructors:

- [InvalidPluginExecutionException(String, Dictionary<String,String>)](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.%23ctor(System.String,System.Collections.Generic.Dictionary{System.String,System.String}))
- [InvalidPluginExecutionException(OperationStatus, String, Dictionary<String,String>)](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.%23ctor(Microsoft.Xrm.Sdk.OperationStatus,System.String,System.Collections.Generic.Dictionary{System.String,System.String}))

These constructors allow you to add values to the [InvalidPluginExecutionException.ExceptionDetails](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.ExceptionDetails) property, which can't be set directly.

Use the constructor's `Dictionary<String,String>` `exceptionDetails` parameter to include information about the failed record and any other relevant information.

### Set exception details

For the `UpdateMultiple` message, your code iterates through the [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) [Targets](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest.Targets) property and applies logic to each [Entity](xref:Microsoft.Xrm.Sdk.Entity). If a failure occurs, you can pass the [Id](xref:Microsoft.Xrm.Sdk.Entity.Id) of the record to the `InvalidPluginExecutionException` constructor in the following way:

```csharp
// in plugin code
foreach (Entity entity in Targets)
{
   // [...] When an error occurs:
   var exceptionDetails = new Dictionary<string, string>();
   exceptionDetails.Add("failedRecordId", (string)entity.Id);
   throw new InvalidPluginExecutionException("This is an error message.", exceptionDetails);
}
```

Add any other information that's relevant to the failure as string key-value pairs to the `exceptionDetails` parameter.

For `CreateMultiple`, we recommend that you don't set the primary key value for each record. In most cases, you should allow the system to set the primary key value for you because the values generated by the system are optimized for best performance.

In cases where the primary key value isn't set, if there's no other unique identifier, you may need to return the index of the failed record in the [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) `Targets` parameter, or some combination of values that uniquely identify the record that fails. For instance, a key named `failedRecordIndex` indicating the record's place in the `EntityCollection`, or any other useful unique identifier, can be added to `exceptionDetails` to help troubleshoot the failure.

### Get exception details

When you include details about the failing operation in the [InvalidPluginExecutionException.ExceptionDetails](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.ExceptionDetails) property, the client application can get them from the [OrganizationServiceFault.ErrorDetails](xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails) property through the [FaultException&lt;OrganizationServiceFault&gt;.Detail](xref:System.ServiceModel.FaultException%601.Detail) property. The following code shows how:

```csharp

try
{
   // xMultiple request that triggers your plugin
}
catch (FaultException<OrganizationServiceFault> ex)
{
   ex.Detail.ErrorDetails.TryGetValue("failedRecordId", out object failedRecordId);
}

```

If the client application uses the Web API, it can [get more details about errors](webapi/compose-http-requests-handle-errors.md#include-more-details-with-errors) by setting the `Prefer: odata.include-annotations="*"` request header.

## Replace single operation plug-ins in solutions

When you deploy plug-in step registrations in solutions, there's no way to force a step registration to be disabled or deleted. That makes replacing logic from a single operation to a multiple operation plug-in a challenge.

When you deploy a new plug-in step in a solution for `CreateMultiple` or `UpdateMultiple` that replaces a plug-in step for `Create` or `Update`, you want to reduce the amount of time when no logic or duplicate logic is applied. You can manually disable the steps for `Create` or `Update` before or after you install the solution. If you disable before, there's a period when no logic is applied. If you disable after, there's a period when duplicate logic is applied. In either case, the organization may require scheduled downtime to ensure logic is applied consistently.

To minimize the duration of either of these conditions, we recommend you include logic to disable any steps that are being replaced by deploying the new plug-ins with [Package Deployer](/power-platform/alm/package-deployer-tool). Package Deployer provides the capability to execute [custom code](/power-platform/alm/package-deployer-tool#add-custom-code) before, during, and after the package is imported into an environment. Use this code to disable the existing step registrations.

### See also

[Sample: CreateMultiple and UpdateMultiple plug-ins](org-service/samples/createmultiple-updatemultiple-plugin.md)   
[Bulk operation messages (preview)](bulk-operations.md)   
[Sample: Use CreateMultiple and UpdateMultiple](org-service/samples/create-update-multiple.md)   
[Optimize performance for Create and Update operations](optimize-performance-create-update.md)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
