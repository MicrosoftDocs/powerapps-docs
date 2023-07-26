---
title: Write plug-ins for CreateMultiple and UpdateMultiple | Microsoft Docs
description: How to write plug-ins for CreateMultiple and UpdateMultiple messages.
author: divkamath
ms.topic: article
ms.date: 05/26/2023
ms.subservice: dataverse-developer
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
  - hakhemic
---
# Write plug-ins for CreateMultiple and UpdateMultiple (Preview)

> [!NOTE]
> Not all tables currently support using the `CreateMultiple` and `UpdateMultiple` messages. These messages are currently being deployed and all tables that currently support `Create` and `Update` will support `CreateMultiple` and `UpdateMultiple` in the coming months. More information: [Bulk Operation messages (preview)](bulk-operations.md)

You should write plug-ins for the `CreateMultiple` and `UpdateMultiple` messages with tables where records may need to be created or updated in bulk, or when performance in creating and updating large numbers of records is important. Just about every table that stores business data may need to be created or updated in bulk.

If you have existing plug-ins for the `Create` and `Update` messages for tables like these, you should migrate them to use `CreateMultiple` and `UpdateMultiple` instead.

## Is updating plug-ins required?

There's no requirement to migrate your plug-ins to use `CreateMultiple` and `UpdateMultiple` instead of `Create` and `Update`. Your logic continues to be applied when applications use `CreateMultiple` or `UpdateMultiple`. There's no requirement to migrate your plug-ins because the Dataverse message processing pipeline merges the logic for plugins written for either the single or multiple version of the `Create` and `Update` messages. More information: [Message pipelines merged](bulk-operations.md#message-pipelines-merged)

However, only plug-ins written for the multiple version of these messages enable optimum performance when developers use `CreateMultiple` and `UpdateMultiple`. Over time, as more applications choose to optimize performance by using the `CreateMultiple` and `UpdateMultiple` messages, we expect writing plug-ins for multiple operations will become the standard, and plug-ins written for single operations will be the exception.

## What is different?

The following are some of the differences you need to manage when migrating existing plugins to the multiple version.

### Targets instead of Target

The multiple version of these messages has a `Targets` parameter that is an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) rather than a `Target` parameter that is a single [Entity](xref:Microsoft.Xrm.Sdk.Entity). Your plug-in code needs to loop through the entities in the collection and apply logic for each one.

### Entity Images

Entity images configured in the step registration for your plug-ins are an array of [EntityImageCollection](xref:Microsoft.Xrm.Sdk.EntityImageCollection). These entity images are only available when you use the [IPluginExecutionContext4 Interface](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4), which provides the [PreEntityImagesCollection](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4.PreEntityImagesCollection) and [PostEntityImagesCollection](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4.PostEntityImagesCollection) properties. These arrays provide access to the same entity images in an array that is synchronized with the EntityCollection.

If you're using the `PluginBase` class that is the standard when initializing plug-in projects using Power Platform tools, in the `PluginBase.cs` file you should replace all instances of `IPluginExecutionContext` with `IPluginExecutionContext4` so that these collections of entity images are available to your plug-in.

