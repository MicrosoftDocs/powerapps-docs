---
title:  Tips when working with low-code plug-ins in Microsoft Dataverse (preview)
description: Describes tips and known issues when working with low-code plug-ins in Microsoft Dataverse
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 05/06/2024
ms.custom: template-how-to
---
# Microsoft Dataverse low-code plug-ins tips and known issues (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article describes tips and known issues when working with low-code plug-ins in Microsoft Dataverse.

> [!IMPORTANT]
>
> - Instant low-code plug-ins are deprioritized and aren't being delivered as a feature. Instant low-code plug-ins are replaced with functions. More information: [Functions in Microsoft Dataverse (preview)](functions-overview.md)
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Handle general runtime issues

If you face runtime plugin issues, re-edit the low-code plug-in. Then the intellisense issues on your formula expression are displayed in the low-code plug-in editor. Follow the guidelines to correct the issue that are also displayed, and then resave the plug-in.  

## Use caution when using post-operation patching

Your low-code plug-in execution might encounter this error when using `Patch` in a post-operation: `Execution failed for PowerPlexPlugin: System.ServiceModel.FaultException 1[Microsoft.Xrm.Sdk.OrganizationServiceFault] This low-code plugin's execution was cancelled because the plugin logic caused an infinite loop. Correct the plugin logic and try again.`

Using `Patch` in a post-operation scenario must be done with caution to avoid infinite loops. A `Patch` operation initiates a new transaction. For example, if an update trigger for `MyTable` invokes `Patch(MyTable, ThisRecord, ...)`, this operation might result in a recursive update cycle.

Here are a couple of examples of operations that can avoid this issue:

- `Patch(CurrentTable, SomeOtherRecord, ... ) // For example, updating a manager's contact from a contact record.`
- `Patch(OtherTable, SomeOtherRecord, ... )   // Operations on a completely different table.`  

## Handle the two-minute timeout

For operations that continue for two minutes or longer, you can receive this error:  

`Execution failed for PowerPlexPlugin: System.ServiceModel.FaultException1[Microsoft.Xrm.Sdk.OrganizationServiceFault]: Operation not allowed as plugin execution exceeded maximum allowed time (Fault Detail is equal to Exception details: limit your callbacks .. Create, Update)`

When working with Dataverse low-code plugins, it’s important to manage the two-minute timeout effectively:

- Limit your number of `Patch` and `Collect` operations inside your plug-ins, especially if you have other plug-ins already registered against that table, which can affect the performance of your plug-ins.
- Monitor performance. Keep an eye on the performance of your plug-ins and consider using tracing and logging capabilities within Dataverse to track execution times and failures. By following these guidelines, you can ensure that your low-code plug-ins run smoothly within the Dataverse environment without interruption caused by the two-minute timeout. More information: [Tracing and logging](/power-apps/developer/data-platform/logging-tracing)

## Failed response received from APIM

If you receive this error message, which can be returned from API management (APIM), just edit the plug-in, and then resave. Saving initializes the APIM authentication and your plug-in begins executing successfully.

`Execution failed for PowerPlexPlugin: Failed response received from APIM; StatusCode: NotFound; ResponseContent: { "statusCode": 404, "message": "Resource not found" } Method: POST; RequestUri: https://canada-001.azure-apim.net/invoke; StatusCode: NotFound; ResponseContent: { "statusCode": 404, "message": "Resource not found" }; HeadersString: Headers - 'Access-Control-Allow-Methods': 'System.String[]'; 'Access-Control-Allow-Origin': 'System.String[]'; 'Access-Control-Max-Age': 'System.String[]'; 'Access-Control-Expose-Headers': 'System.String[]'; 'Date': 'System.String[]';  Access to APIM expires..edit and save the plugin`

## See also

[Use low-code plug-ins in Dataverse](low-code-plug-ins.md)