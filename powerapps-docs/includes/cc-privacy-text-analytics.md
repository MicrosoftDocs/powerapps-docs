By enabling the Text Analytics feature, you enable dependent features within [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] that leverage the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Cognitive Services Text Analytics API to offer advanced insights. These dependent features are:  
  
-   Knowledge suggestions  
  
-   Case topic analysis  
  
-   Similar cases suggestions  
  
 An administrator can enable the Text Analytics feature under **Settings** > **Administration** > **System Settings** > **Preview** tab in the [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)] organization.  
  
 By enabling the Text Analytics feature, when you set up text analytics–based knowledge suggestions within [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)], the case and its related entities’ data is sent to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API to extract keywords/phrases. No data is stored with the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API. Only configured fields in the Knowledge Article configuration are sent to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API to extract the terms. The administrator or customizer does have the option to deactivate the Knowledge Article Configuration to stop making API calls to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API. Also, the customizer can stop using Text Analytics–based suggestions by switching back to Field-based suggestions in the Case Entity Form configuration.  
  
 By enabling the Text Analytics feature, when you set up case topic analysis within [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)], the case and its related entities data is sent to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API for topic determination. No data is stored with the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API. Only configured fields in the Topic Model Configuration are sent to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API to extract the topics. The administrator or customizer does have the option to deactivate the Topic Model to stop making [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API calls.  
  
 By enabling the Text Analytics feature, when you set up similar cases suggestions within [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)], if the Advanced Text Analytics option is enabled in the Similarity Rule, then the case and its related entities’ data is sent to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API to extract keywords and phrases. Only text fields configured in the Similarity Rule are sent to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API. No data is stored with the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API. The administrator or customizer does have the option to deactivate the Similarity rule to stop making [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API calls.  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with Text Analytics–based features are detailed in the following sections.  
  
 [!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]  
  
 [Azure API App](https://azure.microsoft.com/services/app-service/api/)  
  
 The [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] API app triggers the Web jobs that read the data from the [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] organization and send data to the Text Analytics API to do topic analysis. The [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] API App uses a Web job to do the actual data processing in the background and write the data output to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob Storage. The data is stored temporarily in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob Storage. Finally, data is deleted from [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage once topic determination has been done.  
  
 [Azure Scheduler](https://azure.microsoft.com/services/storage/)  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Scheduler is used to trigger a Web job on a scheduled basis to perform topic analysis. Only the topic model build schedule is shared with the scheduler.  
  
 [Azure Table](https://azure.microsoft.com/services/storage/)  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Table is used for communicating the model version and organization context between the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] API app and the Web job.  
  
 [Azure Blob Storage](https://azure.microsoft.com/services/storage/)  
  
 Web jobs temporarily store data in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob Storage and delete it once the Logic App pipeline has finished execution.  
  
 [Azure Text Analytics API](https://www.microsoft.com/cognitive-services/text-analytics-api)  
  
 The [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Text Analytics API is sent data based on fields that are configured in active Knowledge Search fields or the Topic Model configuration or the Similarity Rule configuration. For example, case entity fields, such as title and description, plus the description field in related notes and activities, are configured in the Knowledge Search Field configuration.  
  
 [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] Dataverse search  
  
 You can use Dataverse search, if it has been enabled by an administrator, to find similar records for cases. The text match fields and exact match fields used in the Similarity rule are used to invoke the Dataverse search API. Refer to the technical content for [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] Dataverse search for data-handling details.