> [!IMPORTANT]
> When configuring entity images for plug-in steps for `CreateMultiple` and `UpdateMultiple`, it is very important that you carefully select which column data to include in the entity image. Do not select the default option of all columns. This data is multiplied by the number of entities passed in the `Targets` parameter and contributes to the total message size that will be sent to the sandbox.
> More information:
>
> - [Define entity images](register-plug-in.md#define-entity-images)
> - [Message size limits](bulk-operations.md#message-size-limits)

### Attribute Filters

For a plug-in registered on `Update` or `UpdateMultiple`, you can specify **Filtering Attributes** in the step registration.

- With `Update`, the plug-in only runs when any of the selected attributes are included with the `Target` entity being updated.
- With `UpdateMultiple`, the plug-in runs when any of the selected attributes are included *in any* of the entities in the `Targets` parameter.

> [!IMPORTANT]
> For `UpdateMultiple` you can't assume that every entity in the `Targets` parameter contains attributes used in a filter.

More information: [Include filtering attributes with plug-in registration](best-practices/business-logic/include-filtering-attributes-plugin-registration.md)

## Example

The following are two examples, one with some basic logic for `Update`, and another with logic for `UpdateMultiple`. Both of these access entity images registered with the step.

### [Single](#tab/single)

This example simply updates the `sample_description` attribute with information about whether the `sample_name` value has changed. It refers to an entity image named `example_preimage` that was registered with the step.

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

This example applies the same logic as the **Single** version, except the `Entity` and the `EntityImageCollection` are synchronized using an `count` variable while using a `foreach` loop through the `EntityCollection`.

This example also includes the `count` when using the `localPluginContext.Trace` method and is less verbose to only include traces when error conditions occur. The amount of data that you can write to the trace log table is limited, so you should try to avoid writing traces for each iteration.

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

## Handling Exceptions

All errors that occur within plug-ins should be returned using [InvalidPluginExecutionException](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException). More information: [Use InvalidPluginExecutionException in plug-ins and workflow activities](best-practices/business-logic/use-invalidpluginexecutionexception-plugin-workflow-activities.md)

When you throw an exception for steps registered on the `CreateMultiple` and `UpdateMultiple` messages, you should specify which record caused the plug-in to fail. To capture this information, you need to use one of these constructors:

- [InvalidPluginExecutionException(String, Dictionary<String,String>)](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.%23ctor(System.String,System.Collections.Generic.Dictionary{System.String,System.String}))
- [InvalidPluginExecutionException(OperationStatus, String, Dictionary<String,String>)](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.%23ctor(Microsoft.Xrm.Sdk.OperationStatus,System.String,System.Collections.Generic.Dictionary{System.String,System.String}))

These constructors allow you to add values to the [InvalidPluginExecutionException.ExceptionDetails](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.ExceptionDetails) property, which can't be set directly.

Use the constructor's `Dictionary<String,String>` `exceptionDetails` parameter to include information about the failed record and any other relevant information.

### Set exception details

For the `UpdateMultiple` message, your code iterates through the [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) [Targets](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest.Targets) property and applies logic to each [Entity](xref:Microsoft.Xrm.Sdk.Entity). When some logic fails, you can pass the [Id](xref:Microsoft.Xrm.Sdk.Entity.Id) of the record to the `InvalidPluginExecutionException` constructor in the following way:

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

Add any other information relevant to the failure as string key-value pairs to the `exceptionDetails` parameter.

For `CreateMultiple`, we recommend that you don't set the primary key value for each record. In most cases, you should allow the system to set the primary key value for you because the values generated by the system are optimized for best performance.

In cases where the primary key value isn't set, if there's no other unique identifier, you may need to return the index of the failed record in the [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) `Targets` parameter, or some combination of values that uniquely identify the record that fails.

For instance, a key named `failedRecordIndex` indicating the record's place in the `EntityCollection`, or any other useful unique identifier, can be added to `exceptionDetails` to help troubleshoot the failure.

### Get exception details

When you have included details about the failing operation in the [InvalidPluginExecutionException.ExceptionDetails](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.ExceptionDetails) property, the client application can get these details from the [OrganizationServiceFault.ErrorDetails](xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails) property through the [FaultException&lt;OrganizationServiceFault&gt;.Detail](xref:System.ServiceModel.FaultException%601.Detail) property. The following code shows how:

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

If the client application is using Web API, they can get these details by setting the `Prefer: odata.include-annotations="*"` request header. More information: [Include more details with errors](webapi/compose-http-requests-handle-errors.md#include-more-details-with-errors).

In this way, the caller can know which record caused the failure and any other relevant details you want to include.

## Replace Single operation plug-ins in solution

When you deploy plug-in step registrations via solutions, there's currently no way to force an existing step registration to be disabled or deleted. Replacing logic from a single operation to a multiple operation plug-in is a challenge without a way to force the existing step registration to be deleted or disabled.

When you deploy a new plug-in step via a solution for `CreateMultiple` or `UpdateMultiple` that replaces a plug-in step for `Create` or `Update`, you want to mitigate the amount of time where no logic or duplicate logic is applied. You can manually disable the steps for `Create` or `Update` before or after installing the solution.

- If you disable before, there's a period where no logic is applied.
- If you disable after, there's a period where duplicate logic is applied.

In either case, the organization may require scheduled downtime to ensure logic is applied consistently.

To minimize the duration where either of the conditions above apply, we recommend you include the logic to disable any steps being replaced by deploying the new plug-ins with Package Deployer. Package Deployer provides the capability to execute custom code before, during, and after the package is imported into an environment. Use this code to disable the existing step registrations.

More information:

- [Create packages for the Package Deployer tool](/power-platform/alm/package-deployer-tool)
- [Add custom code](/power-platform/alm/package-deployer-tool#add-custom-code)

### See also

[Sample: CreateMultiple and UpdateMultiple plug-ins](org-service/samples/createmultiple-updatemultiple-plugin.md)   
[Bulk Operation messages (preview)](bulk-operations.md)   
[Sample: Use CreateMultiple and UpdateMultiple](org-service/samples/create-update-multiple.md)   
[Optimize performance for Create and Update operations](optimize-performance-create-update.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
