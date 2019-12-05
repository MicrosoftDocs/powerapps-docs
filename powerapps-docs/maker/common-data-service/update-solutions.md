---
title: "Update solutions | MicrosoftDocs"
description: "Learn how to update a solution in Power Apps"
ms.custom: ""
ms.date: 09/30/2019
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
ms.assetid: 
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Update solutions  

There are times when you may wish to install an update to an existing managed solution. The procedure is similar to installing a new managed solution, except you will get some different options. If you are updating a solution you got from someone else, you should get guidance from the solution publisher about which options you should choose.  
  
1.  Select **Solutions** from the left navigation.
  
2.  In the solutions list menu select **Import**.  
  
3.  In the **Import Solution** dialog **Select Solution Package** step, select **Choose file** and browse to the compressed (.zip or .cab) file that contains the solution you want to update.

4.  Select **Next**.  
  
5.  View information about the solution and then select **Next**. This page will display a yellow bar saying **This solution package contains an update for a solution that is already installed**.  
  
6.  You will have the following options:  
  
    - **Maintain customizations (recommended)**  
  
         Selecting this option will maintain any unmanaged customizations performed on components but also implies that some of the updates included in this solution will not take effect.  
  
    - **Overwrite Customizations**  
  
         Selecting this option overwrites any unmanaged customizations previously performed on components included in this solution. All updates included in this solution will take effect.  
  
     Choose the appropriate option and then select **Next**.  
  
7.  You may need to wait a few moments while the import completes. View the results and then select **Close**.  
  
 If you have imported any changes that require publishing, you must publish customizations before they are available. 
  
 Solution publishers may ask you to export your existing unmanaged customizations, update their managed solution using the option to overwrite customizations, and then re-import your unmanaged customizations. This will help ensure that the changes they are expecting are applied while preserving your customizations.  
  
<a name="BKMK_ExportSolutions"></a>   

### See also
[Export solutions](export-solutions.md) 
[Distribute solutions and patches](use-segmented-solutions-patches-simplify-updates.md) 
[Import solutions](import-update-export-solutions.md)