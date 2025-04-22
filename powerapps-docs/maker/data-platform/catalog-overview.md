---
title: "Catalog in Power Platform"
description: "Use the catalog in Power Platform to managed shared components and templates so that administrators, application makers, and developers within an organization can reuse each other's work."
author: derekkwanpm
ms.author: matp
ms.date: 09/10/2024
ms.reviewer: matp
ms.topic: overview
ms.subservice: dataverse-maker
contributors:
 - JimDaly
 - ChrisGarty
---
# Catalog in Power Platform

Building from scratch every time by recreating branding, layouts, links, complex connectors and flows, and more is painful and error-prone. Organizations where developers and makers build and share customized and reusable components and templates get more value from Power Platform. Successful organizations adopt a *fusion teams* model where pro-developers, makers, and admins all work together to deliver the best solutions for their users, and derive the highest value possible from Power Platform.

> [!IMPORTANT]
>
> - The catalog needs to be set up by an admin before you can use it, including permissions. More information [Administer the catalog](/power-platform/admin/administer-catalog#set-up-the-catalog).
> - The catalog only works with Microsoft Dataverse environments. Environments without Dataverse aren't supported at this time.
> - You need a Managed Environment in order to submit solutions to the catalog. However, you can install catalog items from any environment. More information: [Managed Environments overview](/power-platform/admin/managed-environment-overview)

In any organization, there might be many components and templates distributed among many environments. The catalog in Power Platform enables developers and makers to:

- Crowd-source and find templates and components within their organization easily
- Find and install the latest and authoritative version of a component
- Get started with templates and components that provide immediate value

*Components* include things like:

- AI prompts
- Copilot app templates
- AI plugins
- Power Platform dataflows
- Custom connectors
- Power Apps component framework controls
- Power Automate flows
- Canvas apps
- Model-driven apps

*Templates* are items that represent an advanced starting point for components. Templates connect to their enterprise systems and resources and utilize an organization's themes.

## Terminology

These terms are important to understand when using the catalog:

|Term|Description|
|---------|---------|
|**Catalog Item**|The unit of interaction with the catalog is called an item. <br />- An item is what is being submitted to or installed from the catalog. <br /> - Typically, an item is a Dataverse solution or package deployer package. An item can contain a fully built application, a template for a Power App or flow, or a Power Platform code-first component such as a custom connector or Power Apps component framework (PCF) control. |
|**Catalog Publisher**|The owning entity of the application. For example, the publisher can be the human resources IT team or another line of business team.<br /> - A group of people in an organization that are responsible for managing its lifecycle. <br /> - Support and engineering contacts can be provided.<br /> - Note that the catalog publisher is different from the solution publisher.|
|**Submission** |The act of sharing an item involves submitting it to the catalog. This act creates a *submission request* in the system.|
|**Submission Request**|The result of a submission. This request can be approved or declined. When auto approval is configured for the catalog, no approval is required.|
|**Discovery**|Act of finding items within a catalog by authorized users.|
|**Acquisition**|Act of installing the item to a target environment by a developer.|

## Catalog basics

The catalog needs to be set up by an admin before you can use it, including privileges. More information: [Administer the catalog](/power-platform/admin/administer-catalog#set-up-the-catalog).

You might choose to have multiple catalogs across environments for different regions, departments, or any group. Most organizations only need one catalog. A catalog admin can set up new catalogs in the [Power Platform admin center](https://admin.powerplatform.microsoft.com).

You can submit unmanaged solutions to the catalog for other makers to install and use for themselves, as one of these two catalog item types:

- A **template**: A copy of your unmanaged solution that other makers can edit however they choose. Updates to the original unmanaged solution won't update templates, as templates are no longer "connected" to the solution it came from. If you want other makers to have the ability to change the catalog components as they see fit, use a template.

   > [!NOTE]
   > Currently, certain components aren't supported for use as templates. The supported components for templates are:
   > - Table and its sub components like forms, saved queries, relationships, table maps.
   > - Environment variables.
   > - Canvas apps.
   > - Modern workflows.
   > - Security roles.
   > - `AiModel` and its subcomponents like `AiConfig`.
   > - Web resources.
   > - Power Apps component framework components. This includes modern solution aware components created using the Power Apps component framework. For example custom API, `AiPlugin`, and `AIPlugin` operation.

- A **managed item**: Managed items can be updated with more versions as the original solution is updated, but are generally restricted from editing. If you want makers to use your solution *as is* and you also want to keep copies updated with your changes in the future, use a managed item. Managed items are useful for a variety of scenarios for makers:

  - Use the assets of the managed item as is and make no changes.
  - Build custom functionality on top of the assets in the managed item without changing the original components.
  - Use the assets to assist with building your own solutions. For example, PCF components, custom connectors, and so on.

Admins can administer catalogs, manage access and security, approve catalog items, and more in the [Catalog Manager](/power-platform/admin/administer-catalog), which is the dedicated workspace for admins of the catalog. The catalog itself is designed for makers of any level of experience to publish, discover, and acquire useful catalog items for themselves.  

## Discovery

The catalog area is available in Power Apps and Power Automate. On the catalog page are tiles representing all catalog items available to your organization. This includes items published by your organization, approved partners who have access to your environments, as well as many published by Microsoft, such as AI prompts, Copilot app templates, dataflow templates, enterprise templates, PCF controls, plug-ins, and more.  

:::image type="content" source="media/catalog_gallery.png" lightbox="media/catalog_gallery.png" alt-text="The catalog gallery":::

On the page itself are the following controls:

- Search box (searches the titles of available catalog items)
- Filters (filters for publisher, type, category, and more)
- Catalog selector (some organizations might choose to create multiple catalogs for regions or departments). Users can have access to one or more catalogs.

The list of Microsoft published catalog items that will be available in your catalog out of the box are:

- AI Prompts
- Copilot app templates
- Enterprise templates
- Power Platform dataflows
- PCF controls
- Plug-ins
- Retail cloud templates
- Copilot agents

## My Activity

Linked in the banner of the catalog page is the **My Activity** page. This shows useful info on items you have submitted and acquired, including approval status.

:::image type="content" source="media/myactivity_catalog.png" lightbox="media/myactivity_catalog.png" alt-text="The catalog My Activity page":::

Filters on top of the page allow you to look at different date ranges, types of catalog items, and across different catalogs (if you have multiple catalogs set up in your tenant).

- Metrics on this page:

  - **Total items submitted**: Sum of all items you submitted.
  - **Items approved**: Sum of all items you submitted that were approved by your admin.
  - **Items awaiting approval**: Sum of all items you submitted that your admin has not responded to yet.
  - **Items acquired**: Sum of all items you acquired from the catalog.

- Catalog items acquired table:

  - **Item ID**: Unique identifier for the acquired item.
  - **Item name**: Display name for the acquired item.
  - **Deployment type**: Whether item is a template or managed.
  - **Date acquired**: Date item was last acquired.
  - **Status**: Current status of the acquired item, such as completed or failed.
  - **Message**: Status message, can explain why an item failed.

- Catalog items submitted table:

  - **Item ID**: Unique identifier for the submitted item.
  - **Item name**: Display name for the submitted item.
  - **Deployment type**: Whether item is a template or managed.
  - **Date submitted**: Date item was last submitted.
  - **Status**: Current status of the submitted item, such as approved, rejected, or pending approval.
  - **Reject reason**: Why a submitted item was rejected by an admin.
  
## Frequently asked questions (FAQ)

The following are frequently asked questions related to catalog in Power Platform.

### Where do I provide feedback on catalog?

Ask questions and submit feedback at: [github.com/microsoft/PowerPlatform-Catalog/discussions](https://github.com/microsoft/PowerPlatform-Catalog/discussions)

### What are the items in the catalog?

The catalog items are actually packages. A package contains one or more solutions and some metadata. The [Power Apps](https://make.powerapps.com) experiences can submit individual solutions. The Power Platform CLI experience can be used to create a package containing multiple solutions.

### What are solution templates? What does it mean to install an unmanaged solution?

The use of a [solution](/power-platform/alm/solution-concepts-alm) as a *solution template* is a new scenario we're making available with the catalog. When a maker acquires a solution template, they'll get a new unmanaged copy of that solution. Multiple copies of that [unmanaged solution](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions) can exist in the same environment and each has a unique identifier.

### Catalog item install looks a lot like solution import. Are they the same thing?

A catalog item is a package that contains one or more solutions. Installation of a package containing a single solution with no other package configuration looks similar to a solution import.

### Will the catalog support PCF components within solutions? What about other solution component types?

Yes, distribution of [PCF controls](/power-apps/developer/component-framework/overview) is made easier by using a catalog. Any [solution component](/power-platform/alm/solution-concepts-alm#solution-components) can be contained in a solution in the catalog.

### Can the templates have multiple owners so people know who to reach out to for more information?

Yes, ownership information is part of the metadata for a catalog item. The ownership can be a group with multiple people in it.

### Is there a way to add documentation such as a user guide when submitting a template?

Yes, documentation links are part of the metadata for a catalog item.

### Can catalogs be shared to security groups?

Yes, catalog permissions can be targeted at [specific security groups](/power-platform/admin/administer-catalog#access-controls).

## Next steps

Learn how to administer the catalog.

> [!div class="nextstepaction"]
> [Administer the catalog](/power-platform/admin/administer-catalog)

Learn how to view, submit, and install catalog items.

> [!div class="nextstepaction"]
> [Submit and install catalog items](submit-acquire-from-catalog.md)

Ask questions or contact the project team on GitHub.

> [!div class="nextstepaction"]
> [github.com/microsoft/PowerPlatform-Catalog/discussions](https://github.com/microsoft/PowerPlatform-Catalog/discussions)
