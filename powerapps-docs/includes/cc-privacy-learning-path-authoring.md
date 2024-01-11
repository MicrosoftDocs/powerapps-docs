By enabling Learning Path Authoring for a [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] organization, Learning Path content (published or draft) created by users (with the right security privileges) will be stored in [!INCLUDE[pn_Azure_SQL_Database_long](pn-azure-sql-database-long.md)]. In addition, enabling the feature allows [!INCLUDE[pn_azure_cloud_services](pn-azure-cloud-services.md)] to capture the following data associated with a [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] organization:  
  
-   List of organizations in the Tenant  
  
-   End users’ [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] client and applicable browser / OS configuration  
  
-   Usage data of end users – such as time spent on Learning Paths or clicks recorded  
  
-   Aggregated end-user data – Location, security role, user language  
  
-   Aggregated end-user data – Location, security role, user language  
  
-   Verbatim feedback from end users  
  
 An administrator can enable (and can subsequently disable) Learning Path Authoring through a setting on the **General** tab of the **System Settings** dialog box.  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with Learning Path Authoring functionality are detailed in the following sections.  
  
 [!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]  
  
 [Cloud Services](https://azure.microsoft.com/services/cloud-services/)  
  
 **Web Service**  
  
 Web Service serves the controls that are rendered on the client by Learning Path Runtime. Web Service also supports Designer API, which is used by Learning Path Authoring. The controls are stored by the service on [!INCLUDE[pn_Azure_SQL_Database_long](pn-azure-sql-database-long.md)].  
  
 **Compiler (Worker Role)**  
  
 Compiler role manages the publish of a control to a publishing group. Compiler uses the queue to store messages about the Publish job. The results are stored in [!INCLUDE[pn_Azure_SQL_Database_long](pn-azure-sql-database-long.md)].  
  
 [Azure SQL Database](https://azure.microsoft.com/services/sql-database/)  
  
 Learning Path uses [!INCLUDE[pn_Azure_SQL_Database_long](pn-azure-sql-database-long.md)] to store:  
  
-   Controls that are created by using Learning Path.  
  
-   Configuration-related Learning Path Authoring.  
  
 [Microsoft Entra ID](https://azure.microsoft.com/services/active-directory/)  
  
 Learning Path uses [!INCLUDE[pn_azure_active_directory](pn-azure-active-directory.md)] to authenticate Web Service.  
  
 [Azure Traffic Manager](https://azure.microsoft.com/services/traffic-manager/)  
  
 Learning Path uses [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Traffic Manager to load balance the Web Service for availability and performance.  
  
 [Azure Storage Queue](https://azure.microsoft.com/services/storage/)  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage queue is used to coordinate communication between the Web Service and Compiler roles.  
  
 [Azure Blob Storage](https://azure.microsoft.com/services/storage/)  
  
 Learning Path uses [!INCLUDE[pn_azure_blob_storage](pn-azure-blob-storage.md)] to store the static content (client-side [!INCLUDE[pn_JavaScript](pn-javascript.md)], images, CSS content).  
  
 [Azure Content Delivery Network (CDN)](https://azure.microsoft.com/services/cdn/)  
  
 CDN is used to cache the client side static content ([!INCLUDE[pn_JavaScript](pn-javascript.md)], images, and CSS files), to serve them from global CDN network.