By enabling Dataverse search, data in participating entities and attributes in your [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)] instance will begin syncing to and be stored in an [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Search index.  
  
 Dataverse search is not enabled by default. The system administrator must enable the functionality within a [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)] instance. After Dataverse search is enabled, system administrators and customizers have full control over the data that will be synchronized to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Search index.  
  
 System customizers can use the **Configure Dataverse search** dialog box in **Customization Tools** to enable specific entities for search and then configure Quick Find views on enabled entities to select the searchable attributes. Data changes are synchronized continuously between [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)] and [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Search through a secure connection.  Configuration data is encrypted and the required secrets are stored in [!INCLUDE[pn_azure_key_vault](pn-azure-key-vault.md)].  
  
 Azure components and services that are involved with Dataverse search functionality are detailed in the following sections.  
  
 [!INCLUDE[cc_privacy_note_azure_trust_center](cc_privacy_note_azure_trust_center.md)]  
  
 [Azure Search Services](https://azure.microsoft.com/services/search/)  
  
 An [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Search index is used to provide high-quality search results with quick response times.  [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Search adds powerful and sophisticated next-generation search capabilities to [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)].  This is a dedicated search service external to [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)] provided by [!INCLUDE[pn_Windows_Azure](pn-windows-azure.md)]. All new [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Search indexes are encrypted at rest.  If you opted in before January 24, 2018, you'll need to reindex your data by opting out of Dataverse search, waiting an hour, and opting back in.  
  
 [Azure SQL Database](https://azure.microsoft.com/services/sql-database/)  
  
 Dataverse search uses the [!INCLUDE[pn_Azure_SQL_Database_long](pn-azure-sql-database-long.md)] to store:  
  
-   Configuration data related to the organization and the corresponding index  
  
-   Metadata relating to the search service and indexes  
  
-   Pointers to system metadata and data when synchronizing changes  
  
-   Authorization data to enable enhanced row- level security  
  
[Azure Event Hubs](https://azure.microsoft.com/services/event-hubs/)  
  
The [!INCLUDE[pn_azure_event_hubs](pn-azure-event-hubs.md)] component is used for message exchange between [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)] and [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] and to maintain work items that are managed by the synchronization process. Each message stores information, such as the organization ID and entity name, used to sync the data.  
  
[Azure Service Fabric Cluster](https://azure.microsoft.com/services/service-fabric/)  
  
The processing and indexing of data is handled in micro-services deployed on virtual machines managed through the Service Fabric runtime. The search APIs and the data synchronization process are also hosted on the Service Fabric cluster.  
  
Service Fabric was born from years of experience at Microsoft delivering mission-critical cloud services and is now production-proven for over five years. It’s the foundational technology on which we run our [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] core infrastructure, powering services including [!INCLUDE[pn_skype_for_business](pn-skype-for-business.md)], [!INCLUDE[pn_intune](pn-intune.md)], [!INCLUDE[pn_azure_event_hubs](pn-azure-event-hubs.md)], [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Data Factory, [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] DocumentDB, [!INCLUDE[pn_Azure_SQL_Database_long](pn-azure-sql-database-long.md)], and [!INCLUDE[pn_cortana](pn-cortana.md)]—which can scale to process more than 500 million evaluations per second.  
  
[Azure Virtual Machine Scale Sets](https://azure.microsoft.com/services/virtual-machine-scale-sets/)  
  
[!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Virtual Machine Scale Sets are elastic and designed to support hyper scale-out workloads. The [!INCLUDE[pn_azure_service_fabric](pn_azure_service_fabric.md)] cluster runs on virtual machine scale sets. The micro-services for processing and indexing data are hosted on the scale sets and managed by the Service Fabric runtime.  
  
[Azure Key Vault](https://azure.microsoft.com/services/key-vault/)  
  
[!INCLUDE[pn_azure_key_vault](pn-azure-key-vault.md)] is used for secure management of certificates, keys, and other secrets used in the search process.  
  
[Azure Storage (Blob Storage)](https://azure.microsoft.com/services/storage/blobs/?b=16.38)  
  
Changes to customer data are stored for up to 2 days in [!INCLUDE[pn_azure_blob_storage](pn_azure_blob_storage.md)].  These blobs are encrypted by leveraging the latest feature in the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage SDK, which provides symmetric and asymmetric encryption support and integration with [!INCLUDE[pn_azure_key_vault](pn-azure-key-vault.md)]. With the [!INCLUDE[pn_crm_8_2_0_online_subsequent](pn-crm-8-2-0-online-subsequent.md)], the documents found in Notes and Attachments on email messages and appointments are also synced to the blob storage.  
  
[Azure Active Directory Service](https://azure.microsoft.com/services/active-directory/)  
  
[!INCLUDE[pn_azure_active_directory](pn-azure-active-directory.md)] is used to authenticate between the [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)] and [!INCLUDE[pn_Windows_Azure](pn-windows-azure.md)] services.  
  
[Azure Load Balancer](https://azure.microsoft.com/services/load-balancer/)  
  
The [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Load Balancer is used to distribute incoming traffic among healthy service instances in cloud services or virtual machines defined in a load balancer set. Dataverse search uses it to load balance the end points in a deployment.  
  
[Azure Virtual Networks](https://azure.microsoft.com/documentation/articles/virtual-networks-overview/)  
  
The Virtual Machines on the Service Fabric cluster running in one or more subnets are connected by [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Virtual Network. The security policies, DNS settings, route tables, and IP addresses are fully controlled within this virtual network. Network Security Groups are leveraged to apply security rules on this virtual network. These rules allow or deny network traffic to the VMs in the virtual network.