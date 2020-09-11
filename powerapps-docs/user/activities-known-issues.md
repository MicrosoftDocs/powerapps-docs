---
title: "Known issue for activities| MicrosoftDocs"
description: Known issue for activities|
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 09/11/2020
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Known issues for activities

## Email from

### Email content is lost after entering text in the description field on a email form 

**Issue**: While composing an email and filling the description field if **Save** or **Save and Close** or **Send** is selected immediately after entering text in the description field, the most recent content added to the email from may get lost. 

**Resolution**: As a general guideline please wait a few seconds before you select **Save** or **Save and Close** or **Send** after text is entered in the description field. 

### The From field is read only or look for records search isn't working

**Issue**: The **From** field in an email form is read-only or you can't look up records and filter results by **User** or **Queue**.

**Resolution**: This happens when your system admin has customizated parts of the form. To fix the issue, open a browser window and run the following two commands replacing **envioment URL** with your environment URL.
    
 - (envioment URL)/api/data/v9.1/RemoveActiveCustomizations(SolutionComponentName='AttributeLookupValue',ComponentId=(25E9AF0C-2341-DB11-898A-0007E9E17EBD))
 - (envioment URL)/api/data/v9.1/RemoveActiveCustomizations(SolutionComponentName='AttributeLookupValue',ComponentId=(26E9AF0C-2341-DB11-898A-0007E9E17EBD))
 



