---
title: Steps to building a model-driven app
description: Learn the detailed steps required to build a model-driven app in Power Apps.
keywords: App designer; site map designer; my apps
author: Mattp123
ms.subservice: mda-maker
ms.author: matp
ms.date: 01/28/2025
ms.topic: how-to
applies_to: 
  - PowerApps
ms.assetid: 26c79c20-2987-476e-983a-406e0db13034
search.audienceType: 
  - maker

---
# Steps to building a model-driven app

This page describes the steps associated with building a model-driven app in Power Apps.

## Steps to building and sharing a model driven app

At a fundamental level, model-driven app making consists of the following stages.

|Stage|Purpose|
|-----|-------|
|Modeling business data| To ensure that the data is constructed in the correct way to address the business problem.
|Defining business processes| To help users to update the tables and complete their work efficiently and accurately.
| Composing the app|To create the app and select the tables, and elements of tables relevant to the app.
|Configuring security roles| To ensure that app users can only interact with data relevant to their roles.
|Sharing the app|App distribution.

Each stage requires a range of [editors](model-driven-designers.md) to ensure that the application can be created, whether the app maker is updating the data model, or going through the process of composing the app.

While it might seem strange to have multiple editors, these reflect the various technologies that have been brought to bear within Microsoft Dataverse. Often makers move seamlessly through the editors to construct the app.

For a simple walk-through of building a first app, go to [building a first model-driven app](build-first-model-driven-app.md).

## Modeling business data

To model business data, you determine what data your app needs and how that data relates to other data. Model-driven design uses a metadata-driven architecture so that designers can customize the application without writing code. Metadata means “data about data” and it defines the structure of the data stored in the system.

> [!NOTE]
> With the exception of model-driven apps that have a custom page, model-driven apps can't be created without Dataverse tables. However, Dataverse tables can be used by many Power Platform services, including canvas apps and Power Automate.

[Tutorial: Create a custom table that has components in Power Apps](../data-platform/create-custom-entity.md)

## Defining business processes

Defining and enforcing consistent business processes is an important aspect of model-driven app design. However, it should be noted that it's possible to create a model-driven app without a business process configured around it.

Nevertheless, consistent processes help make sure your app users focus on their work and not on remembering to perform a set of manual steps. These processes can be simple or complex and can contain operations on multiple tables.

The screenshot here illustrates the impact of having a business process flow in place.

:::image type="content" source="../../user/media/business-process.png" alt-text="Sample model-driven app with business process flow" lightbox="../../user/media/business-process.png":::

Business process flows are created and configured using Power Automate.  

More information: [Business process flows overview](/power-automate/business-process-flows-overview) and [Apply business logic with Microsoft Dataverse](../data-platform/processes.md).

## Composing the model-driven app

After you create a data model and define business processes where necessary, the app can be built.

This is done by building an app using the modern editors.

With the modern editors (also known as designers), makers can see the effects of the changes that they make while designing, whereas with the legacy interfaces there was a level of abstraction between the final user experience and the design experience.
More information:

[Learn how to build a modern app](build-first-model-driven-app.md)

When you build an app, a [site map](model-driven-app-glossary.md#site-map) is created, defining the navigation experience for users. With the modern app designer, this is a part of the app design process.

More information: [Building a site map](create-site-map-app.md)

### Playing the app

Play your app through the [app designer](model-driven-app-glossary.md#app-designer).

Once these stages are complete, you can move onto the final phases associated with distributing your app.

## Configuring security roles

Access to tables is defined using security roles and these roles govern the actions that users can perform with the tables within Dataverse. Without this, users have no meaningful access to the app.

These actions cover Create, Read, Write, Delete, Append, Append To, Assign, and Share. Security roles need to be first configured and then users are assigned to roles at the point of sharing.

For more information on understanding, creating and configuring security roles go to:

- [Power Platform documentation](/power-platform/admin/security-roles-privileges)
- [Get started with security roles in Dataverse](/training/modules/get-started-security-roles/)

## Sharing the app

To share an app, two actions are required:

- Assign the user a security role. This means that they have permission to see the data.

   :::image type="content" source="media/share-model-driven-app/share-app.png" alt-text="Sample model-driven app":::

- Share a link to the app. To get the link:

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Apps** on the left navigation pane.
1. Select the model-driven app you want, and then select **Details** on the command bar.
1. Copy the **Web link**. Alternatively, you can make a copy of the **Mobile QR code** for mobile users.
1. Paste the app URL in a location so that your users can access it, such as by posting it on a SharePoint site or send via email.

Sharing an app and security roles are intrinsically linked. To properly share an app, you need to have a strong understanding of both.  [Discover more about sharing apps and establishing security](share-model-driven-app.md)

## Using a model-driven app

Documentation is available that helps users of model-driven apps successfully navigate around and interact in ways that help make them more productive. [Learn more about using model-driven apps](/powerapps/user/use-model-driven-apps)

## Next steps

[Build your first modern app](build-first-model-driven-app.md)

[Meet the model-driven app designers](model-driven-designers.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
