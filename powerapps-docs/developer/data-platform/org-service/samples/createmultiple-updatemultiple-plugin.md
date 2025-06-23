---
title: "Sample: CreateMultiple and UpdateMultiple plug-ins (Microsoft Dataverse) | Microsoft Docs"
description: "This sample shows how to write plug-ins for the CreateMultiple and UpdateMultiple messages"
ms.date: 06/01/2023
author: MsSQLGirl
ms.author: jukoesma
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

This sample on GitHub provides several Plug-in types that demonstrate how to write plug-ins for the `CreateMultiple` and `UpdateMultiple` messages.

> [!IMPORTANT]
> The plug-ins in this sample are designed to work together with the operations in [Sample: SDK for .NET Use bulk operations](create-update-multiple.md). If you want to test these plug-ins, you need to:
>  1. Build the solution to create the assembly.
>  1. Run one or more of the projects in the [Sample: SDK for .NET Use bulk operations](create-update-multiple.md)
>  
>     - **Note**: Use the option to NOT delete the table at the end of the sample.
>  
>  1. Register the assembly using the Plug-in registration tool (PRT).
>  1. Register steps for the plug-in as described in the README.
>  1. Run one or more of the projects in the [Sample: SDK for .NET Use bulk operations](create-update-multiple.md) to test the plug-ins.

See the README.md file in the sample for detailed instructions about how to run the sample and what it does.

> [!div class="nextstepaction"]
> [SDK for .NET Create and Update Multiple Sample](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp/xMultiplePluginSamples/README.md)


### See Also

[Write plug-ins for CreateMultiple and UpdateMultiple](../../write-plugin-multiple-operation.md)   
[Bulk Operation messages](../../bulk-operations.md)   
[Sample: SDK for .NET Use bulk operations](create-update-multiple.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]