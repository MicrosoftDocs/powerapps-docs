---
title: "Data export service (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Capabilities, prerequisites, API, and programming of the Data Export Service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "sabinn-msft" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Data export service

Data Export is an add-on service made available as a Common Data Service for Apps solution that adds the ability to replicate Common Data Service for Apps data to a Microsoft Azure SQL Database store in a customer-owned Microsoft Azure subscription. The supported target destinations are Microsoft Azure SQL Database and Microsoft Azure SQL Server on Microsoft Azure virtual machines. Data Export intelligently synchronizes the entire Dynamics 365 schema and data initially and thereafter synchronizes on a continuous basis as changes occur (delta changes) in the Dynamics 365 (online) system.  
  
 The Data Export service provides an interface for managing configuration and ongoing administration of this service from within CDS for Apps.  For more information, see [Data Export](https://technet.microsoft.com/library/a70feedc-12b9-4a2d-baf0-f489cdcc177d). This topic explains the corresponding programmatic interface and issues for this service.  
  
## Prerequisites for using the Data Export Service  
 Because this service requires access to an external Microsoft Azure SQL Database from CDS for Apps,   a number of prerequisites must be satisfied before you can successfully access this service. The following perquisites are more fully explained from an administrator's perspective in the section [Prerequisites for using Data Export Service](https://technet.microsoft.com/library/mt744592.aspx).  
  
 Your CDS for Apps service must be configured so that:  
  
- The entities that will be exported are enabled with change tracking. For more information, see [Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md).  
  
- Code is run in the context of a user with the System Administrator security role.  
  
> [!NOTE]
>  Note that programmatic access to this service does *not* require the installation of the associated Data Export managed solution.  
  
 The target Azure SQL Database must be configured so that:  
  
- The subscription must support the volume of data being replicated from your CDS for Apps instance.  
  
- Firewall settings must allow access from the IP address of your  Data Export service. For more information, see [Configure an Azure SQL Database server-level firewall rule using the Azure Portal](https://azure.microsoft.com/en-us/documentation/articles/sql-database-configure-firewall-settings/).  
  
- It is recommended that option “Allow access to azure services” be enabled.  
  
- The database user, specified in the  data export connection string, must have the proper create and alter permissions on the target database.  At minimum these include: `CRTB`, `CRTY`, `CRVW`,     `CRPR`, and `ALUS`. For more information, see [Permissions (Database Engine)](https://msdn.microsoft.com/en-us/library/ms191291.aspx).  
  
- At least one user have extensive permissions on the schema. The following script creates such a new user.  
  
```sql  
  
USE MASTER;  
CREATE LOGIN NewUser WITH PASSWORD='newpassword';  
  
USE DESTINATIONDATABASE;  
CREATE USER NewUser FOR LOGIN NewUser  
GRANT CREATE TABLE, CREATE TYPE, CREATE VIEW, CREATE PROCEDURE, ALTER ANY USER to NewUser  
GRANT ALTER, REFERENCES, INSERT, DELETE, UPDATE, SELECT, EXECUTE ON SCHEMA::dbo TO NewUser  
  
```  
  
For online solutions and services, Azure provides a [Key Vault](https://azure.microsoft.com/en-us/services/key-vault/) service to safeguard cryptographic keys, passwords, and other secrets.  To use Azure Key Vault, this customer-owned service must be configured so that permission is granted to "Dynamics 365 Data Export Service", which is used to safely store the SQL Azure connection string. To perform this configuration with a PowerShell script, see [How to set up Azure Key Vault](https://technet.microsoft.com/library/mt744592.aspx). Alternately, this service can be managed through its REST API; see [Key Vault management](https://msdn.microsoft.com/library/azure/mt620024.aspx).  
  
It is also advised that you add the domain https://discovery.crmreplication.azure.net/ to the trusted sites list in your browser and to enable pop-ups for this site.  
  
## Programming for the Data Export Service  
 The Data Export Service exposes a REST-based API that is divided into two groups: a set of `Metadata` operations for exploring CDS for Apps organizational structure, relationships, and connection information; and a set of `Profiles` operations    for configuring and managing each data replication.  This API is fully defined and documented at the following [Swagger](http://swagger.io/) URLs:  
  
|Swagger endpoint|Description|  
|----------------------|-----------------|  
|[https://discovery.crmreplication.azure.net/swagger/docs/2016-01-01](https://discovery.crmreplication.azure.net/swagger/docs/2016-01-01)|JSON definition of the Data Export Service API for use by developer tools and dynamic processes|  
|[https://discovery.crmreplication.azure.net/swagger/ui/index#](https://discovery.crmreplication.azure.net/swagger/ui/index)|The user-friendly version of this API for developer reference|  
  
<a name="bk_ApiQuickReference"></a>   
### API Quick Reference  
 For the reader's convenience, these interfaces are summarized in the following tables.  
  
 **Metadata operations** (`https://discovery.crmreplication.azure.net/crm/exporter/metadata/`)  
  
|Resource|Methods|Description|  
|--------------|-------------|-----------------|  
|organizations|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Metadata/Metadata_GetOrganizations)|Get organizational details for all organizations that the current user belongs to|  
|discover|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Metadata/Metadata_GetOrgDetails)|Get organizational details for the specified organization|  
|connector|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Metadata/Metadata_GetConnectorDetails)|Get connector details for the specified organization|  
|entities|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Metadata/Metadata_GetEntities)|Get all exportable public entities for the specified organization|  
|relationships|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Metadata/Metadata_GetRelationships)|Get all exportable relationships for the specified organization|  
|hasorgacceptedprivacyterms|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Metadata/Metadata_HasOrgAcceptedPrivacyTerms)|Check if the associated organization has accepted the privacy terms|  
|acceptprivacyterms|[POST](https://discovery.crmreplication.azure.net/swagger/ui/index#/Metadata/Metadata_AcceptOrgPrivacyTerms)|Accept the specified org for data access|  
  
 **Profiles operations** (`[Organization-URI]/crm/exporter/`)  
  
|Resource|Methods|Description|  
|--------------|-------------|-----------------|  
|profiles|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_GetProfilesByOrganizationId), [POST](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_CreateProfile)|Get all profiles for specified organization, create a new export profile|  
|profiles/{id}|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_GetProfileById), [PUT](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_UpdateProfile), [DELETE](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_DeleteProfileById)|Get, update or delete a specific profile|  
|profiles/{id}/activate|[POST](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_Activate)|Activate a profile, which starts replication of both the associated metadata and data|  
|profiles/{id}/activatemetadata|[POST](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_ActivateMetadata)|Activate profile for metadata replication only|  
|profiles/{id}/activatedata|[POST](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_ActivateData)|Activate profile for data replication only|  
|profiles/{id}/deactivate|[POST](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_Deactivate)|Deactivate a profile|  
|profiles/{id}/test|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_GetTestResultById)|Perform test operations on an existing profile|  
|profiles/validate|[POST](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_ValidateBeforeProfileCreation)|Perform test operations on a profile description before creating it|  
|profiles/{id}/failures|[GET](https://discovery.crmreplication.azure.net/swagger/ui/index#/Profiles/Profiles_GetProfileFailuresInfoById)|Get the connection string to a blob that contains failure details for a given profile|  
  
### Gain Access  
Because only CDS for Apps System Administrators are authorized to perform data export operations, these APIs enforce caller authorization through the use of Azure Active Directory ([AAD](https://azure.microsoft.com/en-us/services/active-directory/)) [security tokens](https://azure.microsoft.com/en-us/documentation/articles/active-directory-token-and-claims/). The following code snippet demonstrates generating such a token for a web application by using the administrator's name and password.   You must replace the `AppId`, `crmAdminUser` and `crmAdminPassword` with values appropriate to your service. This approach can be used for development and testing, but more secure means should be used for production, such as the use of Azure Key Vault.  
  
```csharp  
  
//Reference Azure AD authentication Library (ADAL)    
using Microsoft.IdentityModel.Clients.ActiveDirectory;  
   . . .  
    string yourAppClientID = "[app-associated-GUID]";   //Your AAD-registered AppId   
    string crmAdminUser = "admin1@contoso.com";  //Your CRM administrator user name  
    string crmAdminPassword = "Admin1Password";  //Your CRM administrator password;   
    //For interactive applications, there are overloads of AcquireTokenAsync() which prompt for password.   
    var authParam = AuthenticationParameters.CreateFromResourceUrlAsync(new   
        Uri("https://discovery.crmreplication.azure.net/crm/exporter/aad/challenge")).Result;  
    AuthenticationContext authContext = new AuthenticationContext(authParam.Authority, false);  
    string token = authContext.AcquireTokenAsync(authParam.Resource, yourAppClientID,   
        new UserCredential(crmAdminUser, crmAdminPassword)).Result.AccessToken;  
  
```  
  
For instructions on how to obtain a `AppId` see [Authorize access to web applications using OAuth 2.0 and Azure Active Directory](https://azure.microsoft.com/en-us/documentation/articles/active-directory-protocols-oauth-code/). For more information about Azure user security, see [Authentication Scenarios for Azure AD](https://azure.microsoft.com/en-us/documentation/articles/active-directory-authentication-scenarios/).  
  
### Error handling and failure processing  
 Once a profile is correctly configured, the synchronization process is typically highly reliable. However, if a record fails to synchronize, the following failure processing is applied:  
  
1. After the configured retry interval, another attempt is made to synchronize the record. This is repeated up to the configured maximum number of retries.  
  
2. The record is marked as processed.  
  
3. A corresponding failed record entry is written to the error log.  
  
4. The next record is processed.  
  
Because the record is marked as processed, no future attempt is made to synchronize the record until its value or schema changes. (Note that writing identical values back into an entity instance also marks it as modified.)  
  
The entries in the error log are write-only. Future successes or failures during synchronization of the same record do not result in the alteration of past entries for this record. For example, a failure entry will remain in the error log even after the record has been successfully synchronized during some later synchronization cycle.  
  
> [!CAUTION]
>  This error processing logic is subject to change in future releases of this service.  
  
These failure entries can be retrieved through the [Get the failure details for a given Profile](https://discovery.crmreplication.azure.net/swagger/ui/index) request. The response returns a URI to an Azure blob that contains the failure information.  Each line has the following comma-separated fields (newlines added for clarity):  
  
```  
  
Entity: <entity-name>,   
RecordId: <”N/A” | guid>,   
NotificationTime: <datetime>,   
ChangeType: <sync-type>,  
FailureReason: <description>  
  
```  
  
For example:  
  
```  
  
Entity: lead,   
RecordId: N/A, NotificationTime: , ChangeType: Trigger Initial Export, FailureReason: There is already an object named 'hatest201_lead' in the database.  
Entity: account, RecordId: b2a19cdd-88df-e311-b8e5-6c3be5a8b200, NotificationTime: 8/31/2016 6:50:38 PM, ChangeType: New, FailureReason: Invalid object name 'dbo.hatest201_account'.  
```  
  
### See also  
 [Manage your data in Dynamics 365](/dynamics365/customer-engagement/developer/manage-data)   
 [Import data](import-data.md)
