---
title: Portal templates
description: Learn about various portal templates available in Power Apps.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/19/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
    - sandhangitmsft
---

# Portal templates

Based on the selected environment in Power Apps, you can create a Dataverse starter portal or a portal in an environment containing customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, and Dynamics 365 Project Service Automation).

## Environment with Dataverse

If you select an environment that contains Microsoft Dataverse, you can create a [Dataverse starter portal](create-portal.md). The Dataverse starter portal comes with the sample data for you to quickly get started. It also has the following built-in sample pages:

- Default studio template
- Page with title
- Page with child links

To create a portal in an environment with Dataverse, go to [Create a Dataverse starter portal](create-portal.md).

## Environment with customer engagement apps

If you select an environment that contains customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, or Dynamics 365 Project Service Automation), you can create the following portals:

- **Customer self-service portal**: A customer self-service portal enables customers to access self-service knowledge, support resources, view the progress of their cases, and provide feedback.
- **Partner portal**: A partner portal allows every organization with resellers, distributors, suppliers, or partners to have real-time access to every stage of shared activities.

    > [!NOTE]
    > Field Service and Project Service packages must be installed in your Dynamics 365 organization to enable respective options. For more information, see [Integrate Project Service Automation](/dynamics365/portals/integrate-project-service-automation) and [Integrate Field Service](/dynamics365/portals/integrate-field-service).

- **Employee self-service portal**: An employee self-service portal creates an efficient and well-informed workforce by streamlining common tasks and empowering every employee with a definitive source of knowledge.
- **Community portal**: A community portal leverages peer-to-peer interactions between customers and experts to organically grow the catalog of available knowledge from knowledge base articles, forums, and blogs as well as providing feedback through comments and ratings.
- **Portal from blank**: Create a website to share data with external and internal users. This template comes with sample pages to get you quickly started.
- **Customer Portal (Preview)**: A Supply Chain Management Customer Portal template provisions an externally facing B2B order placing website. This template allows external users to create and view orders to the associated Dynamics 365 for Supply Chain Management environment. Customer Portal template is in *Preview*. For more information about *preview* features, see [Understand preview features in Power Apps](../canvas-apps/working-with-experimental-preview.md).

For creating a portal with any of the above templates, go to [Create a portal with an environment containing customer engagement apps](create-portal.md).

## Portal templates features

The table below summarizes the features associated with each portal template:

| Feature | Customer self-service portal | Partner portal | Employee self-service portal | Community portal | Portal from blank | Dataverse starter portal| Customer Portal (Preview) | 
|------------------|---------------|----------------|---------------|------------------|---------------|------|-|
| World Ready | *  | * | * | * | * |* |*
| Multi-Language Support | *  | * | * | * | * |* |*
| Portal Administration| * | * | * | * | *  |* |*
| Customization and Extensibility  | *   | *  | *   | *  | * |* |*
| Theming   | *   | *   | *    | *   | *   |* |*
| Content Management                     | *                            |                | *                            | *                |               |
| Knowledge Management                   | *                            | *              | *                            | *                |               |
| Support/Case Management                | *                            |   *             | *                            | *                |               |
| Forums                                 | *                            | *               | *                            | *                |               |
| Faceted Search                         | *                            |                | *                            |                  |               |
| Profile Management                     | *                            |                | *                            |                  |               | |*
| Subscribe to Forum Thread              | *                            |                | *                            |                  |               |
| Comments                               | *                            |                | *                            | *                |               |
| [!INCLUDE[pn-azure-shortest](../../includes/pn-azure-shortest.md)] AD Authentication                |                              |                | *                            |                  |               ||*
| Ideas                                  |                              |                |                              | *                |               |
| Blogs                                  |                              |                |                              | *                |               |
| Project Service Automation Integration |                              | *              |                              |                  |               |
| Field Service Integration              |                              | *              |                              |                  |               |
| Partner Onboarding                     |                              | *              |                              |                  |               |
| Portal Base  |  *    | *      |  *| *| *|* |*
| Portal Workflows|  *| *|  *| *| *|* |*
| Web Notifications|  *| *|  *| *| *|* |*
| [!INCLUDE[cc-microsoft](../../includes/cc-microsoft.md)] Identity|   *|  *|  *|   *| *|* |*
| Identity Workflows| *|  *| *|   *| *|* |*
| Advanced Forms|  *| *|    *| *| *|* |*
| Feedback|   *|  *|  *| *| *|* |*
||

## Next steps

[Create a Dataverse starter portal](create-portal.md)

### See also

[Microsoft Learn: Explore Power Apps portals](/learn/modules/explore-portals) <br>
[Create a portal with an environment containing customer engagement apps](create-portal.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]