---
title: Using Microsoft SQL Server securely with Power Apps
description: Understand how to use SQL Server securely with Power Apps.
author: lancedMicrosoft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/24/2021
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - lancedMicrosoft
---

>   Using Microsoft SQL Server securely with Power Apps

>   Microsoft Power Apps is a low-code development environment that supports
>   connections to external data – including Microsoft SQL Server. While Power
>   Apps connects natively to Dataverse with built-in security, there are
>   different ways to
>   [connect](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/connections-list#security-and-types-of-authentication)
>   and authenticate to Microsoft SQL Server with Power Apps. This article
>   outlines concepts that can be helpful in making a choice about how to
>   connect to SQL Server with a security approach that matches requirements for
>   your Power App application. The content here is applicable to other
>   relational databases as well.

Deployment security
===================

Explicit and Implicit connections
---------------------------------

When a Power App application that connects to SQL Server is created, a
connection is also created. When the author publishes and shares their
application, both the Power App and the connection are deployed to specific end
users. Both the Power App application and the connection are visible to end
users. The authentication method used for the connection can be either
**explicit** or **implicit**. Informally, we say that the connection is either
shared explicitly or implicitly. An **explicitly shared connection** means that
the end user of the application must authenticate to Microsoft SQL Server with
their own explicit credentials. Usually this happens behind the scenes as an
Azure AD or Windows handshake. The user doesn’t even notice it happen. An
**implicitly shared connection** means that the user implicitly uses the
credentials of the Power App author. Meaning, the credentials the author used to
connect and authenticate to the data source when authoring the application. The
end user’s credentials are **not** used to authenticate. Each time the end user
runs the app, they are using the credentials the author created the app with.

Below are the four types of connection authentication used with Microsoft SQL
Server:

| Authentication Type                 | Power Apps connection method |
|-------------------------------------|------------------------------|
| Azure AD Integrated                 | Explicit                     |
| Microsoft SQL Server Authentication | Implicit                     |
| Windows Authentication              | Implicit                     |
| Windows Authentication (non-shared) | Explicit                     |

Implicit connection sharing risks
---------------------------------

Since both a Power App and its connections are deployed to end users, it means
that **end users can author new applications based on those connections**. For
instance, let’s say you create a Power App and as part of the Power App you
filter out data you don’t want users to see. It’s there in the database but you
are relying on the filter you authored to ensure that end users won’t see
certain data. When your app is deployed, an end user can use the connection
deployed with your Power App and create a new Power App. In that new Power App,
they can see the data you filtered out in your application. Once an implicitly
shared connection is deployed to end users none of the restrictions you may have
put in the Power App (filters, read-only access, etc.) will hold. The users will
have whatever rights the authentication allows.

Use cases
---------

There are valid use cases for both implicit and explicit authentication methods.
Both security and ease of development are considerations that should be
considered when choosing your approach. As a general rule, use an explicit
authentication method for any situation where you have a business requirement
that the data must be restricted on a row or column basis. A simple example that
requires an explicit connection is a sales manager who should only be allowed to
see price discounts or base cost data that is in the same table where a while a
sales person needs to see product and price.

Not all data must be secured in this way. Keep in mind that **a Power App is
shared and deployed to specific users or groups of users.** Persons outside of
that group do not have access to the Power App or the connection. So, if
everyone in a group is authorized to see all of the data in a database, an
implicit method of sharing works well. Examples include a department that has a
small database of projects they are tracking, departmental work tickets, or even
a corporate calendar for the entire company. In this kind of scenario, the
building of additional apps on top of the implicitly shared connection may be
encouraged as long as all of the data should be accessible by all the people who
are given access. As Power Apps is designed to be approachable by end users,
this kind of scenario is common because the development cost associated with
implicit connections is low.

Departmental based apps can grow into enterprise wide and mission critical
applications. In these scenarios, it’s important to understand that as a
departmental app moves to be enterprise wide, it will need to have traditional
enterprise security built in. This is more developmentally more expensive but
important in corporate-wide scenarios.

Client & Server side security
=============================

You cannot rely on the security of data through filtering or other client-side
operations to be secure. Applications that require secure filtering of data must
ensure that the user identification and the filtering both happen on the server.
The way to ensure that server side filters work is for the user identity and
authentication to take place separate from the application through a service
such as Azure Active Directory.

![Chart Description automatically generated with medium confidence](media/sql-server-security/ba4d1b3991f6a3eb22d6d5b06b9c15c6.png)

In a client security app pattern, [1] the user only authenticates to the
application on the client side. Then [2] the application requests information of
the service and [3] the service returns the information solely based on the data
request. In a server-side security pattern, [1] the user first authenticates to
the service so the user is known to the service. Then, [2] when a call is made
from the application the service [3] uses the known identity of the current user
to filter the data appropriately and [4] returns the data.

![Diagram Description automatically generated](media/sql-server-security/5308dab450f3d52d1141e2bfe8e88963.png)

The implicit departmental sharing scenarios described above is combination of
these two patterns. The user must log in to the Power App service using AAD
credentials. This is the Server security app pattern. The user is known via the
AAD identity on the service. So, the app is restricted to the set of users to
which Power Apps has formally shared the application. But the implicit shared
connection to SQL Server is the Client security app pattern. SQL Server only
knows that a specific user name and password is used. Any client side filtering,
for instance, can be bypassed with a new application using the same user name
and password.

To securely filter data on the server side use built-in security features in
Microsoft SQL Server such as [row level
security](https://docs.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver15)
for rows and the
[deny](https://docs.microsoft.com/en-us/sql/t-sql/statements/deny-object-permissions-transact-sql?view=sql-server-ver15)
permissions to specific objects (e.g., columns) to specific users. This approach
will use the AAD user identity to filter the data on the server.

Some existing corporate services have used an approach where the user identity
is captured in a business data layer much in the same way that Dataverse does.
In this case the business layer may or may not leverage SQL Server’s row level
security and deny features directly. If it does not, it is often the case that
security is enabled via stored procedures or views. The business layer (on the
server side) uses a known user AAD identity to invoke a stored procedure as a
SQL Server principal and filter the data. However, Power Apps does not currently
connect to Stored Procedures. Alternatively, a business layer may invoke a view
which leverages the AAD identity as a SQL Server principal. In this case use
Power apps to connect to the views so that the data is filtered server side. If
you only expose views to users you may need to use Power Automate for updates.
