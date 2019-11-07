By enabling the Product Recommendations feature, when you build a recommendation model from within [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)], the historical transaction data based on configured Basket Data entities and their filter will be sent to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] and processed in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] and stored temporarily in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage and finally sent to Azure Recommendations API to build the machine learning model. After the model has been built with Azure Recommendations API, data is deleted from [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage. Note that only IDs (Account ID, Product ID, Transaction ID) are sent to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] to build the recommendation model.

An administrator can enable the Product Recommendations feature under **Settings** &gt; **Administration** &gt; **System Settings** &gt; **Preview** tab in the [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)] organization. Data is sent to Azure Recommendations API only when a recommendation model is built. The system administrator does have the option to delete the existing model to delete data shared with the Azure Recommendations API. In addition, the system administrator can delete the connection to the Azure Recommendations API to stop building any recommendation models in the future.

[!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with Product Recommendations are detailed in the following sections.

[!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]

[Azure Logic Apps](https://azure.microsoft.com/services/app-service/logic/)

This provides the orchestrated data pipeline to synchronize product catalog and transaction data with the Recommendations API to build the recommendation model version. This pipeline executes as a multi-tenanted service with multiple API apps for communication between a Dynamics 365 organization and the Recommendations API. Logic apps are triggered from [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] with minimal context, such as Model Version ID and the [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] organization URL. 

[Azure API Apps](https://azure.microsoft.com/services/app-service/api/)

These are the web applications that trigger the Web jobs that read the data from the [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] organization and send data to the Recommendations API to build the recommendation model. There are 3 API apps and corresponding Web jobs - one for reading product data, one for reading transaction data, and one for building a recommendation model. API apps use a Web job to do the actual data processing in the background and write the data output to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob Storage. The data is stored temporarily in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob Storage. Finally, data is deleted from [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage once the model has been built.

[Azure Table](https://azure.microsoft.com/services/storage/tables/)

[!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Table is used for communicating the model version and organization context between the API app and a Web job.

[Azure Blob Storage](https://azure.microsoft.com/services/storage/) 

Data is stored temporarily in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob Storage by Web jobs and deleted once the Logic App pipeline has finished execution.

[Azure Recommendations API](https://www.microsoft.com/cognitive-services/recommendations-api) The Azure Recommendations API is sent with minimal data Product IDs, Transaction IDs, and Account IDs to build the recommendation model. Data is stored with the Recommendations API service until a corresponding model version exists.
