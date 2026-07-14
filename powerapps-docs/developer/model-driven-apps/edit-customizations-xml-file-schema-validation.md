---
title: "Edit the customizations XML file with schema validation (model-driven apps)"
description: "The customizations.xml file is included within the compressed .zip file exported as a solution. Certain portions of the customizations.xml file can be edited manually. Information about the schema helps you confirm that any modifications you make are valid."
author: caburk
ms.author: caburk
ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Edit the customizations XML file with schema validation

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
1. Right-click the customizations.xml file and select **Open With** and then select the version of [!INCLUDE[pn_Visual_Studio_short](../../includes/pn-visual-studio-short.md)].
1. Select **View** and then select **Properties Window**.
1. In the **Properties** window, in the **Schemas** column, click the ellipsis [**...**] button.
1. In the **Xml Schemas** dialog box you should see the customizationsSolution.xsd. In the **Use** column, select **Use this schema**.  
  
   > [!NOTE]
   >  If you do not see it, click **Add** and browse to where you saved it.  
  
1. Click **OK**.  
  
   You are now ready to begin editing the XML with XSD validation.  
  
### See also

[When to edit the customizations file for Microsoft Dataverse](when-edit-customization-file.md)  
[Ribbon core schema](ribbon-core-schema.md)  
[Ribbon types schema](ribbon-types-schema.md)  
[Ribbon WSS schema](ribbon-wss-schema.md)  
[Form XML schema](form-xml-schema.md)  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
