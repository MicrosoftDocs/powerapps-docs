---
title: Data design - Working with enterprise systems | Microsoft Docs
description: Read this article to understand some of the things to consider when integrating with enterprise systems for a Power Apps project.
author: taiki-yoshida
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.author: tayoshi
ms.reviewer: kathyos

---

# Working with enterprise systems

When you need to work and integrate with existing enterprise systems such as
SAP and Oracle, you should seek cooperation and support from
your IT administration team or the team in charge of the system.

Even if you aren't in a technical role, read this section to understand some of
the things that typically need to be taken into consideration when integrating
with enterprise systems.

## Frequency and time of data integration

When integrating with other systems, you need to consider the frequency of
integration and take time zones into account if the integration has use cases that cross time zones.
The frequency of integration will depend on two aspects: data volume and the
time-related requirements of the business.

## Method of integrating with enterprise systems

There are several ways of integrating with enterprise systems:

- **Database** integration is a direct integration with a database. This is
    not a very common way of integrating with external systems,
    because there's a risk of exposing data.

- **API** integration is a method of
    integrating with systems by using APIs. The majority of web systems provide APIs to integrate with, but some don't.

- **File** integration is a method of integrating with other systems by using
    files. One system exports a data file. This file might be in CSV,
    TSV, XML, or another format. The system it's integrating to then either detects that there's a new
    file, or is set up with a timer to periodically scan to check whether new files exist and then
    import the file that was exported. This method is used in situations where
    the data source can't be accessed directly via database or APIs.

## Connecting to on-premises systems

An on-premises data gateway allows apps and services to connect to systems
that aren't open to the internet in a secure manner. Setting up is easy using
an installer, but there are several factors to consider:

- Network bandwidth of the datacenter or server location

- Database tuning of the data source

- Server specification of on-premises systems

- Volume and frequency of data transmission

### Network bandwidth of the datacenter or server location

The speed of the app will depend on whether the network bandwidth between the
on-premises datacenter or server and the cloud service is sufficient. If
many people use the app simultaneously, not having enough bandwidth will cause
the app to take a long time to respond. More information:[Web application requirements](/power-platform/admin/web-application-requirements)

To find out the network speed of your organization, use the [Network Speed Test](https://www.microsoft.com/p/network-speed-test/9wzdncrfhx52)
from Microsoft Store (free of charge) and also [diagnostic tools](/power-platform/admin/verify-network-capacity-throughput-clients)
specifically for model-driven apps.

### Database tuning of the data source

Database tuning also plays an important role, especially if you're going to
connect to a data source that includes lots of data. It's easy to run into problems
if you've created an app that uses data in a way that it wasn't used before.

For example, suppose your existing customer management system is optimized to
search by using a first name, last name, and email address, but you made a new
app that searches by using phone number. The data won't have been indexed to help your app search efficiently.

Indexing helps your apps speed up searches, and when an index is missing
it takes longer to search and query for data. You might need to contact the IT
team for the data source to discuss how you'll access the data and add
additional indexes. For more information about indexing with SQL Server, see [SQL Server Index Architecture and Design Guide](/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver15).

### Server specification of on-premises systems

Another aspect to consider is your server specification that handles the
on-premises gateway. If you have too many users accessing the app simultaneously,
your server might not be able to cope with all the requests. In these situations,
you should consider setting up your on-premises gateway to multiple servers, to
form a cluster. More information: [Manage on-premises data gateway high-availability clusters and load balancing](/data-integration/gateway/service-gateway-high-availability-clusters)

### Volume and frequency of data transmission

For high-volume requests, using an approach like dataflows can provide better
performance while still allowing integration with on-premises data.

> [!div class="nextstepaction"]
> [Next step: Data modeling](data-modeling.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]