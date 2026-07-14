---
title: link-entity element
description: Use this element to join tables with the containing entity or link-entity element.
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.date: 02/29/2024
ms.topic: reference
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# link-entity element

[!INCLUDE [link-entity-description](includes/link-entity-description.md)]

[Learn how to join tables using FetchXml](../join-tables.md).

## Examples

The following examples show using `link-entity` with different types of relationships.

### Many-to-one relationship

This query returns data from the [account](../../reference/entities/account.md) and [contact](../../reference/entities/contact.md) tables based on the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) in the account record:

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <link-entity name='contact'
      from='contactid'
      to='primarycontactid'
      link-type='inner'
      alias='contact'>
      <attribute name='fullname' />
    </link-entity>
  </entity>
</fetch>
```

### One-to-many relationship

This query returns data from the [contact](../../reference/entities/contact.md) and [account](../../reference/entities/account.md) tables based on the [Contact account_primary_contact one-to-many relationship](../../reference/entities/contact.md#BKMK_account_primary_contact).

```xml
<fetch>
  <entity name='contact'>
    <attribute name='fullname' />
    <link-entity name='account' 
     from='primarycontactid' 
     to='contactid' 
     alias='account'>
      <attribute name='name' />
    </link-entity>
  </entity>
</fetch>
```

### Many-to-many relationship

This query returns data from the [SystemUser](../../reference/entities/systemuser.md) and [Team](../../reference/entities/team.md) tables using the [teammembership_association many-to-many relationship](../../reference/entities/team.md#BKMK_teammembership_association).

```xml
<fetch>
  <entity name='systemuser'>
    <attribute name='fullname' />
    <link-entity name='teammembership'
      from='systemuserid'
      to='systemuserid' >
      <link-entity name='team'
        from='teamid'
        to='teamid'
        link-type='inner'
        alias='team'>
        <attribute name='name' />
      </link-entity>
    </link-entity>
  </entity>
</fetch>
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`name`|Yes|[!INCLUDE [link-entity-name-description](includes/link-entity-name-description.md)]|
|`to`|No|[!INCLUDE [link-entity-to-description](includes/link-entity-to-description.md)] [While not technically required, this attribute is usually used.](#using-from-and-to-attributes)|
|`from`|No|[!INCLUDE [link-entity-name-from-description](includes/link-entity-from-description.md)] [While not technically required, this attribute is usually used.](#using-from-and-to-attributes)|
|`alias`|No|[!INCLUDE [link-entity-name-alias-description](includes/link-entity-alias-description.md)]|
|`link-type`|No|[!INCLUDE [link-entity-name-link-type-description](includes/link-entity-link-type-description.md)]|
|`intersect`|No|[!INCLUDE [link-entity-name-intersect-description](includes/link-entity-intersect-description.md)]|

### Using `from` and `to` attributes

It's best to set values for both the  `from` and `to`  attributes. Both of these attributes are usually used to explicitly define the columns to match. However, the `from` and `to`  attributes aren't technically required.

> [!NOTE]
> - It is important that the columns specified in the `from` and `to`   attributes are the same type. Using different column types is not supported. When the columns are not the same type, the Dataverse infrastructure may be able to force a conversion but this practice can result in a significant performance penalty.
> 
> - The meaning of the `from` and `to`  attributes in FetchXml are the opposite of the corresponding [LinkEntity.LinkFromAttributeName](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromAttributeName) and [LinkEntity.LinkToAttributeName](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToAttributeName) properties used when [composing queries using QueryExpression](../../org-service/queryexpression/overview.md).

If you don't use either of these attributes, and a system many-to-many relationship exists between the two tables, Dataverse selects the appropriate key values using that relationship.

If you specify only one of the `from` or `to` attributes, Dataverse attempts to figure out the correct relationship using the relationship schema definitions between the two tables.

Otherwise you'll get the following error:

> Code: `0x80041102`  
> Message: `No system many-to-many relationship exists between <table A> and <table B>.  If attempting to link through a custom many-to-many relationship ensure that you provide the from and to attributes.`

For example, both of these queries use the [teammembership_association](../../reference/entities/team.md#BKMK_teammembership_association) many-to-many relationship between [systemuser](../../reference/entities/systemuser.md) and [team](../../reference/entities/team.md) tables. In this case, Dataverse can work out the `from` and `to` attributes and the `link-entity` that specifies the intersect table isn't necessary.

<!-- Unfortunately the formatting of this XML is lost in the column layout -->

:::row:::
   :::column span="":::
      **Specify all attributes**
      ```xml
      <fetch top="2">
         <entity name="systemuser">
            <attribute name="fullname" />
            <link-entity
               name="teammembership"
               from="systemuserid"
               to="systemuserid"
               intersect="true"
            >
               <link-entity
               name="team"
               from="teamid"
               to="teamid"
               link-type="inner"
               alias="team"
               >
               <attribute name="name" />
               </link-entity>
            </link-entity>
         </entity>
      </fetch>
      ```
   :::column-end:::
   :::column span="":::
      **Let Dataverse choose**
      ```xml
      <fetch top="2">
         <entity name="systemuser">
            <attribute name="fullname" />
            <link-entity name="team" alias="team">
               <attribute name="name" />
            </link-entity>
         </entity>
      </fetch>
      ```
   :::column-end:::
:::row-end:::


### link-type options

Use `link-type` to apply filters on the records returned. The following table describes the valid `link-type` values:

|Name|Description|
|---------|---------|
|`inner`|Default. Restricts results to rows with matching values in both tables.|
|`outer`|Includes results from the parent element that don't have a matching value.|
|`any`|[!INCLUDE [link-type-any-description](includes/link-type-any-description.md)] [Learn to use `any` to filter values on related tables](../filter-rows.md#filter-on-values-in-related-records)|
|`not any`|[!INCLUDE [link-type-not-any-description](includes/link-type-not-any-description.md)] [Learn to use `not any` to filter values on related tables](../filter-rows.md#filter-on-values-in-related-records)|
|`all`|[!INCLUDE [link-type-all-description](includes/link-type-all-description.md)] [Learn to use `all` to filter values on related tables](../filter-rows.md#filter-on-values-in-related-records)|
|`not all`|[!INCLUDE [link-type-not-all-description](includes/link-type-not-all-description.md)] [Learn to use `not all` to filter values on related tables](../filter-rows.md#filter-on-values-in-related-records)|
|`exists`|[!INCLUDE [link-type-exists-description](includes/link-type-exists-description.md)]|
|`in`|[!INCLUDE [link-type-in-description](includes/link-type-in-description.md)]|
|`matchfirstrowusingcrossapply`|[!INCLUDE [link-type-matchfirstrowusingcrossapply-description](includes/link-type-matchfirstrowusingcrossapply-description.md)]|


## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|Joins a table related to the [entity](entity.md) or [link-entity](link-entity.md) to return more columns with the result.|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[all-attributes](all-attributes.md)|0 or 1|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute](attribute.md)|0 or many|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[order](order.md)|0 or many|[!INCLUDE [order-description](includes/order-description.md)]|
|[link-entity](link-entity.md)|0 or many|Joins a table related to the [entity](entity.md) or [link-entity](link-entity.md) to return more columns with the result.|
|[filter](filter.md)|0 or 1|[!INCLUDE [filter-description](includes/filter-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
