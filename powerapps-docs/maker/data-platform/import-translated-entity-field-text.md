---
title: "Import translated table and column text with Power Apps | MicrosoftDocs"
description: "Learn how to import translated table and column text"
ms.custom: ""
ms.date: 06/19/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 3d77d149-819b-45e6-8e70-1fbe54d5c153
caps.latest.revision: 19
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Import translated table, form, and column text back into an app

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

If you have customized table or column text, such as column labels or drop-down list values, you can provide the users in your organization who are not working with the base language version of your environment with this customized text in their own languages. To do so, you export the text strings for all your customizations so that they can be translated into the languages you use in your organization.  
  
 After the translation, you need to import the translated text strings into your environment before users can take advantage of the changes.  
  
> [!IMPORTANT]
> - The file that you import must be a compressed file that contains the CrmTranslations.xml and the [Content_Types].xml file at the root.  
> - You can’t import translated text that is over 500 characters long. If any of the items in your translation file are longer than 500 characters, the import process will fail. If the import process fails, review the line in the file that caused the failure, reduce the number of characters, and try to import again. Also note that after you import translated text, you must republish customizations.  
  
1. Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2. Select **Solutions**, and select the unmanaged solution from which to import the translated text.

3. In the solution explorer, on the Actions toolbar, select **Translations**, and then select **Import translations**.

4.  In the **Import Translated Text** dialog box, specify the file that contains the translated text, and then select **Import**.  
  
5.  When the import is complete, select **Close**.  
  
> [!NOTE]
>  Publishing customizations can interfere with normal system operation. We recommend you schedule publishing when it’s least disruptive to users.  

## Community tools

[Easy Translator](https://www.xrmtoolbox.com/plugins/MsCrmTools.Translator/) is a tool that XrmToolBox community developed for Power Apps. Use Easy Translator to export and import translations with contextual information. 

> [!NOTE]
> The community tools are not supported by Microsoft. 
> If you have questions about the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

## Next steps  
 [Export customized table and column text for translation](export-customized-entity-field-text-translation.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]