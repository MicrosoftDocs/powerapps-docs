---
title: "Web API Functions and Actions Sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to call bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API and C#."
ms.date: 09/02/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Functions and Actions Sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This .NET 6.0 sample demonstrates how to perform common data operations using the Dataverse Web API.

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).
  
> [!NOTE]
> This sample implements the Dataverse operations and console output detailed in [Web API Functions and Actions Sample](../web-api-conditional-operations-sample.md) and uses the common C# constructs described in [Web API Samples (C#)](../web-api-samples-csharp.md).

## Prerequisites

The following is required to build and run this sample:

- Microsoft Visual Studio 2022.
- Access to Dataverse with privileges to perform data operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the [/dataverse/webapi/C#-NETx/FunctionsAndActions/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23-NETx/FunctionsAndActions) folder.
1. Open the `FunctionsAndActions.sln` file using Visual Studio 2022
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find this. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Press F5 to run the sample.

## Code

The code for this sample is here: [PowerApps-Samples/dataverse/webapi/C#-NETx/FunctionsAndActions/Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/FunctionsAndActions/Program.cs)

## Demonstrates

This sample has 9 regions:

### Section 1: Unbound Functions: WhoAmI

Operation: Send <xref:Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI Function> and recieve <xref:Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType>.

### Section 2: Unbound Functions: FormatAddress

Operations:

1. Send <xref:Microsoft.Dynamics.CRM.FormatAddress?text=FormatAddress Function> with parameters for an address in the United States. Recieve <xref:Microsoft.Dynamics.CRM.FormatAddressResponse?text=FormatAddressResponse ComplexType> with the formatted address.
1. Do the same with parameters for an address in Japan.

### Section 3: Unbound Functions: InitializeFrom

Operations:

1. Create an account record to be the original record.
1. Send <xref:Microsoft.Dynamics.CRM.InitializeFrom?text=InitializeFrom Function> with parameters referencing the account record created. Recieve a response with data to create a new account record with values from the original record.
1. Create a new account record using the data from `InitializeFromResponse` so that the new record is associated with the original record and potentially containing data copied from the original record, depending on how the column mappings are configured for the organization.

### Section 4: Unbound Functions: RetrieveCurrentOrganization

Operation: Send <xref:Microsoft.Dynamics.CRM.RetrieveCurrentOrganization?text=RetrieveCurrentOrganization Function> and recieve <xref:Microsoft.Dynamics.CRM.RetrieveCurrentOrganization?text=RetrieveCurrentOrganization ComplexType>.

### Section 5: Unbound Functions: RetrieveTotalRecordCount

Operations: Send <xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount?text=RetrieveTotalRecordCount Function> with parameters for `account` and `contact` tables and recieve <xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCountResponse?text=RetrieveTotalRecordCountResponse ComplexType> containing the number of records in each table.

### Section 6: Bound Functions: IsSystemAdmin

Operations:

1. Detect if organization has the `sample_IsSystemAdmin` custom API installed.
1. If not, install solution in `IsSystemAdminFunction_1_0_0_0_managed.zip` containing the custom API.
1. Retrieve 10 systemuser records.
1. Loop through the records using the `sample_IsSystemAdmin` function to detect which ones have the System Administrator security role.

### Section 7: Unbound Actions: GrantAccess

Operations:

1. Create an account record to share.
1. Retrieve an enabled user other than the current user.
1. Use the <xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function> to determine if the other user has <xref:Microsoft.Dynamics.CRM.AccessRights>`'DeleteAccess'` on the account record created.
1. If they do not have `DeleteAccess`, use <xref:Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action> to share this access to the other user.
1. Test the user's access again using `RetrievePrincipalAccess` to verify that they now have `DeleteAccess`.

### Section 8: Bound Actions: AddPrivilegesRole

Operations:

1. Create a <xref:Microsoft.Dynamics.CRM.role?text=role EntityType> record associated with the caller's business unit.
1. Retrieve the role record with expanded <xref:Microsoft.Dynamics.CRM.privilege?text=privilege EntityType> records to show the privileges included by default.
1. Retrieve information about the `prvCreateAccount` and `prvReadAccount` privileges.
1. Use the retrieved information about those privileges to prepare a list of <xref:Microsoft.Dynamics.CRM.RolePrivilege?text=RolePrivilege ComplexType> instances to be parameters for `AddPrivilegesRole`.
1. Send <xref:Microsoft.Dynamics.CRM.AddPrivilegesRole?text=AddPrivilegesRole Action> with the `RolePrivilege` parameters.
1. Retrieve the role record again with expanded <xref:Microsoft.Dynamics.CRM.privilege?text=privilege EntityType> records to show the privileges now include the `prvCreateAccount` and `prvReadAccount` privileges.

### Section 9: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. This section sends a `$batch` request to delete the record.

## Clean up

By default this sample will delete all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you will be prompted to decide if you want to delete the records.

### See also

[Perform conditional operations using the Web API](../perform-conditional-operations-using-web-api.md)<br />
[Use the Dataverse Web API](../overview.md)<br />
[WebAPIService class library (C#)](webapiservice.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Basic Operations Sample (C#)](webapiservice-basic-operations.md)<br />
[Web API Query Data sample (C#)](webapiservice-query-data.md)<br />
[Web API Conditional Operations sample (C#)](webapiservice-conditional-operations.md)<br />
[Web API Metadata Operations Sample (C#)](webapiservice-metadata-operations.md)<br />
[Web API WebApiService Parallel Operations Sample (C#)](webapiservice-parallel-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
