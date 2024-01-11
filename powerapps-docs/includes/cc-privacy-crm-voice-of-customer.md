By enabling Voice of the Customer for Dynamics 365, when you publish a survey from within Dynamics 365, the survey definition will be sent to Azure and stored in Azure Storage. When a respondent submits a survey (by opening the survey invitation link sent to them via email), the survey responses are stored temporarily in the Azure Service Bus and then are retrieved and stored in Dynamics 365. After the responses have been stored in Dynamics 365, they are deleted from Azure.  
  
 Note that it is possible to include Dynamics 365 data such as customer name, product name, case number, etc. in a survey (within survey elements such as questions, answers, etc.) when rendering a survey for a respondent. When a survey invitation link is generated, this Dynamics 365 data would be sent out of Dynamics 365 and stored in Azure SQL Database in exchange for an identifier that is used within the survey invitation link. This identifier is used to show the Dynamics 365 data within the survey after the survey is opened using the survey invitation link. The identifiers within the survey link that is sent over email to a respondent is stored in the respondents’ email system.  
  
 An administrator can enable the Voice of the Customer for Dynamics 365 feature by installing it as a solution in the Dynamics 365 organization. In addition, an administrator can subsequently disable the feature by uninstalling this solution from the Dynamics 365 organization.  
  
 Azure components and services that are involved with Voice of the Customer for Dynamics 365 functionality are detailed in the following sections.  
  
 Note: For more information about additional Azure service offerings, see the Microsoft Azure Trust Center ([https://azure.microsoft.com/support/trust-center/](https://azure.microsoft.com/support/trust-center/)).  
  
 **Cloud Services** ([https://azure.microsoft.com/services/cloud-services/](https://azure.microsoft.com/services/cloud-services/))  
  
 **Designer Service (Web Role)**  
  
 This provides multiple Web Services for communication between a Dynamics 365 organization and the multi-tenanted Voice of the Customer for Dynamics 365 Azure components.  For example, surveys are published and stored to Azure Blob Storage.  Survey responses are retrieved from an Azure Service Bus queue and returned to be persisted in the Dynamics 365 organization.  All requests are authenticated against Microsoft Entra ID.  
  
 **Survey Runtime (Web Role)**  
  
 This is the web application that serves the surveys to the respondents.  Submitted survey responses are stored temporarily on an Azure Service Bus queue before being processed retrieved by a Dynamics 365 asynchronous service.  
  
 **Response Processor (Worker Role)**  
  
 This worker role is responsible for processing the raw completed surveys into valid survey responses that can be created in Dynamics 365.  
  
 **Push Processor (Worker Role)**  
 This worker role is responsible for processing the valid survey responses and updating as Dynamics 365 entity records. 
 
 **Azure Key Vault** ([https://azure.microsoft.com/services/key-vault/](https://azure.microsoft.com/services/key-vault/))  
  
 All cloud services store configuration data in Azure Key Vault.  Organization, tenant data is stored in SQL Azure.  
  
 **Azure SQL Database** ([https://azure.microsoft.com/services/sql-database/](https://azure.microsoft.com/services/sql-database/))  
  
 Voice of the Customer for Dynamics 365 uses SQL Azure to store:  
  
-   Piped data  
  
-   Survey metadata  
  
-   Organization (tenant) data  
  
 **Azure Blob Storage** ([https://azure.microsoft.com/services/storage/](https://azure.microsoft.com/services/storage/))  
  
 Survey definitions and partially completed (saved) responses are stored to Azure Blob storage.  
  
 **Azure Content Delivery Network (CDN)** ([https://azure.microsoft.com/services/cdn/](https://azure.microsoft.com/services/cdn/))  
  
 The Voice of the Customer for Dynamics 365 solution uses Azure Content Delivery Network to serve static content to the survey runtime such as images (including uploaded images such as customer logos), JavaScript and CSS.  
  
 **Microsoft Entra ID** ([https://azure.microsoft.com/services/active-directory/](https://azure.microsoft.com/services/active-directory/))  
  
 The Voice of the Customer for Dynamics 365 solution uses Microsoft Entra Service to authenticate web services.  
  
 **Azure Service Bus** ([https://azure.microsoft.com/services/service-bus/](https://azure.microsoft.com/services/service-bus/))  
  
 Messages created when a survey is displayed / submitted are stored temporarily to an organization’s (tenant’s) Azure Service Bus Queue until the Azure worker role pushes the survey responses into an organization’s Dynamics 365 instance and persists them as Dynamics 365 entity records.