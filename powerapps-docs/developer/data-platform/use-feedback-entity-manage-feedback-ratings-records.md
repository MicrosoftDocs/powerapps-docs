---
title: "Use the Feedback table to manage feedback and ratings for records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the feedback table to obtain feedback and ratings for the records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/27/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use the Feedback table to manage feedback and ratings for records

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]


Improve your products and services by enabling users to provide feedback and ratings for rows in Microsoft Dataverse. For example, you can enable feedbacks and ratings for the `Product` table to know user's feedback on the products you sell, or on the `Incident` (case) table to understand and improve the quality of your customer support team.  
  
 You can enable feedback and rating for both system and custom tables in Dataverse. By default, the `KnowledgeArticle` table is enabled for feedback and ratings. Use the new `Feedback` table to programmatically create and manage feedback for records.  
  
 To programmatically enable feedback for a:  
  
- System table, use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> message to update the table, and set the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest.HasFeedback> property to true.  
  
- Custom table, set the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.HasFeedback> property to true  while creating the table, or update existing custom table to set the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest.HasFeedback> property to true.  
  
  Once you have enabled a table for feedback and rating, you can't disable it. After you enable a table for feedback, a regarding relationship is created between the table and the `Feedback` table.  
  
> [!NOTE]
>  You can also use the customization tools in Dataverse to enable feedback and rating for system and custom entities.  
  
 The `Feedback` table stores the following information :  
  
- Feedback title  
  
- Feedback comments  
  
- Feedback rating. You can also define a range for ratings by specifying a minimum and maximum (numerical) value for ratings. For example, a rating of 4 on the scale of 1-5.  
  
- Normalized rating for feedback that is automatically calculated  to show the specified user rating scaled to a value between 0 and 1 based on the minimum and maximum rating values.  
  
  > [!NOTE]
  >  The normalized rating helps to normalize or even out the specified rating value for different rating ranges (minimum and maximum rating values). The normalized  rating is calculated as follows: (Rating - Minimum Rating) / (Maximum Rating - Minimum Rating).  
  >   
  >  Also, rating for a row is calculated as an average of all the normalized ratings for the record.  
  
- Feedback status such as Open or Closed  
  
- Feedback source to display the source from where the feedback was submitted. If the feedback was created from within Dataverse, the value is set to **Internal**. Developers can add a value of their choice depending on the application used to provide feedback.  
  
- User who created or last modified the feedback record  
  
- Table row that the feedback is associated with  
  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
