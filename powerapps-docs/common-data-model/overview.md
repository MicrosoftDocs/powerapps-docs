---
title: What is the Common Data Model (CDM) | Microsoft Docs
description: "Common Data Model is a standardized, modular, extensible collection of data schemas published by Microsoft that are designed to make it easier for you build, use, and analyze data.
author: RobertBruckner
ms.service: powerapps
ms.topic: article
ms.date: 07/24/2018
ms.author: robruc
---

# What is the Common Data Model?

If you’ve ever run into challenges with data that’s *nearly* the same or
*should* work together – then spent significant effort transforming fields and
tables to work with your other data – you know that common data elements can
save effort, streamline future development, and enable faster analytics. Those
capabilities and more are what the Common Data Model can provide.

The **Common Data Model (CDM)** is a standardized, modular, extensible collection of
data schemas published by Microsoft that are designed to make it easier for you to
build, use, and analyze data. This collection of predefined schemas—consisting
of *entities*, *attributes*, *semantic metadata* and *relationships*—represent
commonly used concepts and activities, such as Account and Campaign, to simplify
the creation, aggregation, and analysis of data.

![Common Data Model](media/cdm-entities.png)

## Why use the Common Data Model?

The Common Data Model simplifies data management and application development
by unifying data into a known form, and by applying structural and semantic
consistency across multiple applications and deployments. In other words, once
your data is in the Common Data Model, you can use it in many different
applications, streamline the creation or use of other applications to make use
of that existing data, and easily build reports for each of them (or all of
them). In addition, data integrators who bring data from a variety of systems
can focus on landing the data in the Common Data Model, instead of building
a new model for each application.

Imagine you have three business applications – a materials app, a manufacturing
app, and a sales app. Often each of the applications would be created
independently, with different structures representing an entity, such as
*Account*, that are nearly the same (but not) . With the Common Data Model,
you could build your data in a standardized format (using the **Common Data
Model** entities, attributes, and relationships), and then each of those three
apps could use the same data as a basis. Of course each app could have its own
additional data and schemas, based on the functionality of each app. But when it
comes to development, your applications and reports could pull the common data
elements quickly, cleanly, and with confidence.

And what about the need to create a fourth app? Your data is ready, in the
Common Data Model schema, so your development efforts can concentrate on
business logic, not data quagmires and sticky transformations.

In other words, the Common Data Model offers the following for your data:

-   **Structural and semantic consistency** across applications and deployments.

-   **Simplified integration and disambiguation of data** that’s collected from
    processes, digital interactions, product telemetry, people interactions, and
    so on.

-   **A unified shape** where data integrations can **combine existing
    enterprise data with other sources**, and use that data holistically to
    develop new applications or derive insights.

-   **Ability to extend the schema and CDM entities** to tailor the Common Data
    Model to your organization.

You can use the Common Data Model to create new data repositories that
match the schema, and you can also transform your existing data into the Common
Data Model schema. Either way, the efficiency you get from standardization can
expedite and streamline whatever you do next with your data.

## Who uses the Common Data Model?

The Common Data Model is used by a variety of customers, partners and products
all with the same goal of unifying data in well-known form with semantic
meaning.

-   **Application Makers/Developers –** whether these users leverage code-based
    platforms or a low-code/no-code platform like PowerApps, they need to store
    and manage data for their applications.

-   **Data Integrators –** these users are responsible for bringing data from a
    variety of systems to make it accessible for Applications to use.

Historically, the work to build an application has been tightly tied with data
integration, but with the **Common Data Model** and the platforms that support
it, the two can happen independently.

## Common Data Model in Action

Microsoft and its partners use the Common Data Model for their own
applications and offerings, and are building additional services and offering
based on Common Data Model schemas. The following examples show how
organizations use the Common Data Model:

-   The Common Data Service for Applications, which supports Dynamics and
    PowerApps, stores data in conformances with the CDM definition. In fact,
    many of the original business entities including in the CDM came from
    Dynamics offerings such as Dynamics 365 for Sales and Dynamics 365 for
    Marketing.

-   **Industry verticals** such as Healthcare are working closely with Microsoft
    to extend the Common Data Model to their specific business
    concepts, such as *Patient* and *Care Plan*, so they can share data and
    build services so partners can easily exchange data, create interoperable
    apps and services, and create quick analytics that are easy to share.

## Next step


The following articles describe the Common Data Model in more depth, discuss use
cases for creating new data in CDM or transforming your existing data into CDM,
and also discuss programming interfaces and capabilities.

Read the following articles for more information about the **Common Data Model
(CDM)**:

-   How to use the Common Data Model (CDM)

