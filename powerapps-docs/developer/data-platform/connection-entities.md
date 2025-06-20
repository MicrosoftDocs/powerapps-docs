---
title: "Use connections to link records to each other (Microsoft Dataverse) | Microsoft Docs" 
description: "Connection tables help you enable, create, and query connections." 
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"

ms.topic: "article"
author: "mayadumesh" 
ms.subservice: dataverse-developer
ms.author: "jdaly"
search.audienceType: 
  - developer
---
# Use connections to link records to each other



The *connections* provide a flexible way to connect and describe the relationships between any two records in Microsoft Dataverse. It helps you to promote teamwork, collaboration, and effective management of business and sales processes. Connections enable you to easily associate users, contacts, quotes, sales orders, and many other  records with each other. The records in the association can be assigned particular roles that help define the purpose of the relationship.  
  
 Connections provide the following capabilities:  
  
- An easy and flexible way to make a connection between two records of most Dataverse table types. All customizable business and custom tables can be enabled for connections.  
  
- An option to add useful information, such as a description of the connection and the duration.  
  
- The ability to create connection roles that describe the relationship between two records, such as a relationship between a doctor and a patient, or a manager and an employee.  
  
- A quick way to create multiple connections and roles for a particular record. For example, a contact may have many relationships with other contacts, accounts, or contracts. In each relationship a contact may play a different role.  
  
- Information for building queries and creating graphs. You can search for all connections and connection roles for a particular record and create graphs and charts for visual representation of the connections.  
  
- Support for workflows and auditing for automating and improving business processes.  
  
## Enabling and creating connections  
 You can enable any custom or customizable table for connection by updating the table definitions. Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> message to set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsConnectionsEnabled> property to `true`.  
  
 To create a connection between two records, use the `Connection` table. You must specify a record from which you create a connection (source) and a record to which you connect (target). Use the `Connection.Record1Id` column to specify the source record and the `Connection.Record2Id` column to specify the target record. Optionally, you can specify the duration of the connection and the description. To describe the relationship between the participants in the connection, use the connection roles. To specify the connection roles, use the `Connection.Record1RoleId` column and the `Connection.Record2RoleId` column.  
  
## Querying connections  
 Querying connections gives you valuable data that you can use to create reports, graphs, or charts. You can query connections by record, by type (Entity Type Code), by a particular role, or other criteria. The following are examples of how you can query connections:  
  
 By record:  
  
- Show all connections for account A.  
  
- Show all roles for account A.  
  
  By type (using Entity Type Codes):  
  
- Show all roles for the competitor.  
  
- Find the total number of roles for the account.  
  
  By a role:  
  
- Find all connections where account A is a “Vendor”.  
  
- Find all open opportunities over $20,000, where contact B is a “Salesperson”.  
  
- Find all matching roles for a “Doctor” role, such as “Patient”, “Nurse”, or “Medical Assistant”.  
  
- Find all contacts that have the role “Friend”.  
  
> [!IMPORTANT]
>  When you create a connection record, two records are created in the database. The first record represents a source to target connection and the second record represents a target to source connection. This guarantees that a query will find all connections that the record participates in, regardless whether the record is a source record or a target record in the connection.  
  
### See also  
 [Describe a relationship between tables with connection roles](describe-relationship-entities-connection-roles.md)   
 [Connection table](reference/entities/connection.md)   
 [ConnectionRole table](reference/entities/connectionrole.md)   
 [Sample Code for connection tables](/dynamics365/customer-engagement/developer/sample-code-connection-entities)   
 [Business Management tables](/dynamics365/customer-engagement/developer/business-management-entities)   
 [View and Analyze Data with Visualizations and Dashboards in Dynamics 365](/dynamics365/customer-engagement/developer/customize-dev/customize-visualizations-dashboards)   
 [Fiscal Calendar and Territory tables](/dynamics365/customer-engagement/developer/fiscal-calendar-and-territory-entities)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
