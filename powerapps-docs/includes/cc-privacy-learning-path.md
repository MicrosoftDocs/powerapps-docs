By enabling the Learning Path feature, static html, you enable images and scripts to be stored on [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Content Delivery Network (CDN). In addition, all dynamic content that is displayed will be stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Redis Cache, which is used to pre-cache from the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] SQL database.  
  
 An administrator can enable and disable use of the Learning Path feature within a [!INCLUDE[pn_crm_online_shortest](pn-crm-online-shortest.md)] instance by using the Enable Guided Help setting in the [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)] organization.  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with Learning Path functionality are detailed in the following sections.  
  
> [!NOTE]
>  For more information about additional Azure service offerings, see the [Microsoft Azure Trust Center](https://azure.microsoft.com/support/trust-center/).  
  
 [Cloud Services](https://azure.microsoft.com/services/cloud-services/)  
  
 **Learning Path runtime (Web Role)**  
  
 This is the web application that serves the content to users.  
  
 **Learning Path service (Worker Role)**  
  
 Worker role is responsible for processing the data from [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] SQL Database and caching them into [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Redis Cache.  
  
 [Azure SQL Database](https://azure.microsoft.com/services/sql-database/)  
  
 Learning Path uses SQL Database to store:  
  
-   Content  
  
-   Content metadata  
  
-   System metadata  
  
 [Azure Blob Storage](https://azure.microsoft.com/services/storage/)  
  
 The HTML, images, [!INCLUDE[pn_JavaScript](pn-javascript.md)], and CSS are all stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob storage.  
  
 [Azure Content Delivery Network  (CDN)](https://azure.microsoft.com/services/cdn/)  
  
 Learning Path uses [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Content Delivery Network to serve static content to the survey runtime, such as HTML, images, [!INCLUDE[pn_JavaScript](pn-javascript.md)], and CSS.  
  
 [Microsoft Entra ID](https://azure.microsoft.com/services/active-directory/)  
  
 Learning Path uses [!INCLUDE[pn_azure_active_directory](pn-azure-active-directory.md)] Service to authenticate web services specifically for the designer. Currently the designer is not exposed to customers and partners. And hence the authentication is within only the [!INCLUDE[cc_Microsoft](cc-microsoft.md)] domain.  
  
 [Azure Redis Cache](https://azure.microsoft.com/services/cache/)  
  
 Learning path uses [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Redis Cache to cache dynamic content that we serve to users.  
  
 [Azure Traffic Manager](https://azure.microsoft.com/services/traffic-manager/)  
  
 Learning Path uses Traffic Manager to improve the availability of important applications by monitoring your [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] or external sites and services and automatically directing users to a new location anytime there’s a failure.  
  
 [Azure Resource Manager](https://azure.microsoft.com/features/resource-manager/)  
  
 Learning Path uses [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Resource Manager to deploy CDN, Redis Cache, SQL Database, and cloud services as resource groups so that they are in a consistent state and can be deployed repeatedly.