---
title: Write plug-ins for CreateMultiple and UpdateMultiple | Microsoft Docs
description: How to write plug-ins for CreateMultiple and UpdateMultiple messages.
author: divkamath
ms.topic: article
ms.date: 12/12/2022
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
---
# Write plug-ins for CreateMultiple and UpdateMultiple (Preview)

> [!NOTE]
> Not all tables currently support using the `CreateMultiple` and `UpdateMultiple` messages. This capability is currently being deployed and all tables that currently support `Create` and `Update` will support `CreateMultiple` and `UpdateMultiple` in the coming months. More information: [Use CreateMultiple and UpdateMultiple (Preview)](org-service/use-createmultiple-updatemultiple.md)

You should write plug-ins for the `CreateMultiple` and `UpdateMultiple` messages with tables where records may need to be created or updated in bulk, or when performance in creating and updating large numbers of records is important. This is true for just about every table that stores business data.

If you have existing plug-ins for the `Create` and `Update` messages for tables like these, you should migrate them to use `CreateMultiple` and `UpdateMultiple` instead.

## Is updating plug-ins required?

There is no requirement to migrate your plug-ins to use `CreateMultiple` and `UpdateMultiple` instead of `Create` and `Update`. Your logic will continue to be applied when applications use `CreateMultiple` or `UpdateMultiple`. This is because the Dataverse message processing pipeline merges the logic for plugins written for either the single or multiple version of the `Create` and `Update` messages. More information: [Message pipelines merged](org-service/use-createmultiple-updatemultiple.md#message-pipelines-merged)

However, only plug-ins written for the multiple version of these messages will enable optimum performance when developers use `CreateMultiple` and `UpdateMultiple`. Over time, as more applications choose to optimize performance by using the `CreateMultiple` and `UpdateMultiple` messages, we expect writing plug-ins for multiple operations will become the standard, and plug-ins written for single operations will be the exception.

## What is different?

The following are some of the differences you will need to manage when migrating existing plugins to the multiple version.

### Targets instead of Target

The multiple version of these messages has a `Targets` parameter that is an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) rather than a `Target` parameter that is a single [Entity](xref:Microsoft.Xrm.Sdk.Entity). Your plug-in code will need to loop through the entities in the collection and apply logic for each one.

### Entity Images

Entity images configured in the step registration for your plug-ins are an array of [EntityImageCollection](xref:Microsoft.Xrm.Sdk.EntityImageCollection). These entity images are only available when you use the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4> [IPluginExecutionContext4 Interface](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4) which provides the [PreEntityImagesCollection](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4.PreEntityImagesCollection) and [PostEntityImagesCollection](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext4.PostEntityImagesCollection) properties. These arrays provide access to the same entity images in an array that is synchronized with the EntityCollection.

If you are using the `PluginBase` class that is the standard when initializing plug-in projects using Power Platform tools, in the `PluginBase.cs` file you should replace all instances of `IPluginExecutionContext` with `IPluginExecutionContext4` so that these collections of entity images are available to your plug-in.

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

### See also

[Sample: CreateMultiple and UpdateMultiple plug-ins](org-service/samples/createmultiple-updatemultiple-plugin.md)<br />
[Use CreateMultiple and UpdateMultiple (Preview)](org-service/use-createmultiple-updatemultiple.md)<br />
[Sample: Use CreateMultiple and UpdateMultiple](org-service/samples/create-update-multiple.md)<br />
[Optimize performance for Create and Update operations](optimize-performance-create-update.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
