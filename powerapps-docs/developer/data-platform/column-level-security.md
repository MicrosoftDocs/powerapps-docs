---
title: Column-level security with code
description: "Learn how developers use code to secure data for specific columns or fields in a table so that only specified users and teams can view or set the values."
ms.date: 07/29/2025
ms.reviewer: jdaly
ms.topic: article
author: paulliew
ms.subservice: dataverse-developer
ms.author: paulliew
search.audienceType: 
  - developer
---
# Column-level security with code

Column-level security is applied for columns that contain sensitive information. Passwords, bank account numbers, government ID, telephone numbers, or email addresses can be secured at the column level.

This article explains how developers can work with column-level security capabilities using code and the Dataverse SDK for .NET or Web API. You don't need to write code to use this feature. [Learn how to configure column-level security to control access](/power-platform/admin/field-level-security). Developers should also understand how to configure column-level security using [Power Apps](https://powerapps.microsoft.com/).

## Discover which columns are secured

Detect which columns are secured by retrieving the definition of the column and examining the boolean [AttributeMetadata.IsSecured property](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.issecured). 

There are two ways to discover which columns are secured with code. These ways are described in the following two sections:

- [Retrieve column data filtered on IsSecured](#retrieve-column-data-filtered-on-issecured)
- [Retrieve FieldSecurityProfile for System Administrator role](#retrieve-fieldsecurityprofile-for-system-administrator-role)

### Retrieve column data filtered on IsSecured

This method queries the organization's metadata to identify columns marked with the `IsSecured` property set to `true`. Everyone has access to view this data. [Learn how to Query schema definitions](query-schema-definitions.md)

The resulting CSV file contains two columns: **Table** and **Column**, representing the schema names  of the tables and their secured
columns, respectively.

#### [SDK for .NET](#tab/sdk)

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="GetSecuredColumns":::

#### [Web API](#tab/webapi)

This JSON represents the [EntityQueryExpression](/power-apps/developer/data-platform/webapi/reference/entityqueryexpression) data used with the `Query` parameter with the [RetrieveMetadataChanges Function](/power-apps/developer/data-platform/webapi/reference/retrievemetadatachanges) to return data about columns that are secured using the [AttributeMetadata](/power-apps/developer/data-platform/webapi/reference/attributemetadata)`.IsSecured` property.

```json
{
   "Properties": {
      "AllProperties": false,
      "PropertyNames": ["SchemaName","Attributes"]
   },
   "Criteria": {
      "FilterOperator": "And",
      "Conditions": []
   },
   "AttributeQuery": {
      "Properties": {
         "AllProperties": false,
         "PropertyNames": [
            "SchemaName", "IsSecured"
         ]
      },
      "Criteria": {
         "FilterOperator": "And",
         "Conditions": [
            {
               "ConditionOperator": "Equals",
               "PropertyName": "IsSecured",
               "Value": {
                  "Type": "System.Boolean",
                  "Value": "true"
               }
            }
         ]
      }
   }
}
```

**Request**:

This JSON is URL encoded before sending:

```http
GET [ORGANIZATION URI]/api/data/v9.2/RetrieveMetadataChanges(Query=@p1)?@p1=%7b+%22Properties%22%3a+%7b+%22AllProperties%22%3a+false%2c+%22PropertyNames%22%3a+%5b%22SchemaName%22%2c%22Attributes%22%5d+%7d%2c+%22Criteria%22%3a+%7b+%22FilterOperator%22%3a+%22And%22%2c+%22Conditions%22%3a+%5b%5d+%7d%2c+%22AttributeQuery%22%3a+%7b+%22Properties%22%3a+%7b+%22AllProperties%22%3a+false%2c+%22PropertyNames%22%3a+%5b+%22SchemaName%22%2c+%22IsSecured%22+%5d+%7d%2c+%22Criteria%22%3a+%7b+%22FilterOperator%22%3a+%22And%22%2c+%22Conditions%22%3a+%5b+%7b+%22ConditionOperator%22%3a+%22Equals%22%2c+%22PropertyName%22%3a+%22IsSecured%22%2c+%22Value%22%3a+%7b+%22Type%22%3a+%22System.Boolean%22%2c+%22Value%22%3a+%22true%22+%7d+%7d+%5d+%7d+%7d+%7d HTTP/1.1
Accept: application/json
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**:

> [!NOTE]
> The data represented in this response was edited to remove null property values returned in the `EntityMetadata` property and it only returns a single representative secured column. In reality, the total amount of data returned is large depending on the number of tables in your environment.

This example shows how the [Account.OpenDeals column](/dynamics365/developer/reference/entities/account#BKMK_OpenDeals) is one of the secured columns.

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Content-Length: 5324876

{
   "@odata.context": "[ORGANIZATION URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse",
   "ServerVersionStamp": "152647645!07/11/2025 22:09:13",
   "DeletedMetadata": {
      "Count": 0,
      "IsReadOnly": false,
      "Keys": [],
      "Values": []
   },
   "EntityMetadata": [
      {
         "SchemaName": "Account",
         "MetadataId": "70816501-edb9-4740-a16c-6a5efbc05d84",
         "Attributes": [
            {
               "SchemaName": "OpenDeals",
               "MetadataId": "e10cdd44-5c7f-4ac8-a5d1-b2118926f2bd",
               "IsSecured": true
            }
         ]
      },
      Truncated for brevity...
   ]
}
```

---

### Retrieve FieldSecurityProfile for System Administrator role


This method queries the Dataverse field permission table to identify columns that the [Field Security Profile (FieldSecurityProfile)](reference/entities/fieldsecurityprofile.md) record with ID `572329c1-a042-4e22-be47-367c6374ea45` secures. This record manages access to secured columns for system administrators. Typically, only system administrators have the `prvReadFieldPermission` privilege to retrieve this data.

#### [SDK for .NET](#tab/sdk)

The static `GetSecuredColumnList` method returns fully qualified column names in the format `TableName.ColumnName`, sorted alphabetically.

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="GetSecuredColumnList":::

#### [Web API](#tab/webapi)


**Request**:

```http
GET https://[ORGANIZATION URI]/api/data/v9.2/fieldsecurityprofiles(572329c1-a042-4e22-be47-367c6374ea45)/lk_fieldpermission_fieldsecurityprofileid?$select=entityname,attributelogicalname&$count=true HTTP/1.1
Accept: application/json
Authorization: Bearer [REDACTED]
Prefer: odata.include-annotations="*"
OData-Version: 4.0
OData-MaxVersion: 4.0
```

**Response**:

The results in this example were edited for brevity to show only one example column ([Account.OpenDeals column](/dynamics365/developer/reference/entities/account#BKMK_OpenDeals)).

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
   "@odata.context": "[ORGANIZATION URI]/api/data/v9.2/$metadata#fieldpermissions(entityname,attributelogicalname)",
   "@odata.count": 20,
   "@Microsoft.Dynamics.CRM.totalrecordcount": 20,
   "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
   "value": [
      {
         "@odata.etag": "W/\"15577006\"",
         "entityname@OData.Community.Display.V1.FormattedValue": "Account",
         "entityname": "account",
         "attributelogicalname": "opendeals",
         "fieldpermissionid": "9b2606bb-0144-413a-ac56-be26922d4edb"
      },
      Truncated for brevity...
   ]
}
```

---

## Discover which columns can be secured

You can't secure every column. When you [enable column security](/power-platform/admin/field-level-security#enable-column-security) using [Power Apps](https://make.powerapps.com/), the **Enable column security** checkbox is disabled for certain fields. You don't need to manually check each column to find out if you can secure it. Write a query to retrieve which columns you can secure.

Three boolean [AttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata) properties control whether you can secure any column:

- [CanBeSecuredForCreate](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.canbesecuredforcreate)
- [CanBeSecuredForRead](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.canbesecuredforread)
- [CanBeSecuredForUpdate](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.canbesecuredforupdate)

When all of these properties are false, the column can't be secured. Some columns might only be secured for one or two of the three operations: `Create`, `Read`, and `Update`.

The following queries return this data so you can discover which columns in your environment can be secured:

### [SDK for .NET](#tab/sdk)

This static `DumpColumnSecurityInfo` method retrieves metadata about entity attributes, including security-related properties, and writes the information to a CSV file. The output file contains details such as whether columns are secured, can be secured for create, update, or read operations, and other relevant metadata.

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="DumpColumnSecurityInfo":::

### [Web API](#tab/webapi)

This JSON represents the [EntityQueryExpression](/power-apps/developer/data-platform/webapi/reference/entityqueryexpression) data used with the `Query` parameter with the [RetrieveMetadataChanges Function](/power-apps/developer/data-platform/webapi/reference/retrievemetadatachanges) to return data about whether columns can be secured using the [AttributeMetadata](/power-apps/developer/data-platform/webapi/reference/attributemetadata)`.IsSecured` property.

```json
{
   "Properties": {
      "AllProperties": false,
      "PropertyNames": ["SchemaName","Attributes"]
   },
   "Criteria": {
      "FilterOperator": "And",
      "Conditions": [
         {
            "ConditionOperator": "Equals",
            "PropertyName": "IsPrivate",
            "Value": {
               "Type": "System.Boolean",
               "Value": "false"
            }
         }
      ]
   },
   "AttributeQuery": {
      "Properties": {
         "AllProperties": false,
         "PropertyNames": [
            "SchemaName",
            "AttributeTypeName",
            "IsPrimaryName",
            "IsSecured",
            "CanBeSecuredForCreate",
            "CanBeSecuredForUpdate",
            "CanBeSecuredForRead"
         ]
      },
      "Criteria": {
         "FilterOperator": "And",
         "Conditions": [
            {
               "ConditionOperator": "NotEquals",
               "PropertyName": "AttributeTypeName",
               "Value": {
                  "Type": "Microsoft.Xrm.Sdk.Metadata.AttributeTypeDisplayName",
                  "Value": "VirtualType"
               }
            }
         ]
      }
   }
}
```

**Request**:

```http
GET [ORGANIZATION URI]/api/data/v9.2/RetrieveMetadataChanges(Query=@p1)?@p1=+%7b+%22Properties%22%3a+%7b+%22AllProperties%22%3a+false%2c+%22PropertyNames%22%3a+%5b%22SchemaName%22%2c%22Attributes%22%5d+%7d%2c+%22Criteria%22%3a+%7b+%22FilterOperator%22%3a+%22And%22%2c+%22Conditions%22%3a+%5b+%7b+%22ConditionOperator%22%3a+%22Equals%22%2c+%22PropertyName%22%3a+%22IsPrivate%22%2c+%22Value%22%3a+%7b+%22Type%22%3a+%22System.Boolean%22%2c+%22Value%22%3a+%22false%22+%7d+%7d+%5d+%7d%2c+%22AttributeQuery%22%3a+%7b+%22Properties%22%3a+%7b+%22AllProperties%22%3a+false%2c+%22PropertyNames%22%3a+%5b+%22SchemaName%22%2c+%22AttributeTypeName%22%2c+%22IsPrimaryName%22%2c+%22IsSecured%22%2c+%22CanBeSecuredForCreate%22%2c+%22CanBeSecuredForUpdate%22%2c+%22CanBeSecuredForRead%22+%5d+%7d%2c+%22Criteria%22%3a+%7b+%22FilterOperator%22%3a+%22And%22%2c+%22Conditions%22%3a+%5b+%7b+%22ConditionOperator%22%3a+%22NotEquals%22%2c+%22PropertyName%22%3a+%22AttributeTypeName%22%2c+%22Value%22%3a+%7b+%22Type%22%3a+%22Microsoft.Xrm.Sdk.Metadata.AttributeTypeDisplayName%22%2c+%22Value%22%3a+%22VirtualType%22+%7d+%7d+%5d+%7d+%7d+%7d HTTP/1.1
Accept: application/json
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**:

> [!NOTE]
> The data in this response is edited to remove null property values returned in the `EntityMetadata` property and it only returns a single representative column from one table. In reality, the total amount of data returned is large depending on the number of tables and columns in your environment.

This example shows the requested properties of the [Account.AccountCategoryCode column](/power-apps/developer/data-platform/reference/entities/account#BKMK_AccountCategoryCode) is one of the secured columns.

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
   "@odata.context": "[ORGANIZATION URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse",
   "ServerVersionStamp": "152647645!07/11/2025 23:37:54",
   "DeletedMetadata": {
      "Count": 0,
      "IsReadOnly": false,
      "Keys": [],
      "Values": []
   },
   "EntityMetadata": [
      {
         "SchemaName": "Account",
         "MetadataId": "70816501-edb9-4740-a16c-6a5efbc05d84",
         "Attributes": [
            {
               "CanBeSecuredForRead": true,
               "CanBeSecuredForCreate": true,
               "CanBeSecuredForUpdate": true,
               "IsPrimaryName": false,
               "IsSecured": false,
               "LogicalName": "accountcategorycode",
               "SchemaName": "AccountCategoryCode",
               "MetadataId": "118771ca-6fb9-4f60-8fd4-99b6124b63ad",
               "AttributeTypeName": {
                  "Value": "PicklistType"
               }
            },
            Truncated for brevity...
         ]
      },
      Truncated for brevity...
   ]
}
```

[Learn how to Query schema definitions](query-schema-definitions.md)

---

## Secure a column with code

It's easiest to [Secure a column](/power-platform/admin/field-level-security#enable-column-securit) using [Power Apps](https://make.powerapps.com/). If you need to automate securing a column, use code to update the column definition to set the [AttributeMetadata.IsSecured property](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.issecured) property as shown in the following examples:


### [SDK for .NET](#tab/sdk)

This static `SetColumnIsSecured` method retrieves the current definition of the specified column and updates its security status only if the provided value differs from the current value. If the column is already set to the specified security status, no update request is sent.

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="SetColumnIsSecured":::

[Learn how to update a column using the SDK for .NET](org-service/metadata-attributemetadata.md#update-a-column)

### [Web API](#tab/webapi)

The following `Set-ColumnIsSecured-Example` PowerShell function retrieves the current definition of the specified column and updates its security status only if the provided value differs from the current value. If the column is already set to the specified security status, no update request is sent.

This function depends on [Get-Column](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md#get-column-function) and [Update-Column](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md#update-column-function) functions defined by the [Dataverse Web API PowerShell Helper functions](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md) used by other PowerShell samples.

:::code language="powershell" source="~/../PowerApps-Samples/dataverse/webapi/PS/ColumnLevelSecurity/Examples.ps1" id="SetColumnIsSecuredExample":::

[Learn how to update a column using the Web API](webapi/create-update-column-definitions-using-web-api.md#update-a-column)

---

## Provide access to secured columns

By default, when a column is secured, only people who have the system administrator security role can read or set the value. A system administrator can provide other users access to secured columns in two ways:

- [Manage access using field security profiles](#manage-access-using-field-security-profiles): Use field security profiles to give access to column data for all records to groups.
- [Share data in secured fields](#share-data-in-secured-fields): Use field sharing to give a specific principal or team access to data in a secure column for a specific record.

### Manage access using field security profiles

This approach is the most common when you have different groups of users who require different levels of access. See the [Column-level security example](/power-platform/admin/column-level-security-example) that describes how to secure fields for different users using the Power Platform admin center.

To do this using code, create [Field Security Profile (FieldSecurityProfile)](reference/entities/fieldsecurityprofile.md) records that associate principals (users and teams) with [Field Permission (FieldPermission)](reference/entities/fieldpermission.md) records that control which data operations can be performed on that column for any record.

<!-- 
Mermaid markdown used to generate ERD after installing:
https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid -->

<!-- ```mermaid
 erDiagram
    FieldSecurityProfile {
        Guid FieldSecurityProfileId PK
        String Name
        String Description
    }
    FieldPermission {
        Guid FieldPermissionId PK
        Lookup FieldSecurityProfileId FK
        String EntityName
        String AttributeLogicalName
        Choice CanCreate
        Choice CanRead
        Choice CanUpdate
        Choice CanReadUnmasked
    }
    SystemUser {
        Guid SystemUserId PK
    }
    Team {
        Guid TeamID PK
    }

    FieldSecurityProfile ||--o{ FieldPermission : "lk_fieldpermission_fieldsecurityprofileid"
    FieldSecurityProfile }o--o{ SystemUser : "systemuserprofiles_association"
    FieldSecurityProfile }o--o{ Team : "teamprofiles_association" 
```   -->

:::image type="content" source="media/fieldsecurityprofile-erd.png" alt-text="entity relationship diagram for the fieldsecurityprofile table and related tables":::

You can associate system users and teams to your field security profile using the [systemuserprofiles_association](/power-apps/developer/data-platform/reference/entities/fieldsecurityprofile#BKMK_systemuserprofiles_association) and [teamprofiles_association](/power-apps/developer/data-platform/reference/entities/fieldsecurityprofile#BKMK_teamprofiles_association) many-to-many relationships respectively.

Associate field permissions to the field security profiles using the [`lk_fieldpermission_fieldsecurityprofileid` one-to-many relationship](reference/entities/fieldsecurityprofile.md#BKMK_lk_fieldpermission_fieldsecurityprofileid). The following table describes important field permission table columns:


|Column  |Type  |Description  |
|---------|---------|---------|
|`FieldSecurityProfileId`|Lookup|Refers to the field security profile this field permission applies to.|
|`EntityName`|String|The logical name of the table that contains the secured column.|
|`AttributeLogicalName`|String|The logical name of the secured column.|
|`CanCreate`|Choice|Whether create access is allowed. See [Field security permission type options](#field-security-permission-type-options)|
|`CanRead`|Choice|Whether read access is allowed. See [Field security permission type options](#field-security-permission-type-options)|
|`CanUpdate`|Choice|Whether update access is allowed. See [Field security permission type options](#field-security-permission-type-options)|
|`CanReadUnmasked`|Choice|Whether an unmasked value can be retrieved when `CanRead` is **Allowed**.|

#### Field security permission type options

The `CanCreate`, `CanRead`, and `CanUpdate` choice columns use the values defined by the `field_security_permission_type` global choice:

- `0` **Not Allowed**
- `4` **Allowed**

> [!NOTE]
> Don't set `CanReadUnmasked` column unless you're using the [display masked data](#display-masked-data) feature and you want to enable an app to return the unmasked value.

### Share data in secured fields

Create [Field Sharing (PrincipalObjectAttributeAccess)](reference/entities/principalobjectattributeaccess.md) records to share access to a secured field for a specific record with someone else.

> [!NOTE]
> Conceptually, this process is similar to the [PrincipalObjectAccess](reference/entities/principalobjectaccess.md) table that manages sharing of records. The difference is that with *record sharing* you use the `GrantAccess`, `ModifyAccess`, and `RevokeAccess` messages to add, modify, and remove records from the `PrincipalObjectAccess` table. [Learn more about sharing records](security-sharing-assigning.md#sharing-records)
>
> With *field sharing*, use the `PrincipalObjectAttributeAccess` table to grant, modify, and revoke field access using create, update, and delete operations on a table row.

The `PrincipalObjectAttributeAccess` table has these columns:

|Column  |Type  |Description  |
|---------|---------|---------|
|`AttributeId`|Guid|The [AttributeMetadata.MetadataId](/dotnet/api/microsoft.xrm.sdk.metadata.metadatabase.metadataid) of the secured column. |
|`ObjectId`|Lookup|A reference to the record that contains the secured column.|
|`PrincipalId`|Lookup|A reference to the principal (user or team) you're granting access to.|
|`ReadAccess`|Bool|Whether to grant read access to the field data|
|`UpdateAccess`|Bool|Whether to grant update access to the field data|


#### Getting column AttributeId

The `PrincipalObjectAttributeAccess.AttributeId` column uses the [AttributeMetadata.MetadataId](/dotnet/api/microsoft.xrm.sdk.metadata.metadatabase.metadataid) rather than the column logical name. You need to retrieve this value from the metadata. If your application has a metadata cache, you can include this data and access it as needed.

#### Retrieve column AttributeId example

This example shows how to get the [AttributeMetadata.MetadataId](/dotnet/api/microsoft.xrm.sdk.metadata.metadatabase.metadataid) value you need to set the `PrincipalObjectAttributeAccess.AttributeId` column value.

##### [SDK for .NET](#tab/sdk)

The [Grant column access](#grant-column-access-example), [Modify column access](#modify-column-access-example), and [Revoke column access](#revoke-column-access-example) SDK for .NET examples use the `RetrieveColumnId` static method to retrieve the [AttributeMetadata.MetadataId](/dotnet/api/microsoft.xrm.sdk.metadata.metadatabase.metadataid) value used in the `PrincipalObjectAttributeAccess.AttributeId` column.

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="RetrieveColumnId":::

[Learn how to query schema definitions](query-schema-definitions.md)


##### [Web API](#tab/webapi)

This example returns the column `MetadataId` when the table `LogicalName` is `account` and the column `LogicalName` is `name`.

**Request**:

```http
GET [Organization URL]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='name')/MetadataId HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response**:

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
   "@odata.context": "[Organization URL]/api/data/v9.2/$metadata#EntityDefinitions('account')/Attributes('name')/MetadataId",
   "value": "a1965545-44bc-4b7b-b1ae-93074d0e3f2a"
}
```

---


#### Grant column access example

These examples create a new [Field Sharing (PrincipalObjectAttributeAccess)](reference/entities/principalobjectattributeaccess.md) record to share access to the specified field.

##### [SDK for .NET](#tab/sdk)

This method allows you to share read and/or update permissions for a secured column in a Dataverse table with a specific principal (user or team). The column must be configured as a secured field in Dataverse.

This example depends on the `RetrieveColumnId` example function found in [Retrieve column AttributeId example](#retrieve-column-attributeid-example).

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="GrantColumnAccess":::

##### [Web API](#tab/webapi)

This example grants the user with `systemuserid` value of `d93e9712-5c0b-f011-bae2-7c1e526458ff` read access to the value of the column that has `AttributeMetadata.MetadataId` of `0134fc5f-cb61-f011-bec2-00224823101f` for the `sample_example` table record with primary key value of `eccf556c-cb61-f011-bec2-7ced8d1ef7ad`.


**Request**:

```http
POST [ORGANIZATION URI]/api/data/v9.2/principalobjectattributeaccessset HTTP/1.1
Accept: application/json
Authorization: Bearer [REDACTED]
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json

{
  "objectid_sample_example@odata.bind": "/sample_examples(eccf556c-cb61-f011-bec2-7ced8d1ef7ad)",
  "attributeid": "0134fc5f-cb61-f011-bec2-00224823101f",
  "updateaccess": false,
  "principalid_systemuser@odata.bind": "/systemusers(d93e9712-5c0b-f011-bae2-7c1e526458ff)",
  "@odata.type": "Microsoft.Dynamics.CRM.principalobjectattributeaccess",
  "readaccess": true
}
```

**Response**:

The primary key value for the created record is `784a01b1-cb61-f011-bec2-00224823101f`. Use this value to identify records to modify or delete access.

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [ORGANIZATION URI]/api/data/v9.2/principalobjectattributeaccessset(784a01b1-cb61-f011-bec2-00224823101f)
```

[Learn to create a table row using the Web API](webapi/create-entity-web-api.md)

---

#### Modify column access example

These examples retrieve and update an existing [Field Sharing (PrincipalObjectAttributeAccess)](reference/entities/principalobjectattributeaccess.md) record to modify access to the specified field.

##### [SDK for .NET](#tab/sdk)

This example depends on the `RetrieveColumnId` example function found in [Retrieve column AttributeId example](#retrieve-column-attributeid-example).

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="ModifyColumnAccess":::

##### [Web API](#tab/webapi)

This example modifies the access granted in the [Grant column access example](#grant-column-access-example) to include update access.

**Request**:

```http
PATCH [ORGANIZATION URI]/api/data/v9.2/principalobjectattributeaccessset(784a01b1-cb61-f011-bec2-00224823101f) HTTP/1.1
Accept: application/json
Authorization: Bearer [REDACTED]
OData-Version: 4.0
If-Match: *
OData-MaxVersion: 4.0
Content-Type: application/json

{
  "updateaccess": true
}
```

**Response**:

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

[Learn how to update a record using Web API](webapi/update-delete-entities-using-web-api.md#basic-update)

---

#### Revoke column access example

These examples retrieve and delete an existing [Field Sharing (PrincipalObjectAttributeAccess)](reference/entities/principalobjectattributeaccess.md) record to revoke access to the specified field.

##### [SDK for .NET](#tab/sdk)

This example depends on the `RetrieveColumnId` example function found in [Retrieve column AttributeId example](#retrieve-column-attributeid-example).

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="RevokeColumnAccess":::

##### [Web API](#tab/webapi)

This example removes the access that was granted in the [Grant column access example](#grant-column-access-example).


**Request**:

```http
DELETE [ORGANIZATION URI]/api/data/v9.2/principalobjectattributeaccessset(784a01b1-cb61-f011-bec2-00224823101f) HTTP/1.1
Accept: application/json
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**:

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

[Learn to delete a record using Web API](webapi/update-delete-entities-using-web-api.md#basic-delete)

---

## Display Masked data

The default API behavior when returning a value for a secured column is to return no data. The calling application can't distinguish between a value that is secured and a value that is null.

[There's now a preview feature](/power-platform/admin/create-manage-masking-rules) you can use to specify that a string value is returned when data exists. This string might totally obfuscate the value or show portions of the data depending on masking rules you define. In this way, the application can better manage sensitive data.

With this feature, you can configure [Field Permission (FieldPermission)](reference/entities/fieldpermission.md) records to create field security profiles that enable applications to send requests to retrieve records with the masking removed so that the data can be shown under controlled circumstances. [Learn more about retrieving unmasked data](#retrieve-unmasked-data)

### Create a secure masking rule

Every column that displays masked data needs to refer to a [Secured Masking Rule (MaskingRule)](reference/entities/maskingrule.md) table row. You can create secure masking rules in Power Apps and add them to your solution, or you can use any of the existing rules.

Create [Secured Masking Column (AttributeMaskingRule)](reference/entities/attributemaskingrule.md) table records to specify which masking rule a secure column should use.

The following diagram describes these tables:

:::image type="content" source="media/maskingrule-attributemaskingrule-erd.png" alt-text="Diagram showing columns and relationships between the MaskingRule and AttributeMaskingRule tables":::

<!-- 
Mermaid markdown used to generate ERD after installing:
https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid -->
<!-- ```mermaid
 erDiagram
    MaskingRule {
        Guid MaskingRuleId PK
        String Name
        String Description
        String DisplayName
        BooleanManagedProperty IsCustomizable
        String MaskedCharacter
        String RegularExpression
        String RichTestData
        String MaskedRichTestData
        String TestData
        String MaskedTestData
    }
    AttributeMaskingRule {
        Guid AttributeMaskingRuleId PK
        String AttributeLogicalName
        String EntityName
        BooleanManagedProperty IsCustomizable
        Lookup MaskingRuleId FK
        String UniqueName
    } 

    MaskingRule ||--o{ AttributeMaskingRule : "maskingrule_attributemaskingrule"
```   -->

#### Secured Masking Rule columns

The [Secured Masking Rule (MaskingRule)](reference/entities/maskingrule.md) table has these write-able columns:

|Column|Type|Description|
|---|---|---|
|`Name`|String|The unique name of the secured masking rule.|
|`Description`|String|Description of the secured masking rule.|
|`DisplayName`|String|The display name of the secured masking rule.|
|`MaskedCharacter`|String|Character used to mask.|
|`RegularExpression`|String|Regular Expression in C#.|
|`IsCustomizable`|BooleanManagedProperty|Information that specifies whether this component can be customized. [Learn more about managed properties](/power-platform/alm/managed-properties-alm)|
|`RichTestData`|String|Set rich text test data to test this secured masking rule.|
|`MaskedRichTestData`|String|`RichTestData` column data evaluated by this secured masking rule.|
|`TestData`|String|Set test data to test this secured masking rule.|
|`MaskedTestData`|String|`TestData` column data evaluated by a secured masking rule.|

> [!NOTE]
> The `RichTestData`, `MaskedRichTestData`, `TestData`, and `MaskedTestData` columns exist to support the experience to test masking rules in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). [Learn more about creating masking rules](/power-platform/admin/create-manage-masking-rules#create-masking-rules).

#### Secured Masking Column columns

The [Secured Masking Column (AttributeMaskingRule)](reference/entities/attributemaskingrule.md) table has these write-able columns:

|Column|Type|Description|
|---|---|---|
|`AttributeLogicalName`|String|Logical name of the column for which the secured masking rule is used.|
|`EntityName`|String|Logical name of the table that contains the column.|
|`MaskingRuleId`|Lookup|The masking rule that the column uses|
|`UniqueName`|String|The unique name of the secured masking column.|
|`IsCustomizable`|BooleanManagedProperty|Information that specifies whether this component can be customized. [Learn more about managed properties](/power-platform/alm/managed-properties-alm)|


### Retrieve unmasked data

When a [Field Permission (FieldPermission)](reference/entities/fieldpermission.md) record `CanRead` column is **Allowed**, you can set the `CanReadUnmasked` choice column when the column has an [Secured Masking Column (AttributeMaskingRule)](reference/entities/attributemaskingrule.md) record associated with it.

The `CanReadUnmasked` column supports the following options defined by the `field_security_permission_readunmasked` global choice.

|Value|Label|Description|
|---|---|---|
|0|**Not Allowed**|The default value. If there isn't an `AttributeMaskingRule` for the column, you can't set any other value.|
|1|**One Record**|Unmasked data can be returned using the a `Retrieve` operation only.|
|3|**All Records**|Unmasked data can be returned using the a `Retrieve` and `RetrieveMultiple` operations.|


#### Retrieve unmasked data example

The following examples show how to use the [`UnMaskedData` optional parameter](optional-parameters.md#return-unmasked-data) to request that the unmasked value is returned when the configuration of the field permission allows it.

### [SDK for .NET](#tab/sdk)

The `GetUnmaskedExampleRows` example returns unmasked values for any of the requested columns where the field permission `CanReadUnmasked` column value is set to **All Records** because the optional `UnMaskedData` parameter is added to the `RetrieveMultiple` request.

This method queries the `sample_example` table and retrieves specific columns, including sensitive data such as government ID and date of birth. The query results are ordered by the `sample_name` column in descending order.

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/Examples.cs" id="GetUnmaskedExampleRows":::

### [Web API](#tab/webapi)

**Request:**

```http
GET [ORGANIZATION URI]/api/data/v9.2/sample_examples?$select=sample_name,sample_email,sample_governmentid,sample_telephonenumber,sample_dateofbirth&$orderby=sample_name%20desc&UnMaskedData=true HTTP/1.1
Accept: application/json
Authorization: Bearer [Redacted]
Prefer: odata.include-annotations="*"
OData-Version: 4.0
OData-MaxVersion: 4.0
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
   "@odata.context": "[ORGANIZATION URI]/api/data/v9.2/$metadata#sample_examples(sample_name,sample_email,sample_governmentid,sample_telephonenumber,sample_dateofbirth)",
   "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
   "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
   "@Microsoft.Dynamics.CRM.globalmetadataversion": "153019637",
   "value": [
      {
         "@odata.etag": "W/\"153019647\"",
         "sample_email": "jaydenp@adatum.com",
         "sample_governmentid": "***-**-5353",
         "sample_dateofbirth": "3/25/1974",
         "sample_name": "Jayden Phillips",
         "sample_exampleid": "eccf556c-cb61-f011-bec2-7ced8d1ef7ad",
         "sample_telephonenumber": "(736) 555-9012"
      },
      {
         "@odata.etag": "W/\"153012339\"",
         "sample_email": "benjamin@adventure-works.com",
         "sample_governmentid": "***-**-7508",
         "sample_dateofbirth": "6/18/1984",
         "sample_name": "Benjamin Stuart",
         "sample_exampleid": "edcf556c-cb61-f011-bec2-7ced8d1ef7ad",
         "sample_telephonenumber": "(195) 555-7901"
      },
      {
         "@odata.etag": "W/\"153012340\"",
         "sample_email": "avery@alpineskihouse.com",
         "sample_governmentid": "***-**-1720",
         "sample_dateofbirth": "9/4/1994",
         "sample_name": "Avery Howard",
         "sample_exampleid": "eecf556c-cb61-f011-bec2-7ced8d1ef7ad",
         "sample_telephonenumber": "(152) 555-5591"
      }
   ]
}
```

---

### Related articles

[Security and data access](security-model.md)   
[Sharing and assigning](security-sharing-assigning.md)   
[Sample: Column-level security using Dataverse SDK for .NET](org-service/samples/column-level-security.md)   
[Sample: Column-level security using Dataverse Web API (PowerShell)](webapi/samples/column-level-security-powershell.md)
