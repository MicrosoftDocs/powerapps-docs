---
title: "Use XRM tooling to execute actions in Microsoft Dataverse (Dataverse) | Microsoft Docs"
description: "A CrmServiceClient class instance can be used to perform create, retrieve, update and delete operations on Microsoft Dataverse data"
ms.date: 01/30/2023
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - phecke
---
# Use XRM tooling to execute actions in Microsoft Dataverse

After you are connected to Dataverse, you can use the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> or <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class object to perform actions on your Dataverse data such as create, update, retrieve or delete data. This section provides some examples on how you can perform actions in Dataverse using XRM tooling. 

> [!IMPORTANT]
> While XRM tooling APIs including the [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) class continue to be supported, it is recommended that all new app development use the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class for web service connections and operations. If you need to use the WPF Login Control or the PowerShell module, continue using XRM tooling for those.
  
## In This Section

[Create data using XRM tooling](use-xrm-tooling-create-data.md)<br />
[Retrieve data using XRM tooling](use-xrm-tooling-retrieve-data.md)<br />
[Update data using XRM tooling](use-xrm-tooling-update-data.md)<br />
[Delete data using XRM tooling](use-xrm-tooling-delete-data.md)<br />
[Execute organization request using XRM tooling](use-messages-executecrmorganizationrequest-method.md)
  
### See also

[Use XRM Tooling API to connect to Dataverse](use-crmserviceclient-constructors-connect.md)  
[Build windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
