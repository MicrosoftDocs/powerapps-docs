---
title: "Customization XML reference (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "The customizations.xml file is one of the files included in an exported unmanaged solution. The file contains all or selected portions of the customizations and configurations for your system" # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 864699de-c22f-3504-f120-84ca5a4aeca6
author: JimDaly" # GitHub ID
ms.author: jdaly" # MSFT alias of Microsoft employees only
manager: shilpas" # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Customization XML reference

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customization-xml-reference -->

The customizations.xml file is one of the files included in an exported unmanaged solution. The file contains all or selected portions of the customizations and configurations for your system. 
  
 The solutions file is exported as a compressed .zip file. The contents of the unmanaged solutions file must be extracted before the customizations file can be edited. All the files of the unmanaged solution must be added to a compressed .zip file before it can be re-imported.  

> [!NOTE]
> - Editing a managed solution file is not supported.  
> - Not all elements of the customizations.xml file can be edited. More information: [Support for Editing the Customization File](../common-data-service/when-edit-customization-file.md)

## In This Section

 [Ribbon core schema](ribbon-core-schema.md) 
 [Ribbon types schema](ribbon-types-schema.md)  
 [Ribbon WSS schema](ribbon-wss-schema.md)  
 [SiteMap schema](/dynamics365/customer-engagement/developer/customize-dev/sitemap-schema) <!-- TODO need to fix the link> 
 [Form XML schema](form-xml-schema.md) 
 [FetchXML schema](../common-data-service/fetchxml-schema.md) 

## Related Sections

 [Schemas used in Dynamics 365](/dynamics365/customer-engagement/developer/schemas-used-dynamics-365) <!-- TODO need to fix the link> 
 [When to Edit the Customizations File](../common-data-service/when-edit-customization-file.md)  
[Edit the Customizations file with Schema Validation](edit-customizations-xml-file-schema-validation.md)  
 [Customize the Ribbon for Dynamics 365](customize-commands-ribbon.md)  
 [Change Application Navigation using the SiteMap](/dynamics365/customer-engagement/developer/customize-dev/change-application-navigation-using-sitemap) <!-- TODO need to fix the link> 