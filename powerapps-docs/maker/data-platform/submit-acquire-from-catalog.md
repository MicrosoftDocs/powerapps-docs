---
title: "View, submit, and install catalog items"
description: "Learn how to submit and acquire items from your organization's catalog."
author: isaacwinoto
ms.author: isaacwinoto
ms.date: 11/14/2024
ms.reviewer: matp
ms.topic: how-to
ms.subservice: dataverse-maker
search.audienceType: 
  - maker
---
# View, submit, and install catalog items

In any organization, there might be many components and templates distributed among many environments. The catalog in Power Platform enables developers and makers to:

- Crowd-source and find templates and components within their organization easily
- Find and install the latest and authoritative version of a component
- Get started with templates and components that provide immediate value

> [!IMPORTANT]
> You need a Managed Environment in order to submit items to the catalog. You can however install catalog items from any environment. More information: [Managed Environments overview](/power-platform/admin/managed-environment-overview)

Before reading this article, you should:

- [Learn about the catalog](catalog-overview.md)
- [Learn how administrators setup and configure the catalog](/power-platform/admin/administer-catalog)

> [!NOTE]
> Developers can also use the Power Platform CLI, Dataverse SDK for .NET, and Dataverse Web API to perform the operations described here. [Catalog in Power Platform for developers](/power-platform/developer/catalog/overview)

## Access controls

The catalog has a separate set of access controls from Power Platform. This means makers in a given environment don't automatically get permissions to publish and acquire items from the catalog. There are four access roles:

|Role|Enables user to:|
|---------|---------|
|**Catalog Submitter**|Submit items to the catalog|
|**Catalog Consumer**|Discover and install items from the catalog|
|**Catalog Approver**|Approve submissions to the catalog.<br />Catalog approvers can be users from your central IT department or line of business that your organization wants to empower to participate in the approvals process.|
|**Catalog Admin**|Administer the catalog.|

Any environment that has a catalog sees these roles inside of Power Platform admin center, and can be [assigned to groups or individuals](/power-platform/admin/security-roles-privileges) just like any other security roles.

Power Platform admins and system customizers already have full access to the catalog. However, don't assign these roles for generally managing catalog access, and instead use one of the roles in the previous table.

## Submission

[Unmanaged solutions](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions) in your environment can be published to the catalog. In your normal course of creating solutions, you might decide that what you're building would be useful as a reusable artifact for yourself or others in your organization.

Navigate to your solutions page, and any unmanaged solution has a new option for **Publish to Catalog** in the three vertical dots next to the solution display name. This option is disabled for anyone without the **Catalog Submitter** role.

:::image type="content" source="media/catalog_submission.png" lightbox="media/catalog_submission.png" alt-text="Catalog submission":::

> [!NOTE]
> This option is not enabled for managed solutions. You can't submit managed solutions into the catalog.

You can't submit an app, flow, or other component directly into the catalog. You must first ensure it exists in an unmanaged solution. You can add it to an unmanaged solution by selecting **New solution** on top of the **Solutions** area or by selecting an existing one from the list, and then selecting **Add existing** in the top menu in the solution itself, and adding your desired component (such as an app or a flow).

:::image type="content" source="media/add_to_solution.png" lightbox="media/add_to_solution.png" alt-text="Add to solution":::

> [!NOTE]
> Any maker with the **Catalog Submitter** role in a given environment will be able to publish. However, after a solution is published, a maker needs to be a part of the publishing group to re-publish that same solution again. You see this error if you don't have access, which you can request from your admin.

:::image type="content" source="media/access_error_submission.png" lightbox="media/access_error_submission.png" alt-text="Access needed: This solution has already been published to the catalog error":::

When you select **Publish to Catalog**, there's a wizard with four steps:

### Step 1: Add your solution

1. **Select a catalog**: If you have multiple catalogs set up, you can select which catalog you would like to publish this item to.
1. Select **managed item** or **template** for your submission.

   - **Managed items** can't be edited by other makers, your environment shares a single copy, and that copy can be versioned with updates over time. Makers can then update their solutions with your updates.
   - A **template** is a standalone copy that can be edited, makers can have as many copies as they want, and won't automatically update solutions in environments when new updates are published.

1. **Select a primary component**: A solution might have many components in it. You might want makers to open a specific component for editing after they install it, such as opening Canvas Studio for your canvas app. Set the primary component to whichever you think is the "focus" of the solution, otherwise, set **Unspecified**, and installers go the solution itself.

#### Resubmitting items

If you're resubmitting an item, you get an alert message notifying you about the resubmission. You're prompted with a version field. The last digit of the version number is automatically incremented for you. You can modify the version number if you like, but don't set the version number to a lower number from this interface. Updating the version number in the catalog submission updates the version number in the original solution as well.

Keep these points in mind when resubmitting items:

- Resubmitting a **template** replaces the previous item in the catalog, and doesn't affect any solutions already using the previous catalog item. Makers who now install your resubmission get your newest version.
- Resubmitting **managed items** will update the catalog item with your most recent version, and the next time makers see your catalog item in an environment where that catalog item was already installed, they'll see an **Update** button, which installs the most recent changes to the managed item into that environment, and then all solutions using that managed item will be updated as well.
- You can't resubmit a managed item as a template, and vice versa.

