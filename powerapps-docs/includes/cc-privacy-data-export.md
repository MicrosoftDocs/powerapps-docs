By using the Data Export Service, when you activate a data export profile from within [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)], the data of the entities added to the profile is sent to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)]. The initial synchronization includes all the data associated with the entities added to the export profile, but thereafter synchronization includes only new changes, which are continuously sent to the Data Export Service. Data sent to the Data Export Service is stored temporarily in [!INCLUDE[pn_azure_service_bus](pn_azure_service_bus.md)] and [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage, processed in [!INCLUDE[pn_azure_service_fabric](pn_azure_service_fabric.md)], and finally synchronized (inserted, updated, or deleted) to the destination database specified in your [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] subscription. After the data has been synchronized, it is deleted from [!INCLUDE[pn_azure_service_bus](pn_azure_service_bus.md)] and [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage. If there is a failure during data synchronization, minimal data corresponding to entity type, record ID, and sync timestamp is stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage to allow for downloading a list of records that were not updated.  
  
 An administrator can deactivate the data export profile at any time to stop data synchronization. In addition, an administrator can delete the export profile to remove any failed record logs and can uninstall the Data Export Service solution to stop using the Data Export Service.  
  
 Data synchronization happens continuously between [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)] and the Data Export Service in a secure manner. Data is encrypted as it is continuously exchanged between [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)] and the Data Export Service.  
  
 Azure components and services that are involved with the Data Export Service are detailed in the following sections.  
  
 [!INCLUDE[cc_privacy_note_azure_trust_center](cc_privacy_note_azure_trust_center.md)]  
  
 [Azure Service Fabric](https://azure.microsoft.com/services/service-fabric/)  
  
 This provides the API and compute [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] VMs to process record synchronize notifications received from [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)] and then process them to insert, update, or delete record data in the destination database. Micro-services that are deployed on virtual machines managed by the [!INCLUDE[pn_azure_service_fabric](pn_azure_service_fabric.md)] runtime handle all the compute services related to data synchronization.  
  
 [Azure Service Bus](https://azure.microsoft.com/services/service-bus/)  
  
 This provides the message bus into which [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)] inserts the synchronization notification messages that are processed by compute nodes in [!INCLUDE[pn_azure_service_fabric](pn_azure_service_fabric.md)]. Each message stores information, such as the org id and record, for which for which to sync data. Data in the Azure Service Bus is not encrypted at rest, but is only accessible by the Data Export Service.  
  
 [Azure Blob Storage](https://azure.microsoft.com/services/storage/)  
  
 Data is temporarily stored in [!INCLUDE[pn_azure_blob_storage](pn_azure_blob_storage.md)] in case the record sync notification’s data is too large to store in a message or a transient failure is encountered to process the synchronization notification. These blobs are encrypted by leveraging the latest feature in the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Storage SDK, which provides symmetric and asymmetric encryption support and integration with [!INCLUDE[pn_azure_key_vault](pn-azure-key-vault.md)].  
  
 [Azure SQL](https://azure.microsoft.com/services/sql-database/)  
  
 The [!INCLUDE[pn_Azure_SQL_Database_long](pn-azure-sql-database-long.md)] stores data export profile configuration and data synchronization metrics.