When you accept the terms and conditions for event management, the webinar-integration feature is activated. The webinar integration feature leverages a partner webinar provider to conduct an event or a session as a webinar. To use any webinar provider’s service, you must have an account with them. The only partner webinar provider service provided out of the box at this time is ON24. When using the webinar-integration feature, data essential to providing and running the webinar would be processed and stored on [!INCLUDE[pn-azure-service-fabric](../includes/pn-azure-service-fabric.md)], and then sent to ON24. Such data would include the webinar participants’ registration data such as their names, emails, and company names. In addition, ON24 would send webinar metrics such as webinar viewing duration to [!INCLUDE[pn-microsoftcrm](../includes/pn-microsoftcrm.md)] via [!INCLUDE[pn-azure-service-fabric](../includes/pn-azure-service-fabric.md)].

You don't need to activate the webinar feature to use the rest of the event-management solution. An administrator can turn off the webinar integration feature by removing the credentials in the webinar configuration.

[!INCLUDE[pn-windows-azure](../includes/pn-windows-azure.md)] components and services used by the webinar-integration feature are:

- [!INCLUDE[pn_azure_key_vault](../includes/pn_azure_key_vault.md)] ([!INCLUDE[proc-more-information](../includes/proc-more-information.md)] [What is Azure Key Vault?](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-whatis))
  - Provides encryption key for encrypting/decrypting customer’s ON24 account credentials
- [!INCLUDE[pn-azure-service-fabric](../includes/pn-azure-service-fabric.md)] ([!INCLUDE[proc-more-information](../includes/proc-more-information.md)] [Overview of Azure Service Fabric](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-overview))
  - Processes and sends registration data and webinar account credentials to ON24
  - Retrieves webinar metrics from On24 to [!INCLUDE[pn-microsoftcrm](../includes/pn-microsoftcrm.md)]
  -Stores customer’s ON24 account credentials (custom encrypted)