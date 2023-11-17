By installing and enabling the [!INCLUDE[pn_gamification](pn-gamification.md)] solution, the enabling user’s account identifiers (such as first name, last name, and email address) will be stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] to allow for authorization with the [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] service, which is hosted in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)]. This applies to all users that are enabled in the [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] service by their administrator. The [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] solution sends Key Performance Indicators (KPI) data, configured by an administrator, to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] service, and that data is stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] structured storage as well as blob storage.  Each user’s Avatar, Custom Awards, and Company Logo are stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)], but the information is not returned to [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)].  
  
Note that administrators and authorized users can leverage [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)] data, such as phone calls, opportunities, and booked revenue to configure KPIs for use in games. The [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] service does not initiate any calls to [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)] and only responds to data, such as games where the KPIs are being used, that flows back to [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)].  
  
An administrator can also enable the [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] TV stream to be made public. Game managers who set up [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] TV streams and enable public streaming will allow for the TV stream to be viewed by anyone on the Internet who has the stream link.  
  
An administrator can subsequently remove the [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] functionality by uninstalling this solution from the [!INCLUDE[pn_microsoftcrm](pn-microsoftcrm.md)] organization.  
  
[!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] are detailed in the following sections.  
  
[!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]  
  
[Cloud Services](https://azure.microsoft.com/services/cloud-services/)  
  
 **Designer Service (Web Role)**  
  
This provides multiple Web Services for communication between a [!INCLUDE[pn_crm_shortest](pn-crm-shortest.md)] organization and the multi-tenanted [!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components. For example, gamification details stored to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] SQL Storage.  Game calculations use [!INCLUDE[pn_azure_service_bus](pn-azure-service-bus.md)] queue and returned to be scored and shown in the service.  Customer and user uploaded images are stored in [!INCLUDE[pn_azure_blob_storage](pn-azure-blob-storage.md)]. All requests are authenticated against [!INCLUDE[pn_azure_active_directory](pn-azure-active-directory.md)].  
  
[Azure Key Vault](https://azure.microsoft.com/services/key-vault/)  
  
All services store configuration data in [!INCLUDE[pn_azure_key_vault](pn-azure-key-vault.md)].  
  
[Azure SQL Database](https://azure.microsoft.com/services/sql-database/)  
  
[!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] uses SQL [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] to store:  
  
- KPI data  
  
- Game calculations  
  
- Organization (tenant) data  
  
[Azure Blob Storage](https://azure.microsoft.com/services/storage/)  
  
Avatars, company logos, and other customer uploaded images are stored in [!INCLUDE[pn_azure_blob_storage](pn-azure-blob-storage.md)].  
  
[Azure Content Delivery Network (CDN)](https://azure.microsoft.com/services/cdn/)  
  
[!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] uses [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Content Delivery Network to serve static content to the runtime such as images (including uploaded images such as customer logos), [!INCLUDE[pn_JavaScript](pn-javascript.md)], and CSS.  
  
[Microsoft Entra ID](https://azure.microsoft.com/services/active-directory/)  
  
[!INCLUDE[pn_gamification_shortest](pn-gamification-shortest.md)] uses [!INCLUDE[pn_azure_active_directory](pn-azure-active-directory.md)] to authenticate users and determine eligibility to use the platform.