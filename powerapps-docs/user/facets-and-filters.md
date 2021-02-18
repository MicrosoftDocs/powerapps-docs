---
title: "Filter rows with facets| MicrosoftDocs"
description: How to Filter rows with facets.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 2/8/2021
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
---

# Configure facets and filters

With Dataverse, you can refine your search results by using facets and filters. Facets and filters let you drill into and explore the results of your current search without having to repeatedly refine your search terms.

In the Set **Personal Option**s dialog box, you can personalize the facets for a table. 

> [!NOTE]
> Your admin can use the Quick Find view to define which fields appear as default facets when you use Relevance Search. The first four view columns with data types other than single line of text and multiple lines of text are displayed as default facets in the result. You can override this setting in your [Personalization Settings](https://docs.microsoft.com/powerapps/user/set-personal-options#to-set-personal-options). At any time up to four fields can be selected as facets.
  
1. In the upper-right corner, select **Settings**, and then select **Personalization Settings**.  
  
   > [!div class="mx-imgBorder"]
   > ![Personalization Settings](media/personalization-settings.png "Personalization Settings")
  
2. On the **General** tab, in the **Select the default search experience** section, for the **Facets and Filters** column, select **Configure**.  

   > [!div class="mx-imgBorder"]
   > ![Configure Facets and Filters](media/configure-facets-filters.png "Configure Facets and Filters")  
  
3. In the **Configure Facets and Filters** dialog box, specify the facets you'd like to see for a table. 
  
   - In the **Select Table** drop-down list, select a table you want to configure facets for. This drop-down list contains only the tables that are enabled for Relevance Search.  
  
   - For the selected table, select up to four facet columns. By default, the first four "facet-able" columns in the **Quick Find** view for the selected table are selected in the list. At any time, you can only have four columns selected as facets.  
  
   You can update multiple tables at one time. When you select **OK**, the changes for all tables that you've configured are saved. To revert to the default behavior for a table that you previously configured, select **Default**.  
  
   > [!NOTE]
   > - If a system customizer deletes a column or makes it no longer searchable, and you've saved a facet for that column, it will no longer show up as a facet.  
   >   -   You'll only see the columns that exist in the default solution and that are configured as searchable by your system customizer.  
   
   
   ## See also

[What is Relevance Search](relevance-search-benefits.md)<br/>
[Search for tables and rows using Relevance Search](relevance-search.md)<br/>
[Frequently asked questions about Relevance Search](relevance-faq.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]