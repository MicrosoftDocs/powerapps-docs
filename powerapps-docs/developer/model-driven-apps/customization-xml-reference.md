---
title: "Customization XML reference (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "The customizations.xml file is one of the files included in an exported unmanaged solution. The file contains all or selected portions of the customizations and configurations for your system" # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: article
ms.assetid: 864699de-c22f-3504-f120-84ca5a4aeca6
author: Nkrb # GitHub ID
ms.subservice: mda-developer
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Customization XML reference

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customization-xml-reference -->

The customizations.xml file is one of the files included in an exported unmanaged solution. The file contains all or selected portions of the customizations and configurations for your system. 
  
 The solutions file is exported as a compressed .zip file. The contents of the unmanaged solutions file must be extracted before the customizations file can be edited. All the files of the unmanaged solution must be added to a compressed .zip file before it can be re-imported.  

> [!NOTE]
> - Editing a managed solution file is not supported.  
> - Not all elements of the customizations.xml file can be edited. More information: [Support for Editing the Customization File](/power-platform/alm/when-edit-customization-file)

## In This Section

 [Ribbon core schema](ribbon-core-schema.md) 
 [Ribbon types schema](ribbon-types-schema.md)  
 [Ribbon WSS schema](ribbon-wss-schema.md)  
 [Form XML schema](form-xml-schema.md)  
 [FetchXML schema](../data-platform/fetchxml-schema.md) 

## Related Sections

[When to edit the customizations file](/power-platform/alm/when-edit-customization-file)  
[Edit the Customizations file with schema validation](edit-customizations-xml-file-schema-validation.md)  
[Customize the Ribbon for Dynamics 365](customize-commands-ribbon.md)  
[Change application navigation using the SiteMap](../../maker/model-driven-apps/create-site-map-app.md) 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]