---
title: What is Microsoft Dataverse? | Microsoft Docs
description: Introduction to Microsoft Dataverse, tables, server-side logic, security, and developer capabilities.
author: mattp123
manager: kvivek
ms.service: powerapps
ms.topic: overview
ms.component: cds
ms.custom: intro-internal
ms.date: 11/10/2020
ms.reviewer: matp
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - "Power Apps"
---

# What is Microsoft Dataverse?
[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Dataverse lets you securely store and manage data that's used by business applications. Data within Dataverse is stored within a set of tables. A *table* is a set of rows (formerly referred to as records) and columns (formerly referred to as fields/attributes). Each column in the table is designed to store a certain type of data, for example, name, age, salary, and so on. Dataverse includes a base set of standard tables that cover typical scenarios, but you can also create custom tables specific to your organization and populate them with data by using Power Query. App makers can then use Power Apps to build rich applications that use this data.

![Diagram showing overview of Microsoft Power Platform.](./media/data-platform-cds-intro/platform.png "Dataverse in Microsoft Power Platform")

For information about purchasing a plan to use Dataverse, go to [Pricing info](/power-platform/admin/pricing-billing-skus).

## Why use Dataverse?
Standard and custom tables within Dataverse provide a secure and cloud-based storage option for your data. Tables let you create a business-focused definition of your organization's data for use within apps. If you're not sure whether tables are your best option, consider these benefits:

- **Easy to manage** &ndash; Both the metadata and data are stored in the cloud. You don't need to worry about the details of how they're stored.
- **Easy to secure** &ndash; Data is securely stored so that users can see it only if you grant them access. Role-based security allows you to control access to tables for different users within your organization.
- **Access your Dynamics 365 Data** &ndash; Data from your Dynamics 365 applications is also stored within Dataverse, allowing you to quickly build apps that use your Dynamics 365 data and extend your apps with Power Apps.
- **Rich metadata** &ndash; Data types and relationships are used directly within Power Apps.
- **Logic and validation** &ndash; Define calculated columns, business rules, workflows, and business process flows to ensure data quality and drive business processes.
- **Productivity tools** &ndash; Tables are available within the add-ins for Microsoft Excel to increase productivity and ensure data accessibility.

More information: [Why choose Dataverse?](why-dataverse-overview.md)

## Terminology updates

Responding to customer feedback and data from user research, effective November 2020 we're updating some terminology in Dataverse to be more intuitive and make its usage more productive. The terminology updates are listed below, and we're in the process of rolling them out across Microsoft Power Platform.

|Legacy term |Current term |
|--|--|
|Entity, entities	|Table, tables|
|Field, fields<br/>Attribute, attributes|Column, columns|
|Record, records|	Row, rows|
|Option set, multi select option sets<br/>Picklist, picklists|	Choice, choices |
| Two Options|	Yes/No|

> [!NOTE]
> These terminology updates aren’t applicable to any APIs or messages in the Dataverse web services. For example, the names of the messages <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> and <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> won't change. 


## Dynamics 365 and Dataverse

Dynamics 365 applications&mdash;such as Dynamics 365 Sales, Dynamics 365 Customer Service, or Dynamics 365 Talent&mdash;also use Dataverse to store and secure the data they use. This enables you to build apps by using Power Apps and Dataverse directly against your core business data, which is already used within Dynamics 365, without the need for integration.

- **Build apps against your Dynamics 365 data** &ndash; Build apps quickly against your business data within Power Apps or by using the extensible platform that lets pro developers programmatically interact with data and metadata, apply business logic, create custom connectors, and integrate with external data.

- **Manage reusable business logic and rules** &ndash; Business rules and logic already defined in your Dataverse tables are applied to apps created with Power Apps to ensure data consistency, regardless of how your users access the data or which app they use.

- **Reusable skills across Dynamics 365 and Power Apps** &ndash; Users who are skilled in Power Apps or Dynamics 365 can now take advantage of those skills across the Dataverse platform. Creating tables, forms, and charts are now common tasks you perform across your applications.

    > [!NOTE]
    > Finance and Operations apps currently require the configuration of the [Data Integrator](/power-platform/admin/data-integrator) to make your business data from Finance and Operations apps available in Dataverse.

## Integrating data into Dataverse

Building an app typically involves data from more than one source. Although this can sometimes be done at the application level, there are cases where integrating this data into a common store allows for an easier app-building experience and a single set of logic to maintain and operate over the data. Dataverse allows data to be integrated from multiple sources into a single store, which can then be used in Power Apps, Power Automate, Power BI, and Power Virtual Agents along with data that's already available from the Dynamics 365 applications.

* **Scheduled integration with other systems** &ndash; Data that's kept within another application can be regularly synchronized with Dataverse to allow you to take advantage of data from other applications in Power Apps.
* **Transform and import data using Power Query** &ndash; Transforming data when importing into Dataverse can be done through Power Query&mdash;a tool commonly used across Excel and Power BI&mdash;from many online data sources.
* **One-time import of data** &ndash; Simple import and export of Excel and CSV files can be used for a one-time (or infrequent) import of data into Dataverse.

For more information about integrating data into the Dataverse, go to [Add data to a table in Dataverse by using Power Query](add-data-power-query.md).

## Interacting with tables
When you develop an app, you can use standard tables, custom tables, or both. Dataverse provides standard tables by default. These are designed, in accordance with best practices, to capture the most common concepts and scenarios within an organization.

For a full list of tables, see the [entity reference](../../developer/data-platform/reference/about-entity-reference.md).

You can extend the functionality of standard tables by creating one or more custom tables to store information that's unique to your organization. More information: [How to create a custom table](create-custom-entity.md)

## Logic and validation
Tables within Dataverse can take advantage of rich server-side logic and validation to ensure data quality and reduce repetitive code in each app that creates and uses data within a table.

- **Business rules** validate data across multiple columns and tables, and provide warning and error messages, regardless of the app used to create the data. More information: [Create a business rule](./data-platform-create-business-rule.md)

- **Business process flows** guide users to ensure they enter data consistently and follow the same steps every time. Business process flows are currently only supported for model-driven apps. More information: [Business process flows overview](/power-automate/business-process-flows-overview)

- **Workflows** allow you to automate business processes without user interaction. More information: [Workflows overview](./overview-realtime-workflows.md)

- **Business logic with code** supports advanced developer scenarios to extend the application directly through code. More information: [Apply business logic with code](../../developer/data-platform/apply-business-logic-with-code.md)

## Security
Dataverse has a rich security model to protect the data integrity and privacy of users while promoting efficient data access and collaboration. You can combine business units, role-based security, row-based security, and column-based security to define the overall access to information that users have in a Dataverse environment. More information: [Security in Dataverse](/power-platform/admin/wp-security) in the Power Platform admin guide 

## Developer capabilities
In addition to the features available through the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) portal, Dataverse includes features for developers to programmatically access metadata and data to create tables and business logic, in addition to interacting with data. More information: [Dataverse Developer Overview](../../developer/data-platform/overview.md)

## Next steps
To get started using Dataverse:
- [Create a canvas app using a Dataverse database](../canvas-apps/data-platform-create-app-scratch.md).
- [Create a custom table](create-custom-entity.md) and then [create a canvas app that uses the table](../canvas-apps/data-platform-create-app.md).
- [Create a model-driven app](../model-driven-apps/build-first-model-driven-app.md) built on Dataverse.
- [Use Power Query](./add-data-power-query.md) to connect to an online or on-premises data source and import the data directly into Dataverse.

## Privacy notice
With the Microsoft Power Apps common data model, Microsoft collects and stores custom table and column names in our diagnostic systems. We use this knowledge to improve the common data model for our customers. The table and column names that app Creators create help us understand scenarios that are common across the Microsoft Power Apps community and ascertain gaps in the service's standard table coverage, such as schemas related to organizations. The data in the database tables associated with these tables is not accessed or used by Microsoft or replicated outside of the region in which the database is provisioned. Note, however, that the custom table and column names may be replicated across regions and are deleted in accordance with our data retention policies. Microsoft is committed to your privacy as described further in our [Trust Center](https://www.microsoft.com/trustcenter/Privacy/default.aspx).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]