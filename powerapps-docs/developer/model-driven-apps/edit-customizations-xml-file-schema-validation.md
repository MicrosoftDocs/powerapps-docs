---
title: "Edit the customizations XML file with schema validation (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "The customizations.xml file is included within the compressed .zip file exported as a solution. Certain portions of the customizations.xml file can be edited manually. Information about the schema helps you confirm that any modifications you make are valid." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.custom:
  - ""
ms.topic: article
ms.assetid: b77d962e-6e3c-bd28-d03c-cf2e23cd742d
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

# Edit the customizations XML file with schema validation

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-dev/edit-customizations-xml-file-schema-validation -->

The customizations.xml file is included within the compressed .zip file exported as a solution. Certain portions of the customizations.xml file can be edited manually. Information about the schema helps you confirm that any modifications you make are valid.  
  
## XSD schema files  
 [!INCLUDE[schema_download](../../includes/schema-download.md)] for the XSD schema files used to validate the customization.xml file in a solution. The necessary files are:  
  
- CustomizationsSolution.xsd  
  
- fetch.xsd  
  
- FormXml.xsd  
  
- isv.config.xsd  
  
- RibbonCore.xsd  
  
- RibbonTypes.xsd  
  
- RibbonWSS.xsd  
  
- SiteMap.xsd  
  
- SiteMapType.xsd  
  
- VisualizationDataDescription.xsd  
  
  
<a name="BKMK_UseSchemaValidation"></a>

## Using schema validation  

Because the exported XML is a text file, you can edit it using a text editor such as [!INCLUDE[pn_Notepad](../../includes/pn-notepad.md)]. However, we strongly recommend that you use an application that supports XSD schema validation such as [!INCLUDE[pn_Visual_Studio](../../includes/pn-visual-studio.md)]. XSD validation in [!INCLUDE[pn_Visual_Studio](../../includes/pn-visual-studio.md)] <!-- TODO - need to fix this link. The page is not available (or [Visual Studio Express 2012 for Web](https://www.microsoft.com/visualstudio/eng/products/visual-studio-express-for-web))--> provides [!INCLUDE[pn_IntelliSense](../../includes/pn-intellisense.md)] information and schema validation to help prevent errors.  
  
The XSD schema files that are used to validate the customization.xml file in a solution are available here. [!INCLUDE[schema_download](../../includes/schema-download.md)]. Make sure to copy all the files from that folder into the same directory. You will need to associate the customizations.xml file to the CustomizationsSolution.xsd file. That file has links to all the other XSD files in the folder.  
  
1. Download the XSD schema files and copy all of them to your computer. Save them in the location that [!INCLUDE[pn_Visual_Studio](../../includes/pn-visual-studio.md)] uses for XSD validation files. This location is probably `[install drive]\Program Files (x86)\Microsoft Visual Studio X.0\Xml\Schemas` where `X` represents the version of [!INCLUDE[pn_Visual_Studio_short](../../includes/pn-visual-studio-short.md)].  
  
2. Right-click the customizations.xml file and select **Open With** and then select the version of [!INCLUDE[pn_Visual_Studio_short](../../includes/pn-visual-studio-short.md)].  
  
3. Select **View** and then select **Properties Window**.  
  
4. In the **Properties** window, in the **Schemas** column, click the ellipsis [**...**] button.  
  
5. In the **Xml Schemas** dialog box you should see the customizationsSolution.xsd. In the **Use** column, select **Use this schema**.  
  
   > [!NOTE]
   >  If you do not see it, click **Add** and browse to where you saved it.  
  
6. Click **OK**.  
  
   You are now ready to begin editing the XML with XSD validation.  
  
### See also

[When to edit the customizations file for Microsoft Dataverse](when-edit-customization-file.md)<br/> 
[Ribbon core schema](ribbon-core-schema.md)<br/>
[Ribbon types schema](ribbon-types-schema.md)<br/>
[Ribbon WSS schema](ribbon-wss-schema.md)<br/>
[Form XML schema](form-xml-schema.md)     
[ISV configuration file schema](/dynamics365/customer-engagement/developer/customize-dev/isv-configuration-file-schema)<br/>   <!-- TODO need to fix link relevant to the topic in powerapps repo-->



[!INCLUDE[footer-include](../../includes/footer-banner.md)]