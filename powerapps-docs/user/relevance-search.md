---
title: "Share records using Access Team| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 12/11/2018
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
# Use Relevance Search 

you can search for records across multiple entities by using Relevance Search or Categorized Search. Relevance Search returns search results, sorted by relevance, in a single list. Categorized Search returns search results grouped by entity types, such as accounts, contacts, or leads. To find records of one type only, you can use the **Quick Find View** in the entity's grid.   
  
## What is Relevance Search?  
 Relevance Search delivers fast and comprehensive results across multiple entities in a single list, sorted by relevance. It uses a dedicated search service external to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] (powered by [!INCLUDE[pn_Windows_Azure](../includes/pn-windows-azure.md)]) to boost [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] search performance.  
  
 Relevance Search is available in addition to other [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] searches you are already familiar with. You can continue using single-entity Quick Find on the entity grid or Multi-Entity Quick Find (called Categorized Search, if you have Relevance Search enabled) by using **Search Dynamics 365 for Customer Engagement apps data** on the navigation bar. For more comprehensive and faster results, we recommend using Relevance Search.  

 Relevance Search brings the following enhancements and benefits:  
  
- Improves performance with external indexing and [!INCLUDE[pn_azure_shortest](../includes/pn-azure-shortest.md)] Search technology.  
  
- Finds matches to any word in the search term in any field in the entity. Matches can include inflectional words like **stream**, **streaming**, or **streamed**.  
  
- Returns results from all searchable entities in a single list sorted by relevance, based on factors like number of words matched or their proximity to each other in the text.  
  
- Highlights matches in the result list.  
  
> [!NOTE]
> - Relevance Search isn't available for [!INCLUDE[pn_crm_op_edition](../includes/pn-crm-onprem.md)] organizations.  
> - Relevance Search is disabled by default. Your administrator needs to enable it for the organization. After Relevance Search is enabled, you might have to wait up to an hour or more, depending on the size of your organization, before you start seeing Relevance Search results in the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] web application. Smaller changes in indexed data can take up to 15 minutes to show up in your system.
> - Enabling Relevance Search allows all users in the organization to use it.  
> - Relevance search is text-based, and can search only on fields of type Single Line of Text, Multiple Lines of Text, Option Sets, or Lookups. It doesn't support searching in fields of Numeric or Date data type. 
  
 Although Relevance Search finds matches to any word in the search term in any field in an entity, in Quick Find&mdash;even with full-text search enabled&mdash;all words from the search term must be found in one field.  
  
 In Relevance Search, the better the match, the higher it appears in the results. A match has a higher relevancy if more words from the search term are found in close proximity to each other. The smaller the amount of text where the search words are found, the higher the relevancy. For example, if you find the search words in a company name and address, it might be a better match than the same words found in a large article, far apart from each other. Because the results are returned in a single list, you can see a mix of records displayed one after another, such as accounts, opportunities, leads, and so on. The matched words in the list are highlighted.  
  
