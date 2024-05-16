---
title: "Customer tables (account, contact, customeraddress) (Microsoft Dataverse) | Microsoft Docs"
description: "The account and contact tables are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A customer address table is used to store address and shipping information for a customer."
ms.date: 05/15/2024
ms.reviewer: jdaly
ms.topic: article
author: mkannapiran
ms.subservice: dataverse-developer
ms.author: kamanick
search.audienceType:
  - developer
---

# Customer tables (account, contact, customeraddress)

The [account](reference/entities/account.md) and [contact](reference/entities/contact.md) tables are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. The [customer address](reference/entities/customeraddress.md) table stores address and shipping information for a customer.

## Account table

The account table is one of the tables in Dataverse to which most other tables are attached or parented. In Dataverse, an account represents a company with which the business unit has a relationship. Information that is included in an account is all relevant contact information, company information, category, relationship type, and address information. Other information that applies includes the following items:

- An account can be a parent to most table types, including another account.
- An account can be a standalone table.
- An account can have only one account as its parent.
- Accounts can have multiple child accounts and child contacts.

Account management is one of the important concepts of business-to-business customer relationship management (Dynamics 365) because an organization wants to see all the activities they have with another company. All these activities come together at the account level.

[View the Account table reference](reference/entities/account.md).

## Contact table

In Dataverse, a contact represents a person, usually an individual, with whom a business unit has a relationship, such as a customer, a supplier, or a colleague. The contact table is one of the tables that most other tables are linked to. A contact can be a stand-alone table. Included in this table are professional, personal, and family information, and multiple addresses.

[View the Contact table reference](reference/entities/contact.md).

Both accounts and contacts are part of managing customers and are related to one another in the following ways:

