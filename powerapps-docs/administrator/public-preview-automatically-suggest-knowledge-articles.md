---
title: "Preview feature: Automatically suggest knowledge articles with Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.custom: ""
ms.date: 09/30/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: ee417009-afaf-4a63-9d8b-ef756a37decf
caps.latest.revision: 10
author: "Mattp123"
ms.author: "matp"
manager: "brycho"
---
# Preview feature: Automatically suggest knowledge articles

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

You want your customer service reps to quickly resolve cases with high customer satisfaction. By using the [!INCLUDE[pn_MicrosoftCognitiveServices_full](../includes/pn-microsoftcognitiveservices-full.md)] Text Analytics service with [!INCLUDE[pn_ms_dyn_365](../includes/pn-ms-dyn-365.md)], you can set up service case analysis to automatically provide your support staff with more relevant solutions from knowledge articles. They'll spend less time searching for answers and more time providing the correct response. The knowledge article suggestion feature includes support for both out-of-box entities and custom entities with a one-to-may (1:N) or many-to-one (N:1) relationship to the source entity.  
  
> [!IMPORTANT]
> - This feature is currently only available for instances in the United States (US) region.  
> - [!INCLUDE[cc_preview_features_definition](../includes/cc-preview-features-definition.md)]  
> - [!INCLUDE[cc_preview_features_expect_changes](../includes/cc-preview-features-expect-changes.md)]  
> - [!INCLUDE[cc_preview_features_no_MS_support](../includes/cc-preview-features-no-ms-support.md)]  
>   
> **Send us feedback**  
>   
>  We'd love your feedback on the knowledge article suggestions feature! To send us your feedback, register your account on the [Microsoft Connect site](https://connect.microsoft.com/site687), and then [submit your feedback](https://connect.microsoft.com/site687/Feedback/LoadSubmitFeedbackForm?FormID=5908).  
  
<a name="BKMK_EnablePreview"></a>   

## Enable Text Analytics  
 To enable Text Analytics, do the following:  
  
1. [!INCLUDE[proc_settings_administration](../includes/proc-settings-administration.md)]  
  
2.  Click **System Settings** and open the **Previews** tab.  
  
3.  Under **Text Analytics Preview for Case Topic analysis, Suggest Similar Cases and Suggest Knowledge Articles**, set the **Enable Dynamics 365 Text Analytics Preview** to **Yes**.  
  
4.  Click **OK** to give your consent.  
  
5.  Click **OK** to close the **System Settings** dialog.  
  
<a name="BKMK_ConnectTextAnalytics"></a>   

## Connect Dynamics 365 (online) to the Cognitive Services Text Analytics service  
 If you haven't already, create the [!INCLUDE[pn_CognitiveServices_short](../includes/pn-microsoftcognitiveservices-short.md)] Text Analytics service connection. [Set the Azure Machine Learning text analytics connection](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#Set_AzureMLconnection)  
  
<a name="BKMK_SetUpKnowledgeSearch"></a>   

## Set up Knowledge Search field settings  
 Set up keyword or key phrase determination fields to search knowledge articles to help resolve service cases.  
  
1.  Click **Settings** > **Service Management** > **Knowledge Search Field Settings**.  
  
2.  Click **New**.  
  
3.  Fill in the fields on the New Knowledge Search Model dialog.  
  
    |Item|Description|  
    |----------|-----------------|  
    |Name (required)|The name of the topic model.|  
    |Source Entity (required)|The entity that articles are suggested for. Limited to entities enabled for Knowledge Management (isKnowledgeManagementEnabled attribute). Go to **Settings** > **Customizations** > **Customize the System**. Select an entity, and then under **Communication and Collaboration**, enable **Knowledge Management**.|  
    |Maximum Number of Key Phrases (required)|The maximum number of keywords or key phrases to be determined using text analytics.|  
    |Description|A description of the search configuration.|  
  
4.  Click **Save**.  
  
5.  Scroll down to **Keyword or Key Phrase Determination Fields**, and then click **New** .  
  
6.  These settings determine the keywords or key phrases determined from the source record by using text analytics to match with knowledge base records using text search. This helps to achieve more relevant results with the knowledge base.  
  
     Text Analytics Entity Mapping  
  
    |Item|Description|  
    |----------|-----------------|  
    |Entity|Choose an entity to use in creating a text search rule to find matching records in [!INCLUDE[pn_dyn_365](../includes/pn-dyn-365.md)]. The following entities are available: Activity, Case, Case Resolution, Email, Fax, Note.<br /><br /> -   Source entity like Case and Note.<br />-   Activity and out-of-box activity entities like Email, Fax, Letter, Phone Call, and Appointment.<br />-   Any custom entity with a 1:N or N:1 relationship to the source entity.|  
    |Field|Choose the  field to use in creating a text search rule to find matching knowledge base records. The following types of fields are available: Option Set, Single Line of Text, Multiple Lines of Text.|  
  
7.  Add more fields to create a comprehensive search of related articles.  
  
8.  Click **Activate**.  
  
<a name="BKMK_ModifyCase"></a>   
## Modify the Case form to include knowledge base suggestions  
 These steps apply to any knowledge enabled entity.  
  
1.  Go to **Service** > **Cases**, and then select the case to include knowledge base suggestions.  
  
2.  Click the **More Commands** button .  
  
3.  Click **Form Editor**.  
  
4.  Click the **Conversation Tabs** box, and then click **Change Properties**.  
  
5.  Click the **Knowledge Base Search** tab, check the **Turn on automatic suggestions** check box, and then select **Text analytics** for the **Give knowledge base (KB) suggestions** drop-down list.  
  
     If **Text analytics** is not available in the drop-down list, check to make sure the knowledge search model is activated.  
  
6.  Click **Save** > **Publish** to publish the modified form.  
  
<a name="BKMK_ViewAutomatic"></a>   
## View automatic suggestions in a case  
  
1.  Click **Service** > **Cases** and open a case record.  
  
2.  On the Activity wall, click **KB Records**.  
  
 You can now see a list of KB articles related to this case.  
  
 Click an article to review the text inline.  
  
<a name="BKMK_ISHSearch"></a>   
## Search for related knowledge articles and cases in the interactive service hub  
 The interactive service hub  unifies vital information in one place, and lets you focus on things that require your attention, like finding articles and cases related to your active case.  
  
1.  Open the interactive service hub. See [Open the interactive service hub](https://docs.microsoft.com/dynamics365/customer-engagement/customer-service/user-guide-customer-service).  
  
2.  Click **Service** > **Cases** and open a case.  
  
3.  Click the **Knowledge Base Search** button to find related knowledge articles.  
  
4.  Click the **Similar Cases** button to find related cases.  
 
### See also  
 [What are Preview features and how do I enable them?](https://docs.microsoft.com/dynamics365/customer-engagement/admin/what-are-preview-features-how-do-i-enable-them)   
 [User's guide for the new interactive service hub](https://docs.microsoft.com/dynamics365/customer-engagement/customer-service/user-guide-customer-service)   