### Step 2: Catalog info

Enter the following information:

|Field|Instructions|
|---------|---------|
|**Title**|Rename the item if needed before it gets submitted to catalog. The default is the solution name. You can't edit title when submitted a managed item.|
|**Description**|Provide details on this catalog item. Makers read your description in the catalog gallery to find out more about it.|
|**Business justification**|By default, your admin must approve all catalog submissions before they're added to the catalog. This field provides a justification for your submission to your admin.|
|**Works with**|A flow that you're building might be intended to **work with** canvas apps and model apps, for example. Indicate here what your catalog item is intended to work with.|
|**Business categories**|Select up to five business categories that describe your catalog item. Makers use these categories to search for catalog items that are of interest to them.|
|**Publisher**|Select an existing publisher in this environment, or create a new publisher, to connect to this catalog submission. A maker can't resubmit a catalog item unless they're part of the publishing group that submitted the item the first time.|
|**Author**|This defaults to the current user, but you can change it if needed|

### Step 3: Solution info

Enter the following information:

|Field|Instructions|
|---------|---------|
|**Solution icon**|Attach an icon to your solution (216 x 216 pixel) to help identify it in the catalog gallery|
|**template images**|Attach some screenshots or other visuals that can help makers understand more details about this catalog item|
|**Help link**|Add the URL for any help documentation|
|**Privacy policy link**|Add the URL for any privacy policy documentation |
|**Legal terms link**|Add the URL for any legal terms documentation|

### Step 4: Review and finish

This last step provides a summary of all the info you provided. If everything looks good, select **Submit** to publish to the catalog. As previously mentioned, if your catalog requires an approver before submission can complete, you need to wait for approval. Contact your admin or approver if you need the process accelerated.
  
## Acquisition

As makers browse the **Discover** page and find catalog items that are useful for them, they can acquire those artifacts and install a copy into their environment to start using or building with. Selecting **Get** on any template or managed item opens a details popup that contains information like description, links, included components, business categories, expandable screenshots, and more.

:::image type="content" source="media/catalog_item.png" lightbox="media/catalog_item.png" alt-text="Catalog item tile":::

If the details meet what the maker is looking for, they can select **Get** on the details popup to start the acquisition wizard.

> [!NOTE]
> If the catalog item is a managed item, and has already been installed in the environment, you can't install the managed item again, as the environment shares that managed item. If the managed item has already been installed in an environment, and an update has been published to the managed item, you see an **Update** button instead of **Get**, which updates the shared managed solution in the environment. If the managed item was already updated, and no new updates have been published, the **Update** button is disabled until a new update is published.

The acquisition wizard has four steps:

### Step 1: Check connections

This step checks the connections for the solution to make sure they're working for you in your environment. If there are any connection issues, you see a red status notification, and can resolve by selecting the ellipsis (&hellip;) next to the problematic connection to update it.

### Step 2: Environment variables

The publishing maker might decide some environment variables need to be specified before you can acquire the solution. Typically, these variables are set to some default value. If unsure of what to fill out, check with the author of the catalog item or in the details of the catalog listing, available on the catalog details. More information: [Step 2: Catalog info](#step-2-catalog-info)

### Step 3: Configuration

The publishing maker determines this step, if they want you to provide any additional information for using the solution. This might include things like, "*What days of the week do you run a report?*". If no additional information needed, this step is blank.

### Step 4: Summary

When you reach the final step, the summary screen, you're now waiting for the catalog item to install into your environment. Depending on the complexity, this might take from less than a minute to several minutes. When complete, you're given several options in the dropdown, depending on what's included in the catalog item, and if the author set a primary component. The following is an example where a canvas app is the primary component of the catalog item:

:::image type="content" source="media/acquisition_options.png" lightbox="media/acquisition_options.png" alt-text="Catalog item install options":::

In this example, you can:

- **Edit App**: Opens the app in Canvas Studio
- **Go to App**: Takes you to the app screen, if you aren't ready to edit yet
- **Go to Solutions**: Opens the solution file

Depending on what is contained in the catalog item package, different options appear.

After the catalog item is installed, you can find the catalog item:

- In the **Unmanaged solutions** list in the solutions page if the catalog item was a **template**
- In the **Managed solutions** list in the solutions page if the catalog item was a **managed item**

As previously mentioned, templates can be acquired as many times as you like, each as its own copy. The catalog appends a suffix to the unmanaged solution display name to differentiate the different copies. Managed items can be acquired only once into the managed solutions list, and all makers in the environment share the same managed solution. This means you can't acquire a managed item back into the same environment it was published from and the **Update** button is disabled.

### See also

[Catalog in Power Platform)](catalog-overview.md)   
[Administer the catalog](/power-platform/admin/administer-catalog)   
[Catalog in Power Platform for developers](/power-platform/developer/catalog/overview)
