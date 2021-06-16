---
title: "Catalog and CatalogAssignment tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use the Catalog and CatalogAssignment tables to expose events in your solution"
ms.custom: ""
ms.date: 06/08/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Catalog and CatalogAssignment tables

Use the [Catalog](reference/entities/catalog.md) and [CatalogAssignment](reference/entities/catalogassignment.md) tables to create a structure to expose actions used in your solution as business events. Microsoft Dataverse Business events is a new capability currently being developed. Business events will enable many scenarios to create integrations with many applications through Dataverse. More information: [Microsoft Dataverse business events](business-events.md)

Your catalog will describe those events that are relevant to your solution so that people can use them. If you do not catalog the events relevant to your solution, they may not be available to people using your solution.

Use the Catalog table to create a two level hierarchy. This will create a **Catalog** and **Category** group where the second level catalog represents the category.

The first level catalog must represent your solution. Use multiple second-level catalogs related to your first level catalog to group different categories of functionality within your solution.

For each second-level catalog that represents the categories within your solution, you will use the CatalogAssignment table to specify any Tables, Custom API, or Custom Process actions you want to be available as events. Only Custom API that are configured as Actions can be used.

> [!IMPORTANT]
> In order for people to use Catalogs and Catalog Assignments, they must be given read access to these these tables. Currently only the System Administrator has full access to the Catalog and Catalog Assignment tables.
> You must grant **Read** access to the security roles assigned to any users who will need to use these tables. These tables are found within the **Custom Entities** tab when you edit a security role.
> 
> More information: 
> - [Edit a security role](/power-platform/admin/create-edit-security-role#edit-a-security-role)
> - [Security roles and privileges](/power-platform/admin/security-roles-privileges)

## Example: Contoso Customer Management

To introduce the idea of a catalog, let's start with an example.

Contoso Customer management solution contains many components. The only components of interest here are: 
- Tables
- Custom API
- Custom Process Action (workflow)

### Tables

Contoso Customer management is a solution which includes the following tables:


|SchemaName |Display Name  |Description  |
|---------|---------|---------|
|`Account`|Account|A Dataverse system table|
|`Contact`|Contact|A Dataverse system table|
|`contoso_Membership`|Membership|A custom table|

### Custom API

They have also created a number of Custom API actions which are called by their point-of-sale system, their Web site, and ERP systems to notify Dataverse of events that do not originate within Dataverse:

|UniqueName  |DisplayName  |
|---------|---------|
|`contoso_CustomerEnteredStore`|Entered Store|
|`contoso_CustomerVisitWebSite`|Visit Web Site|
|`contoso_CustomerPurchasedProduct`|Purchased Product|
|`contoso_CustomerReturnedProduct`|Returned Product|

### Catalog structure

The Contoso Customer management solution catalog looks like this:

|Catalog  |Description  |
|---------|---------|
|Contoso Customer Management|Root Catalog|
|&nbsp;&nbsp;&nbsp;&nbsp;Tables|2nd Level Catalog Category|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Account|CatalogAssignment: Entity|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contact|CatalogAssignment: Entity|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Membership|CatalogAssignment: Entity|
|&nbsp;&nbsp;&nbsp;&nbsp;Customer Events|2nd Level Catalog Category|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entered Store|CatalogAssignment: CustomAPI|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Visit Web Site|CatalogAssignment: CustomAPI|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Purchase Product|CatalogAssignment: CustomAPI|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return Product|CatalogAssignment: CustomAPI|


### Events available

When you make a CatalogAssignement to a table, any system bound operations for that table become available as events.

With this catalog, the following events will be available:

|Table  |Event  |Why available  |
|---------|---------|---------|
|Account|Create<br />Update<br />Delete| Standard Data Operation |
|Contact|Create<br />Update<br />Delete| Standard Data Operation |
|Membership|Create<br />Update<br />Delete| Standard Data Operation |
|N/A|`contoso_CustomerEnteredStore`|Explicit Catalog Assignment|
|N/A|`contoso_CustomerVisitWebSite`|Explicit Catalog Assignment|
|N/A|`contoso_CustomerPurchasedProduct`|Explicit Catalog Assignment|
|N/A|`contoso_CustomerReturnedProduct`|Explicit Catalog Assignment|

Most tables will support **Create**, **Update**, and **Delete** events. There are some exceptions.

> [!NOTE]
> More specialized events bound to tables are planned. As those events are enabled, your catalog assignments will include those events.
>
> For example:
> - User-owned tables will include **GrantAccess**, **ModifyAccess**, **RevokeAccess** events
> - Those tables that support the **Merge** action will include that event.



<!--  Describes events to be enabled in future
|Table  |Event  |Why available  |
|---------|---------|---------|
|Account|Create<br />Update<br />Delete| Standard Data Operation |
|Account|GrantAccess<br />ModifyAccess<br />RevokeAccess|User owned entity can be shared.|
|Account|Merge|Account table supports merge operations|
|Contact|Create<br />Update<br />Delete| Standard Data Operation |
|Contact|GrantAccess<br />ModifyAccess<br />RevokeAccess|User owned entity can be shared.|
|Contact|Merge|Contact table supports merge operations|
|Membership|Create<br />Update<br />Delete| Standard Data Operation |
|Membership|GrantAccess<br />ModifyAccess<br />RevokeAccess|User owned entity can be shared.|
|N/A|`contoso_CustomerEnteredStore`|Explicit Catalog Assignment|
|N/A|`contoso_CustomerVisitWebSite`|Explicit Catalog Assignment|
|N/A|`contoso_CustomerPurchasedProduct`|Explicit Catalog Assignment|
|N/A|`contoso_CustomerReturnedProduct`|Explicit Catalog Assignment|

- Most Tables will support Create, Update, and Delete events. There are some exceptions.
- User-owned Tables can be shared, and sharing can be changed or revoked. The events for those operations will be included with the tables.
- Certain system tables support special operations, such as Merge.
- Any custom table will not have any additional events, unless they are user-owned.

-->

Any Custom API or Custom Process Actions, even if they are bound to a table, must be explicitly assigned.

## Catalog table columns

All the available columns and relationships are available in [Catalog table/entity reference](reference/entities/catalog.md).

The following table includes selected columns/attributes of a Catalog table/entity that you can set.


|Display Name<br/>`SchemaName`<br/>`LogicalName`|Type|Description  |
|---------|---------|---------|
|Catalog<br/>`CatalogId`<br/>`catalogid`|Uniqueidentifier|Unique identifier for catalog instances.|
|Description<br/>`Description`<br/>`description`|String|Localized description for catalog instances.<br/>**Required**|
|Display Name<br/>`DisplayName`<br/>`displayname`|String|Localized display name for catalog instances.<br/>**Required**|
|Is Customizable<br/>`IsCustomizable`<br/>`iscustomizable`|ManagedProperty|Controls whether the Catalog can be customized or deleted.<br/>**Required**|
|Name<br/>`Name`<br/>`name`|String|The primary name of the catalog.<br/>**Required**|
|Parent Catalog<br/>`ParentCatalogId`<br/>`parentcatalogid`|Lookup|Unique identifier for the Parent Catalog.<br />**Cannot be changed after it is saved.**|
|Unique Name<br/>`UniqueName`<br/>`uniquename`|String|Unique name for the catalog.<br/>**Required**<br/>Must begin with a customization prefix.|

> [!NOTE]
> Unless you want to allow people who install your managed solution to modify your catalog, you should set the **Is Customizable** managed property to false.
>
> When you associate a Catalog Assignment to a Catalog, you will not be able to delete the catalog until you remove the catalog assignment.


## CatalogAssignment Table Columns

All the available columns and relationships are available in [CatalogAssignment table/entity reference](reference/entities/catalogassignment.md).

The following table includes selected columns/attributes of a CatalogAssignment table/entity that you can set.

|Display Name<br/>`SchemaName`<br/>`LogicalName`|Type|Description  |
|---------|---------|---------|
|Catalog Assignment<br/>`CatalogAssignmentId`<br/>`catalogassignmentid`|Uniqueidentifier|Unique identifier for catalog assignment instances.  |
|catalog<br/>`CatalogId`<br/>`catalogid`|Lookup|Unique identifier for the catalog associated with the catalog assignment.<br/>**Required**|
|Is Customizable<br/>`IsCustomizable`<br/>`iscustomizable`|ManagedProperty|Controls whether the CatalogAssignment can be customized or deleted.<br/>**Required**|
|Name<br/>`Name`<br/>`name`|String|The primary name of the catalog assignment.  |
|Catalog Assignment Object<br/>`Object`<br/>`object`|Lookup|Unique identifier for the object associated with the catalog assignment.<br/>**Required**<br />**Cannot be changed after it is saved.**<br />This polymorphic lookup can be linked to the following tables:<br/>&nbsp;&nbsp;customapi<br />&nbsp;&nbsp;entity<br />&nbsp;&nbsp;workflow<br/><br/>When using the Web API to associate this polymorphic relationship, you must use the single-valued navigation property names for each relationship.<br/><br/>These names are:<br/>&nbsp;&nbsp;`CustomAPIId`<br />&nbsp;&nbsp;`EntityId`<br />&nbsp;&nbsp;`WorkflowId`<br /><br />When associating to a table, custom api, or custom process action you will need to get the respectiveid value. See [Get the Id for CatalogAssignment items](#get-the-id-for-catalogassignment-items) for more information.|

> [!NOTE]
> Unless you want to allow people who install your managed solution to modify your catalog assignments, you should set the **Is Customizable** managed property to false.


### Get the Id for CatalogAssignment items

You will need to get the id of entities, custom apis, and custom process actions when you associate them with a CatalogAssignment.

#### Get the Id of a table

The Entity table contains multiple rows for each table. One for each layer in the solution. You can get the Id for a specific table, such as the Account table, using either of these queries using the Web API:

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='account')?$select=MetadataId
```

```http
GET [Organization URI]/api/data/v9.2/entities?$select=entityid&$filter=name eq 'Account'&$top=1
```


#### Get the Id of a Custom API

This is most easily done using the Web API. The following example will return the `customapiid` of a custom api with the `uniquename` of `your_CustomAPIName`.

```http
GET [Organization URI]/api/data/v9.2/customapis?$select=customapiid&$filter=uniquename eq 'your_CustomAPIName'
```

#### Get the Id of a Custom Process Action

This is most easily done using the Web API. The following example will return the `workflowid` of a custom process action with the `uniquename` of `ExampleCustomProcessAction`.

```http
GET [Organization URI]/api/data/v9.2/workflows?$select=workflowid,uniquename&$filter=category eq 3 and type eq 2 and endswith(uniquename,'ExampleCustomProcessAction')
```

> [!NOTE]
> The `uniquename` of the workflow doesn't include the customization prefix that is prepended to the name of the custom process action in the Web API. If the custom action you call from the Web API is named `new_ExampleCustomProcessAction`, the workflow uniquename will be `ExampleCustomProcessAction`.
>
> Make sure you to access the row where [Type](/powerapps/developer/data-platform/reference/entities/workflow#BKMK_Type) is `2`. This is the activated workflow.
>
> Custom process action workflows have the [Category](/powerapps/developer/data-platform/reference/entities/workflow#BKMK_Category) value of `3`.


## Create a Catalog in Power Apps

At the time of this writing, you can create **Catalog** records in Power Apps (<https://make.powerapps.com>), but you cannot create **Catalog Assignment** records. Without catalog assignments, the catalog will not be functional. Catalog assignments can only be created using code at this time. See [Create Catalogs and CatalogAssignments with code](#create-catalogs-and-catalogassignments-with-code)

You should always create a catalog as part of a solution. Use the following instructions to create catalog records:

1. Sign in to [Power Apps](https://make.powerapps.com), 
1. In the left navigation pane, select **Solutions**.
1. Create or select a solution that you want to use, then click **New**.
1. Select **Catalog** from the menu and a new window will open.
1. Complete the form using information from [Catalog table columns](#catalog-table-columns).
1. Save and close the form.

> [!IMPORTANT]
> There is a known issue where the catalog will not be added to the solution. Until this is fixed, you must manually add the catalog to your solution.

### Add a catalog to your solution

1. While viewing your solution, click **Add existing**.
1. Select the catalog you want to add, and click **Add**.


## Create Catalogs and CatalogAssignments with code

You can create catalogs and catalog assignment records using either the Web API or the Organization Service.

### Using the Web API

> [!NOTE]
> At this time it is not possible to create catalog and catalog assignment records using 'deep-insert'. Each record must be created individually and associated with the records.

The following series of Web API operations will create a catalog hierarchy and a CatalogAssignment in a solution with the UniqueName: `ContosoCustomerManagement`. Note the use of the `MSCRM.SolutionUniqueName` request header to set the association to the solution when the record is created.

See the [Create a record using the Web API](webapi/create-entity-web-api.md) sections: [Basic Create](webapi/create-entity-web-api.md#basic-create) and [Associate table rows on create](webapi/create-entity-web-api.md#associate-table-rows-on-create) for more information.

#### Create the root catalog

**Request**

```http
POST [Organization URI]/api/data/v9.2/catalogs HTTP/1.1
MSCRM.SolutionUniqueName: ContosoCustomerManagement
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
{
    "name": "Contoso Customer Management",
    "uniquename": "contoso_CustomerManagement",
    "displayname": "Contoso Customer Management",
    "description": "The root catalog for the Contoso Customer Management solution",
    "iscustomizable": {
        "Value": false
    }
}

```

**Response**

```http
HTTP/1.1 204 No Content
OData-EntityId: [Organization URI]/api/data/v9.2/catalogs(00000000-0000-0000-0000-000000000001)

```

#### Create the Table Events Sub-catalog

**Request**

```http
POST [Organization URI]/api/data/v9.2/catalogs HTTP/1.1
MSCRM.SolutionUniqueName: ContosoCustomerManagement
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
{
    "name": "Contoso Customer Management Table Events",
    "uniquename": "contoso_TableEvents",
    "displayname": "Tables",
    "description": "Groups Table events for the Contoso Customer Management Solution",
    "iscustomizable": {
        "Value": false
    },
    "ParentCatalogId@odata.bind": "catalogs(00000000-0000-0000-0000-000000000001)"
}

```

**Response**

```http
HTTP/1.1 204 No Content
OData-EntityId: [Organization URI]/api/data/v9.2/catalogassignments(00000000-0000-0000-0000-000000000002)

```

#### Create the Account Catalog Assignment on the Tables catalog

See [Get the Id of a table](#get-the-id-of-a-table) for information about the id of a table.

**Request**

```http
POST {{webapiurl}}catalogassignments HTTP/1.1
MSCRM.SolutionUniqueName: ContosoCustomerManagement
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
{
    "name": "Account",
    "EntityId@odata.bind": "entities(70816501-edb9-4740-a16c-6a5efbc05d84)",
    "iscustomizable": {
        "Value": false
    },
    "CatalogId@odata.bind": "catalogs(00000000-0000-0000-0000-000000000002)"
}

```

**Response**

```http
HTTP/1.1 204 No Content
OData-EntityId: [Organization URI]/api/data/v9.2/catalogassignments(00000000-0000-0000-0000-000000000003)

```


### Using the Organization Service

The following code shows creating a catalog hierarchy and a catalog assignment in a solution with the UniqueName: `ContosoCustomerManagement`.

> [!NOTE]
> Use the `SolutionUniqueName` optional parameter with the  [CreateRequest Class](/dotnet/api/microsoft.xrm.sdk.messages.createrequest) to create the records in the context of that solution.
> More information: [Passing optional parameters with a request](/powerapps/developer/data-platform/org-service/use-messages#passing-optional-parameters-with-a-request)

```csharp
string conn = $@"
Url = {url};
AuthType = OAuth;
UserName = {userName};
Password = {password};
AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
LoginPrompt=Auto;
RequireNewInstance = True";

var service = new CrmServiceClient(conn);

var solutionUniqueName = " ContosoCustomerManagement ";

//Create the root catalog
Catalog rootCatalog = new Catalog
{
    Name = "Contoso Customer Management",
    UniqueName = "contoso_CustomerManagement",
    DisplayName = "Contoso Customer Management",
    Description = "The root catalog for the Contoso Customer Management solution",
    IsCustomizable = new BooleanManagedProperty(false)
};

CreateRequest rootCatalogReq = new CreateRequest {
    Target = rootCatalog
};
rootCatalogReq["SolutionUniqueName"] = solutionUniqueName;

Guid rootCatalogId = ((CreateResponse)service.Execute(rootCatalogReq)).id;

//Create the Table Events Sub-catalog
Catalog tableEvents = new Catalog
{
    Name = "Contoso Customer Management Table Events",
    UniqueName = "contoso_TableEvents",
    DisplayName = "Tables",
    Description = "Groups Table events for the Contoso Customer Management Solution",
    IsCustomizable = new BooleanManagedProperty(false),
    ParentCatalogId = new EntityReference("catalog", rootCatalogId)
};

CreateRequest tableEventsReq = new CreateRequest
{
    Target = tableEvents
};
tableEventsReq["SolutionUniqueName"] = solutionUniqueName;

Guid tableEventsId = ((CreateResponse)service.Execute(tableEventsReq)).id;

//Create the Account Catalog Assignment on the Tables catalog
CatalogAssignment accountAssignment = new CatalogAssignment
{
    Name = "Account",
    IsCustomizable = new BooleanManagedProperty(false),
    Object = new EntityReference("entity",new Guid("70816501-edb9-4740-a16c-6a5efbc05d84")),
    CatalogId = new EntityReference("catalog", tableEventsId)

};

CreateRequest accountAssignmentReq = new CreateRequest
{
    Target = accountAssignment
};
accountAssignmentReq["SolutionUniqueName"] = solutionUniqueName;

Guid accountAssignmentId = ((CreateResponse)service.Execute(accountAssignmentReq)).id;

```

## Create Catalog and Catalog Assignments by editing solution files

Within a solution file, you can edit the files to create catalogs and catalog assignments. 

Use the [SolutionPackager tool](/power-platform/alm/solution-packager-tool) to extract a solution into files that can be managed in source control. You can then edit the files. You can then use SolutionPackager to pack the extracted files back into a solution. More information: [Source control with solution files](/power-platform/alm/use-source-control-solution-files)

> [!TIP]
> Create some catalogs and catalog assignments with code in a solution, then export and extract the solution to see some examples.
>
> Make sure you are using the latest version of the [Microsoft.CrmSdk.CoreTools NuGet Package](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools)

### Create a Catalog with solution files

Within a solution, all the catalogs will be within a `catalogs` folder.

Each catalog will be included in a folder matching the uniquename of the catalog, such as `contoso_CustomerManagement`.

Within the folder is an XML file containing the definition of the catalog.

For example:

```xml
<catalog uniquename="contoso_CustomerManagement">
    <description default="The root catalog for the Contoso Customer Management solution">
        <label description="The root catalog for the Contoso Customer Management solution" languagecode="1033" />
    </description>
    <displayname default="Contoso Customer Management">
        <label description="Contoso Customer Management" languagecode="1033" />
    </displayname>
    <iscustomizable>0</iscustomizable>
    <name>Contoso Customer Management</name>
</catalog>
```

If the Catalog represents a category, the relationship to the parent catalog is included. 

For example:

```xml
<catalog uniquename="contoso_TableEvents">
    <description default="Groups Table events for the Contoso Customer Management Solution">
        <label description="Groups Table events for the Contoso Customer Management Solution" languagecode="1033" />
    </description>
    <displayname default="Tables">
        <label description="Tables" languagecode="1033" />
    </displayname>
    <iscustomizable>0</iscustomizable>
    <name>Contoso Customer Management Table Events</name>
    <parentcatalogid>
        <uniquename>contoso_CustomerManagement</uniquename>
    </parentcatalogid>
</catalog>
```

### Create a CatalogAssignment with solution files

Within a solution, in the `Assets` folder, you will find a `catalogassignements.xml` file. All catalog assignments are included in the file.

For example:

```xml
<catalogassignments>
    <catalogassignment objectidtype="entity" object.logicalname="account" catalogid.uniquename="contoso_TableEvents">
        <iscustomizable>0</iscustomizable>
        <name>Account</name>
    </catalogassignment>
</catalogassignments>
```

### See also  

[Microsoft Dataverse business events (preview)](business-events.md)<br />
[Create an entity record using the Web API](webapi/create-entity-web-api.md)<br />
[Retrieve an entity record using the Web API](webapi/retrieve-entity-using-web-api.md)<br />
[Create entities using the Organization Service](org-service/entity-operations-create.md)<br />
[Retrieve an entity using the Organization Service](org-service/entity-operations-retrieve.md)
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