- A contact can be a parent to every other table except accounts and contacts.
- A contact can have only one account as its parent.
- A contact can be marked as the primary contact person for an account setting the [Account.PrimaryContactId](reference/entities/account.md#BKMK_PrimaryContactId) column.

The contact table stores all information about a person such as an email address, street address, telephone numbers, and other related information, such as the birthday or anniversary date. Depending on the type of customers a business unit has, it needs either only contacts, or contacts and accounts, to give a full view of its customers.

Linking tables such as activities and notes to the `contact` table lets user see all the communication the user has had with a customer, any actions the user has taken on behalf of the customer, and all information the user needs about the customer.

## CustomerAddress table

This table contains additional address and shipping information for customer records (account and contact). By default, Dataverse creates two `customeraddress` records in this table when a new customer record is created, even when there is no data for these records. [Learn how you can change this behavior](#disable-empty-record-creation)

All `customeraddress` records related to account and contact records are available via the [Account_CustomerAddress](reference/entities/account.md#BKMK_Account_CustomerAddress) and [Contact_CustomerAddress](reference/entities/contact.md#BKMK_Contact_CustomerAddress) relationships respectively. These relationships both use the [parentid](reference/entities/customeraddress.md#BKMK_ParentId) lookup, and the [parentidtypecode](reference/entities/customeraddress.md#BKMK_ParentIdTypeCode) column will tell you the type of customer record the address is related to.

### Address data embedded with customer records

You can retrieve or modify the data for the two embedded `customeraddress` records with the customer record. Both `account` and `contact` tables have columns `address1_addressid` and `address2_addressid` which store `customeraddressid` values, and there are other customer columns each prefixed with either `address1*` or `address2*` that contain the corresponding address information from the `customeraddress` table.

The `customeraddress` [addressnumber](reference/entities/customeraddress.md#BKMK_AddressNumber) column tells you which address applies to the parent customer record columns. You can't set the `addressnumber` column to a value used by another `customeraddress` record related to the same parent customer, but you can set an existing `addressnumber` value to null, and then change the value of another record if you want to swap the relative position of the records for the customer records. Other than controlling the respective address position in the customer record (either `1` or `2`), the `addressnumber` column value isn't used for any other purpose and is usually null.

Dataverse will only update these `customeraddress` records through the corresponding customer record columns instead of updating the `customeraddress` rows directly. However, anyone can edit these records as `customeraddress` records, or add additional `customeraddress` records associated with the `account` or `contact` record that are not embedded with the account and contact records.

#### Deletion of embedded customer address rows isn't allowed

By default, if you attempt to delete one of the two embedded `customeraddress` records that are referenced in the `address1_addressid` or `address2_addressid` for an customer record, you will get an error like the following:

> Name: `CannotDeleteDueToAssociation`<br />
> Code: `0x80040227`<br />
> Number: `-2147220953`<br />
> Message: `Customer Address can not be deleted because it is associated with another object. Address Id = 4f33c2e4-d5a3-4b03-b050-21984c0e4c15, AddressNumber=2, ParentId=4b757ff7-9c85-ee11-8179-000d3a9933c9, ObjectTypeCode=1`

[Learn how you can change this behavior](#delete-embedded-address-records)

### Disable Empty Record Creation

Because each row in the `customeraddress` table counts against the Dataverse capacity you pay for, you may want to minimize this cost.

You can tell Dataverse not to create empty `customeraddress` table rows for each customer record by changing a the **Disable empty address record creation** setting in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/). [Learn more about this setting](/power-platform/admin/settings-features#disable-empty-address-record-creation)

> [!NOTE]
> Before changing this behavior, you should consider whether you have existing customizations that depend on default behavior.

While this setting is on, no new empty `customeraddress` table rows will be created when new customer records are created. Records are only created only if the incoming payload contains address data. If this setting is switched off, the default behavior resumes. Turning this setting on doesn't delete any existing `customeraddress` table rows. Switching this setting back on after it was switched off will not re-create records that would have been created.

#### Detect whether empty address record creation is disabled

These example functions show how to detect whether the **Disable empty address record creation** setting is enabled in the environment.

##### [SDK for .NET](#tab/sdk)

This static `IsEmptyAddressRecordCreationDisabled` method uses the [WhoAmIRequest class](/dotnet/api/microsoft.crm.sdk.messages.whoamirequest) and the [IOrganizationService.Retrieve method](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrieve) to check a value in the [Organization.OrgDbOrgSettings column](reference/entities/organization.md#BKMK_OrgDbOrgSettings)

```csharp
static bool IsEmptyAddressRecordCreationDisabled(IOrganizationService service)
{

   Guid orgId = ((WhoAmIResponse)service
         .Execute(new WhoAmIRequest())).OrganizationId;

   Entity organization = service
         .Retrieve("organization", orgId, new ColumnSet("orgdborgsettings"));

   XDocument orgdborgsettings = XDocument
         .Parse((string)organization["orgdborgsettings"]);

   XElement? element = orgdborgsettings
         .XPathSelectElement("//CreateOnlyNonEmptyAddressRecordsForEligibleEntities");

   // Return true only when the element exists and has the value of 'true'
   return element != null && element.Value == "true";
}
```

- [Use the SDK for .NET](org-service/overview.md)
- [WhoAmIRequest Class](/dotnet/api/microsoft.crm.sdk.messages.whoamirequest)
- [Retrieve a table row using the SDK for .NET](org-service/entity-operations-retrieve.md)
- [Organization.OrgDbOrgSettings column](reference/entities/organization.md#BKMK_OrgDbOrgSettings)

##### [Web API](#tab/webapi)

This `Test-IsEmptyAddressRecordCreationDisabled` PowerShell function uses the example `Get-WhoAmI` and `Get-Record` functions described in [Create reusable functions](webapi/use-ps-and-vscode-web-api.md#create-reusable-functions) and depend on global variables set in the [Connect function](webapi/use-ps-and-vscode-web-api.md#create-a-connect-function)

```powershell
function Test-IsEmptyAddressRecordCreationDisabled {

   $orgId = Get-WhoAmI | Select-Object -ExpandProperty OrganizationId

   $orgdborgsettings = Get-Record `
      -setName 'organizations' `
      -id $orgId `
      -query "?`$select=orgdborgsettings"
   | Select-Object `
      -ExpandProperty orgdborgsettings

   $xml = [xml]$orgdborgsettings

   $element = $xml.SelectSingleNode("//CreateOnlyNonEmptyAddressRecordsForEligibleEntities")

   # Return true only when the element exists and has the value of 'true'
   return ($null -ne $element) -and ($element.InnerText -eq 'true')
}
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)
- [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI)
- [Organization entitytype](xref:Microsoft.Dynamics.CRM.organization)

---

### Delete embedded address records

By default, you can't delete embedded `customeraddress` table rows that are referenced by the `address1_addressid` and `address2_addressid` columns in customer tables. See [Deletion of embedded customer address rows isn't allowed](#deletion-of-embedded-customer-address-rows-isnt-allowed)

You can change this with the **Enable Deletion of Address Records** setting in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/). [Learn more about this setting](/power-platform/admin/settings-features#enable-deletion-of-address-records)

#### Detect whether deletion of address records is enabled

These example functions show how to detect whether the **Enable Deletion of Address Records** setting is enabled in the environment with code.

##### [SDK for .NET](#tab/sdk)

This static `IsDeleteAddressRecordsEnabled` method uses the [WhoAmIRequest class](/dotnet/api/microsoft.crm.sdk.messages.whoamirequest) and the [IOrganizationService.Retrieve method](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrieve) to check a value in the [Organization.OrgDbOrgSettings column](reference/entities/organization.md#BKMK_OrgDbOrgSettings)

```csharp
static bool IsDeleteAddressRecordsEnabled(IOrganizationService service)
{

   Guid orgId = ((WhoAmIResponse)service
         .Execute(new WhoAmIRequest())).OrganizationId;

   Entity organization = service
         .Retrieve("organization", orgId, new ColumnSet("orgdborgsettings"));

   XDocument orgdborgsettings = XDocument
         .Parse((string)organization["orgdborgsettings"]);

   XElement? element = orgdborgsettings
         .XPathSelectElement("//EnableDeleteAddressRecords");

   // Return true only when the element exists and has the value of 'true'
   return element != null && element.Value == "true";

}
```

##### [Web API](#tab/webapi)

This `Test-IsDeleteAddressRecordsEnabled` PowerShell function uses the example `Get-WhoAmI` and `Get-Record` functions described in [Create reusable functions](webapi/use-ps-and-vscode-web-api.md#create-reusable-functions) and depend on global variables set in the [Connect function](webapi/use-ps-and-vscode-web-api.md#create-a-connect-function)

```powershell
function Test-IsDeleteAddressRecordsEnabled {

   $orgId = Get-WhoAmI | Select-Object -ExpandProperty OrganizationId

   $orgdborgsettings = Get-Record `
      -setName 'organizations' `
      -id $orgId `
      -query "?`$select=orgdborgsettings"
   | Select-Object `
      -ExpandProperty orgdborgsettings

   $xml = [xml]$orgdborgsettings

   $element = $xml.SelectSingleNode("//EnableDeleteAddressRecords")

   # Return true only when the element exists and has the value of 'true'
   return ($null -ne $element) -and ($element.InnerText -eq 'true')
}
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)
- [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI)
- [Organization entitytype](xref:Microsoft.Dynamics.CRM.organization)

---

### Bulk delete of empty customer address records

After you have disabled empty address record creation and enabled deletion of address records, you can use the following example functions to asynchronously delete empty `customeraddress` records using the `BulkDelete` message.

##### [SDK for .NET](#tab/sdk)

The static `BulkDeleteEmptyCustomerAddressRecords` method creates a system job to delete empty `customeradddress` records using the [BulkDeleteRequest class](/dotnet/api/microsoft.crm.sdk.messages.bulkdeleterequest). 

This method uses the example `IsDeleteAddressRecordsEnabled` and `IsEmptyAddressRecordCreationDisabled` static methods described in [Detect whether deletion of address records is enabled](#detect-whether-deletion-of-address-records-is-enabled) and [Detect whether empty address record creation is disabled](#detect-whether-empty-address-record-creation-is-disabled) respectively to ensure these settings are configured to allow deletion of all the empty customer address records and ensure no new ones are created.

```csharp
/// <summary>
/// Create a Bulk Delete job to delete empty customer address records
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance.</param>
/// <returns>The Id of the system job</returns>
/// <exception cref="Exception"></exception>
static Guid BulkDeleteEmptyCustomerAddressRecords(IOrganizationService service)
{
    if (!IsDeleteAddressRecordsEnabled(service))
    {

        throw new Exception("Enable deletion of address records" +
            " before running this method.");
    }

    if (!IsEmptyAddressRecordCreationDisabled(service))
    {

        throw new Exception("Disable empty address record creation" +
            " before running this method.");
    }

    var query = new QueryExpression("customeraddress")
    {

        ColumnSet = new ColumnSet("customeraddressid"),
        Criteria =
        {
            Conditions =
            {
                new ConditionExpression("city", ConditionOperator.Null),
                new ConditionExpression("country", ConditionOperator.Null),
                new ConditionExpression("county", ConditionOperator.Null),
                new ConditionExpression("fax", ConditionOperator.Null),
                new ConditionExpression("freighttermscode", ConditionOperator.Null),
                new ConditionExpression("latitude", ConditionOperator.Null),
                new ConditionExpression("line1", ConditionOperator.Null),
                new ConditionExpression("line2", ConditionOperator.Null),
                new ConditionExpression("line3", ConditionOperator.Null),
                new ConditionExpression("longitude", ConditionOperator.Null),
                new ConditionExpression("postalcode", ConditionOperator.Null),
                new ConditionExpression("postofficebox", ConditionOperator.Null),
                new ConditionExpression("primarycontactname", ConditionOperator.Null),
                new ConditionExpression("shippingmethodcode", ConditionOperator.Null),
                new ConditionExpression("stateorprovince", ConditionOperator.Null),
                new ConditionExpression("telephone1", ConditionOperator.Null),
                new ConditionExpression("telephone2", ConditionOperator.Null),
                new ConditionExpression("telephone3", ConditionOperator.Null),
                new ConditionExpression("upszone", ConditionOperator.Null),
                new ConditionExpression("utcoffset", ConditionOperator.Null)
            }
        }
    };

    BulkDeleteRequest request = new()
    {
        QuerySet = new QueryExpression[] { query },
        StartDateTime = DateTime.UtcNow,
        RecurrencePattern = string.Empty,
        SendEmailNotification = false,
        JobName = "Delete empty customer address records",
        ToRecipients = new List<Guid>().ToArray(),
        CCRecipients = new List<Guid>().ToArray()

    };

    var response = (BulkDeleteResponse)service.Execute(request);
    return response.JobId;

}
```

- [Use the SDK for .NET](org-service/overview.md)
- [BulkDeleteRequest class](/dotnet/api/microsoft.crm.sdk.messages.bulkdeleterequest)
- [Delete data in bulk](delete-data-bulk.md)

##### [Web API](#tab/webapi)

```powershell
TODO
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)
- [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete)
- [Delete data in bulk](delete-data-bulk.md)

---

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
