---
title: "Import solutions | MicrosoftDocs"
description: "Learn how to import a solution in Power Apps"
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
ms.assetid: 56363ea3-ea76-4311-9b7a-b71675e446fb
caps.latest.revision: 57
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Import solutions 

 You can import solutions manually using the steps below. Only import solutions that you've obtained from a trusted source. Customizations might include code that can send data to external sources.   
  
1.  Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation.  
  
2.  On the command bar, select **Import**.  

    > [!div class="mx-imgBorder"]  
    > ![Import solution](media/solution-import.png "Import solution") 
  
3.  On the **Select Solution Package** page, select **Browse** to locate the compressed (.zip or .cab) file that contains the solution you want to import. 
  
4.  Select **Next**.  
  
5.  Information about the solution is displayed. Select **Import**.  
  
6. You may need to wait a few moments while the import completes. View the results and then select **Close**.  
  
 If you have imported any changes that require publishing, you must publish customizations before they are available. 
  
 If the import isn’t successful, you will see a report showing any errors or warnings that were captured. Select **Download Log File** to capture details about what caused the import to fail. The most common cause for an import to fail is that the solution did not contain some required components.  
  
 When you download the log file, you will find an XML file that you can open using Office Excel to view the contents.  
  
> [!NOTE]
>  You can’t edit an active routing rule set. Therefore, if you’re importing a solution that includes an active routing rule set into an environment where the rule already exists with the same ID, the import will fail. More information: [Create rules to automatically route cases](https://docs.microsoft.com/dynamics365/customer-engagement/customer-service/create-rules-automatically-route-cases)  
  
<a name="BKMK_UpdateSolutions"></a>   

### See also
[Update solutions](update-solutions.md) <br />
[Export solutions](export-solutions.md)