<a name="BKMK_Use_RelevanceSearch"></a>   
## Use Relevance Search  
 When Relevance Search is enabled for your organization, it becomes the default search experience. When you enter a search term in **Search Dynamics 365 for Customer Engagement apps data** on the navigation bar, and then select the Enter key or select the search button, the **Relevance Search** search results page appears. Search results are shown in a single list ordered by relevance. To learn how to change your default search experience, see [Select a default search experience](#BKMK_DefaultOption).  
  
 Start a new search by entering a search term in the **Relevance Search** search box or in the **Search Dynamics 365 for Customer Engagement appsdata** search box on the nav bar, as shown here.  
  
 ![Relevance Search](../basics/media/relevance-search.png "Relevance Search")  
  
 Use syntax in your search term to get the results you want. For example, type **car silver 2-door** to include matches for any word in the search term in the search results. Type **car+silver+2-door** to find only matches that include all three words. Type **car&#124;silver&#124;2-door** to  get results that contain **car** or **silver** or **2-door**, or all three words. More information about syntax you can use in your search queries: [Simple query syntax in Azure Search](https://docs.microsoft.com/rest/api/searchservice/simple-query-syntax-in-azure-search)


> [!NOTE]
> You'll see hit highlights when your search term matches a term in your app. The hit highlights appear as bold and italicized text in your search results. These are often returned as a portion of the full value in a field because only the matched terms are highlighted. 
  
 In [!INCLUDE[pn_crm_8_2_0_online](../includes/pn-crm-8-2-0-online.md)], the following enhancements have been made to the Relevance Search experience:  
  
- You'll find search results for text in a document that is stored in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)], including text in notes, email attachments, or appointments. The following file formats are supported for search: PDF, Microsoft Office documents, HTML, XML, ZIP, EML, plain text, and JSON.  
  
- You can search for records that are shared with you and records that you own.  
  
  > [!NOTE]
  >  Hierarchical security models aren't supported.  Even if you see a row in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] because you have access to it through hierarchical security, you won't see the result in Relevance Search.  
  
- You can also search for option sets  and lookups. For example, let's say you want to find a retail store account that has **Pharmaceuticals** in the name. When you search for **Pharmaceutical Retail**, you'll find the result because there's a match to the Industry field, which is a searchable option set.  
  
  Because your results might include a mix of entities, you can narrow your search results to a specific entity by selecting an entity in the **Filter with** drop-down list. When you filter on a specific record type, you can include activities and notes related to the selected record in your search results. To do that, select the **Search activities and notes for selected records** check box to the right of the **Filter with** drop-down list. The check box is selected after you select a record in the **Filter with** drop-down list; it is cleared if you didn't select an entity in the **Filter with** list. The activities and notes are returned as top-level results.  
  
<a name="BKMK_FilterWithFacets"></a>   
## Filter records with facets  
 With [!INCLUDE[pn_crm_8_2_0_online](../includes/pn-crm-8-2-0-online.md)], you can now refine your search results by using facets and filters. Facets are available in the left pane. Immediately after you perform a search, the following global facets are available for four common fields:  
  
-   Record Type  
  
-   Owner  
  
-   Created On  
  
-   Modified On  
  
### Record Type facets  
 To narrow your search results to a specific entity, select the entity under the **Record Type** section.  
  
 ![Record Type facet to narrow the search results](../basics/media/relevance-search-record-type-facet.png "Record Type facet used to narrow search results")  
  
 When you filter on a specific record type, you can include activities and notes that are related to the selected record in your search results. To do that, select the **Related Notes & Activities** check box. The activities and notes will appear in top-level results.  
  
 ![Include notes and activities related to a record type in the search results](../basics/media/relevance-search-record-type-facet-related-notes-activities.png "Include notes and activities related to a record type in the search results")  
  
 Search results that are found in email attachments or appointment entities  are shown in the search results under their parent record, either Email or Appointment.  
  
 When you refine by record type, the facet scope switches to the selected entity, and up to four facets that are specific to the entity are shown. For example, if you select the Account entity, you'll see the **Primary Contact** facet in addition to the global facets.  
  
 In the **Set Personal Options** dialog box, you can also choose other facets from the ones that your system administrator or customer has made available to you. The user setting overrides the default setting. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Configure facets and filters for the search](#BKMK_ConfigureFacets)  
  
### Text-based facets  
 All lookups, option sets, and record types are text-based facets. For example, the text-based facet Owner consists of a list of field values and their corresponding counts.  
  
 ![Text-based facet in Relevance Search](../basics/media/relevance-search-text-based-facets.png "Text-based facet in Relevance Search")  
  
 Filters in these facets are sorted in descending order by count. The top four facet values are displayed by default. When there are more than four facet values, you'll see a **SHOW MORE** link that you can select to expand the list and see up to 15 top facet values. Select each value to filter the search results to show only records where the field has the value you've selected. For example, if you select **Kim Abercrombie**, the search results will show all records where the owner is Kim Abercrombie. When you select a Lookup or Option Set facet value, search results are filtered to only include records with the value that you specified.  
  
### Date and time facets  
 Like other facets, you can use date and time facets to filter and see search results for a specific time. To select a range of values, drag the slider or select one of the vertical columns.  
  
 ![Date and time facets for Relevance Search](../basics/media/relevance-search-date-time-facets.png "Date and time facets for Relevance Search")  
  
<a name="BKMK_ConfigureFacets"></a>   
## Configure facets and filters for the search  
 Facets and filters let you drill into and explore the results of your current search without having to repeatedly refine your search term. Configure the facets and filters you want in the **Set Personal Options** dialog box.  
  
> [!NOTE]
>  The system customizer can set the default experience for all entities, but you can configure your own facets and filters.  
  
#### To configure facets for yourself  
  
1. Select the personal settings button in the upper-right corner of the page, and then select **Options**.  
  
   ![Select default search experience](../basics/media/relevance-search-personal-settings.PNG "Select default search experience")  
  
2. On the **General** tab, in the **Select the default search experience** section, for the **Facets and Filters** field, select **Configure**.  
  
3. In the **Configure Facets and Filters** dialog box, specify the facets you'd like to see for an entity. Your system administrator or customizer can set a default experience for all entities, but you can set your own here.  
  
   - In the **Select Entity** drop-down list, select an entity you want to configure facets for. This drop-down list contains only the entities that are enabled for Relevance Search.  
  
   - For the selected entity, select up to four facet fields. By default, the first four facetable fields in the **Quick Find** view for the selected entity are selected in the list. At any time, you can only have four fields selected as facets.  
  
     You can update multiple entities at one time. When you select **OK**, the changes for all entities that you've configured are saved. To revert to the default behavior for an entity that you previously configured, select **Default**.  
  
   > [!NOTE]
   > - If a system customizer deletes a field or makes it no longer searchable, and you've saved a facet for that field, it will no longer show up as a facet.  
   >   -   You'll only see the fields that exist in the default solution and that are configured as searchable by your system customizer.  
  
<a name="BKMK_CategorizedSearch"></a>   
## Switch to Categorized Search  
 Categorized Search returns results grouped by entity, such as accounts, contacts, or leads.  
  
> 
>  You can further narrow the search results by using the **Filter with** drop-down list to see the results for a specific entity. To switch from Relevance Search to Categorized Search, select **Relevance Search**, and then select **Categorized Search** from the drop-down list. To switch back to Relevance Search, select **Categorized Search**, and then select **Relevance Search**.  
  
 ![Categorized Search](../basics/media/relevance-search-categorized-search.png "Categorized Search")  
  
 [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Search for records](../basics/search-records.md)  
  
<a name="BKMK_DefaultOption"></a>   
## Select a default search experience  
 You can choose a default search experience for your browser from the following choices:  
  
- Relevance Search  
  
- Categorized Search  
  
- Use last search  
  
  The **Use last search** selection provides the last search experience you used in the current browser client. For example, if you used Relevance Search for your last search, the system will continue using this search until you manually switch to Categorized Search.  
  
To select the default search experience, do the following:  
  
1. Select the personal settings button in the upper-right corner of the page, and then select **Options**.  
  
   ![Select default search experience](../basics/media/relevance-search-personal-settings.PNG "Select the default search experience")  
  
2. On the **General** tab, use the **Select the default search experience** drop-down list to choose **Relevance Search**, **Categorized Search**, or **Use last search**.  
  
<a name="BKMK_PrivacyNotice"></a>   
## Privacy notice  
[!INCLUDE[cc_privacy_crm_relevance_search](../includes/cc-privacy-crm-relevance-search.md)]
