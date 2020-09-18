---
title: "Known issue for activities| MicrosoftDocs"
description: Known issue for activities|
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 09/14/2020
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

## Email content is lost after entering text in the body of the message

**Issue**: Recent content added to the email may get lost if you enter text in the body of an email and immediately select **Save**, **Save and Close**, or **Send**. 

**Resolution**: To avoid this issue, wait a few seconds before you select **Save**, **Save and Close**, or **Send** after your enter text in the body of the email.

## The From field is read only or lookup isn't working

**Issue**: The **From** field in an email form is read-only or you can't look up records and filter results by **User** or **Queue**.

**Resolution**: This happens when customization specifically have been applied on this field by your system administrator. To fix the issue, open a browser window and run the following two commands replacing the **environment URL** with the URL of your environment.


 - (replace with your environment URL)/api/data/v9.1/RemoveActiveCustomizations(SolutionComponentName='AttributeLookupValue',ComponentId=(25E9AF0C-2341-DB11-898A-0007E9E17EBD))
 - (replace with your environment URL)/api/data/v9.1/RemoveActiveCustomizations(SolutionComponentName='AttributeLookupValue',ComponentId=(26E9AF0C-2341-DB11-898A-0007E9E17EBD))
 
To find the URL, in the address bar the first part of the URL that starts with **https://** and ends with **.com** is your environment URL. For more information on how to find the environment URL, see [Get the environment UR](https://docs.microsoft.com/power-platform/guidance/coe/setup-powerbi#get-the-environment-url).

