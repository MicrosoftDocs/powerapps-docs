---
title: Dataverse Accelerator | Microsoft Docs
description:  The Dataverse Accelerator rapidly delivers experimental and innovative Dataverse development capabilities to empowers Power Platform makers.
author: denise-msft
ms.author: demora
ms.service: powerapps
ms.topic: how-to
ms.date: 03/17/2024
ms.custom: template-how-to
contributors:
- dikamath
---

# Use the Dataverse Accelerator (preview)

The Dataverse Accelerator is a powerful toolkit designed to streamline and expedite the development process within Microsoft Dataverse. By leveraging pre-built components, templates, and best practices, developers can significantly reduce development time while maintaining high standards of quality and efficiency.

> [!NOTE]
> The Dataverse Accelerator user interface is built on the Power Platform [custom pages feature](../../model-driven-apps/model-app-page-overview.md). As part of these updates we're deploying into environments using system maintenance accounts. In some circumstances these accounts have had an unexpected side effect of presenting as a [break-glass account](/entra/identity/role-based-access-control/security-emergency-access). We're working to correct this behavior as quickly as possible. In the meantime the following apps might appear in the Power Platform admin center:
> - Dataverse Accelerator app – &lt;model-driven app&gt;, created by a global admin account
> - Dataverse Actions page - &lt;canvas app&gt; This is a Custom page on which the low-code plugin is built, created with the user name associated to the global admin account.
> - Overview page - &lt;canvas app&gt; This is a custom page on which the low-code plugin is built, created with the user name associated to the global admin account.

## Prerequisites

Before you begin using the Dataverse Accelerator, ensure that you have the following prerequisites:

- Access to a Microsoft Dataverse environment.
- Basic familiarity with Power Platform and Dataverse concepts.
- Appropriate permissions to install and configure solutions (e.g., system administrator or system customizer security role)
- Access to the Dataverse accelerator app.

## Manage the Dataverse Accelerator app

The Dataverse Accelerator app is hosted on App Source as a [Dynamics 365 app](/power-platform/admin/manage-apps). It is automatically installed in every new environment, and can be managed through the existing App Source platform.

### Install

The Dataverse Accelerator app is automatically installed in all Power Platform environments with a Microsoft Dataverse database enabled.

If the Dataverse Accelerator is not already installed in an environment, follow the steps to [install an app in the environment view](/power-platform/admin/manage-apps#install-an-app-in-the-environment-view) for the Dataverse Accelerator.

### Update

If the Dataverse Accelerator is already installed in your environment and you want to install the latest version, follow these steps:

1. Navigate to the [environment-level view of apps](/power-platform/admin/manage-apps#environment-level-view-of-apps)
1. Locate the **Dataverse Accelerator** app listing.
1. If an update is available, click the **Update available** link next to the listing.

> [!TIP]
> Enable auto app updates for the Microsoft - Power CAT publisher to automatically receive updates when available (not necessary for new environments created after October 1st 2023).

### Delete

You can delete the Dataverse Accelerator app from an environment using pac cli.

> [!NOTE]
> Deleting the Dataverse Accelerator app will not delete the underlying capibilities presented in the app. The app is just a vessle, presenting platform features in a modern shell.

Using pac cli, [connect to the target environment](/power-platform/developer/cli/reference/connection#pac-connection-create) and execute the three [solution delete](/power-platform/developer/cli/reference/solution#pac-solution-delete) commands below:

```powershell
pac solution delete --solution-name msdyn_DataverseAcceleratorApp 
pac solution delete --solution-name DataverseAccelerator 
pac solution delete --solution-name DataverseAccelerator_Anchor 
```

## Features

| Feature | Description |
| -- | -- |
| [Low Code Plugins](/powerapps-docs/maker/data-platform/low-code-plug-ins.md) | Description. |
| [Plugin monitoring](#) | Description. |

## Troubleshooting

If you encounter any issues or errors while using the Dataverse Accelerator, refer to the troubleshooting section of the documentation for guidance. Common issues and their resolutions are documented to help you resolve problems quickly and effectively.

## Frequently Asked Questions (FAQs)

1. **What is Dataverse Accelerator?**
   - Dataverse Accelerator is a toolkit designed to expedite the development process within the Microsoft Dataverse environment. It provides pre-built components, templates, and sample applications to help makers quickly deploy solutions tailored to common business scenarios.

1. **Who can use Dataverse Accelerator?**
   - Dataverse Accelerator is designed for Power Platform makers, developers, and organizations utilizing the Microsoft Dataverse platform for their applications and data management needs.

1. **What are the key benefits of using Dataverse Accelerator?**
   - Dataverse Accelerator offers several benefits, including accelerated development, enhanced data management capabilities, and customization options. It enables makers to deliver solutions more quickly while maintaining high standards of quality and efficiency.

1. **Is Dataverse Accelerator compatible with my existing Dataverse environment?**
   - Yes, Dataverse Accelerator is compatible with existing Power Platform environments that have Microsoft Dynamics enabled. It can be seamlessly integrated into your environment to enhance development capabilities without disrupting ongoing operations.

1. **How do I install Dataverse Accelerator?**
   - Follow the [install instructions](#) of this article to install the Dataverse Accelerator.

1. **How do I install Dataverse Accelerator?**
   - Follow the [install instructions](#) of this article to install the Dataverse Accelerator.

1. **Can I customize Dataverse Accelerator components to fit my specific requirements?**
   - Yes, Dataverse Accelerator provides extensive customization options. You can tailor existing components or create new ones from scratch to meet your organization's unique business needs and requirements.

1. **Is there a cost associated with using Dataverse Accelerator?**
   - The core components of Dataverse Accelerator are typically available at no additional cost for users with appropriate licenses for Microsoft Power Platform and Dataverse. However, additional costs may apply for certain advanced features or services.

1. **Where can I find support and resources for Dataverse Accelerator?**
   - See the section on [contacting help and support](./contacting-help-and-support) for instructions on getting support either with the features in the Dataverse Accelerator, or if you encounter problems using the application.

1. **How often is Dataverse Accelerator updated?**
   - Dataverse Accelerator is regularly updated to incorporate new features, improvements, and bug fixes. Major updates are announced based on the individual features, and will be indicated in the feature details.

## Contacting help and support

For issues with the Dataverse Accelerator solution installation or low-code plug-ins, such as errors received, [use the Help + support experience](/power-platform/admin/get-help-support) and include the following information:

- Problem Type: **Dataverse Web API and SDK**
- Problem Subtype: **Accelerator kit for Dataverse**