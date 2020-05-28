Working with enterprise systems
===============================

When you need to work and integrate with existing enterprise systems such as
SAP, Oracle, Web Ordering system, you should seek cooperation and support from
your IT administration team or the team in charge of the system.

Even if you aren’t in a technical role, read this section to understand some of
the things that typically need to be taken into consideration when integrating
with enterprise systems.

Frequency and time of data integration
--------------------------------------

When integrating with other systems, you need to consider frequency of
integration, and time zones if the integration has cross-time-zone use cases.
The frequency of integration will depend on two aspects: the data volume and the
time-related requirements of the business.

Method of integrating with enterprise systems
---------------------------------------------

There are several ways of integrating with enterprise systems.

-   **Database** integration is a direct integration with a database. This is
    not a very common way of integrating with external systems
    as there is a risk of exposure of data.

-   **API** (Application Programming Interface) integration is a method of
    integrating with systems using APIs. The majority of web systems provide APIs to integrate with, but there are some systems that don't.

-   **File** integration is a method of integrating with other systems using
    files. One system exports a file with sets of data. This file could be CSV,
    TSV, XML etc. The system to integrate to then either detects there is a new
    file, or is set up with a timer to periodically scan if new files exist to
    import the file that was exported. This method is used in situations where
    the data source cannot be accessed directly via database or APIs.

Connecting to on-premise systems
--------------------------------

On-premise data gateway allows Power Apps and services to connect to systems
that are not open to the internet in a secure manner. Setting up is easy using
an installer, but there are several factors to consider:

-   Network bandwidth of the datacenter/server location

-   Database tuning of data source

-   Server specification of on-premise systems

-   Volume and frequency of data transmission

### Network bandwidth of the datacenter/server location

The speed of the app will depend on whether the network bandwidth between the
on-premise datacenter/server and the cloud service is sufficient. If there are
many people using the app simultaneously, not having enough bandwidth will cause
the app to take a long time to respond. [See this document for minimum
requirements for network
bandwidth](https://docs.microsoft.com/power-platform/admin/web-application-requirements).

To find out the network speed of your organization, we provide the [Network
Speed
Test](https://www.microsoft.com/p/network-speed-test/9wzdncrfhx52)
from Microsoft Store (free of charge) and also [diagnostic
tools](https://docs.microsoft.com/power-platform/admin/web-application-requirements)
specifically for model-driven apps.

### Database tuning of data source

Database tuning also plays an important role especially if you are going to
connect to a data source with lots of data. It is easy to start facing problems
if you have created an app that uses data in a way that it was not used
previously.

For example, suppose your existing customer management system is optimized to
search using a first name, last name, and email address, but you made a new
Power App that searches using phone number.

Indexing helps your apps speed up searches etc, and missing indexes is a problem
as it takes longer to search and query for data. You may need to contact the IT
team for the data source to discuss how you’ll access the data and add
additional indexes. For more details on indexing with Microsoft SQL server, have
a look at the [SQL Server Index Architecture and Design
Guide](https://docs.microsoft.com/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver15).

### Server specification of on-premise systems

Another aspect to consider is your server specification that handles the
on-premise gateway. If you have too many users accessing the app simultaneously,
your server may not be able to cope with all the requests. In these situations,
you should consider setting up your on-premise gateway to multiple servers to
form a cluster. [This document explains the steps to set up a
cluster.](https://docs.microsoft.com/data-integration/gateway/service-gateway-high-availability-clusters)

### Volume and frequency of data transmission 

For high volume requests, an approach like dataflows can provide better
performance while still allowing integration with on-premise data.
