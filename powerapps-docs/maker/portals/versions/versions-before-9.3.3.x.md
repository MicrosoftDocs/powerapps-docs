---
title: Power Apps portals versions before 9.3.3.x
description: Learn about the updates to Power Apps portals versions before 9.3.3.x, previously known as Dynamics 365 Portals.
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/26/2021
ms.subservice: portals
ms.author: dileeps
ms.reviewer: ndoelman
contributor:
    - nickdoelman
    - dileepsinghmicrosoft
---

# Power Apps portals versions before 9.3.3.x

In this article, you'll see a list of features added for Dynamics 365 Portals for versions earlier than 9.3.3.x. For more information on updates to Dynamics 365 Portals, see [portal capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/help/3181191).

> [!NOTE]
> Power Apps portals was earlier known as Dynamics 365 Portals.

## Dynamics 365 Portals version 9.1.4 for customer engagement apps

Dynamics 365 Portals version 9.1.4 for customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, and Dynamics 365 Project Service Automation) brought the following updates and features:

- **Maintenance mode for portal**: As a portal administrator, you can now configure your portal to display a proper message to customers whenever a maintenance activity is going on—for example, solution packages are being upgraded. More information: [Maintenance mode for a portal](../admin/enable-maintenance-mode.md)

- **Enable Power BI Embedded service**: As a portal customizer, you can now embed dashboards and reports created in the new workspace of Power BI by enabling Power BI Embedded service. The dashboards and reports are embedded on webpages in a portal by using the *powerbi* Liquid tag. More information: [Set up Power BI integration](../admin/set-up-power-bi-integration.md#enable-power-bi-embedded-service)

- **Enable content moderation on ideas**: As a portal administrator, you can now create a content moderation policy to moderate the ideas that are submitted on your portal.

- **OAuth 2.0 implicit grant flow**: As a portal developer, you can now make client-side API calls to external APIs and get them secured by using OAuth 2.0 implicit grant flow. More information: [OAuth 2.0 implicit grant flow](../oauth-implicit-grant-flow.md)

- **Dataverse starter portal (preview)**: As a portal administrator, you can now configure your portal to connect to the Dataverse environment and allow your users to interact with it. This feature brings in the ability to connect a portal to a Dataverse environment that does not have any customer engagement apps (Dynamics 365 Sales, Dynamics 365 Service, or Dynamics 365 Marketing) preinstalled.

## Dynamics 365 Portals version 9.1.1 for customer engagement apps

Dynamics 365 Portals version 9.1.1 for customer engagement apps brought the following new feature:

- **Portal checker**: You can now use portal checker to identify issues with your portal by looking at various configuration parameters and provide suggestions on how to fix them. More information: [Portal checker](../admin/portal-checker.md)

## Dynamics 365 Portals version 9.0.10 for customer engagement apps

Dynamics 365 Portals version 9.0.10 for customer engagement apps brought the following updates and features:

- **Migrate Dynamics 365 Portals configuration**: You can now migrate your Dynamics 365 Portals configuration from development to testing or the production environments. Migration involves exporting the existing configuration from the source Dynamics 365 instance, and then importing it into the target Dynamics 365 instance. To migrate configuration data, you need to use the Configuration Migration tool and a portal-specific configuration schema file. More information: [Migrate Dynamics 365 Portals configuration](../admin/migrate-portal-configuration.md)

- **Add Power BI visualization**: As a portal customizer, you can now embed Power BI visualizations (dashboard, reports, and tiles) on webpages in a portal by using the *powerbi* Liquid tag. More information: [Set up Power BI integration](../admin/set-up-power-bi-integration.md)

- **Restrict portal access by IP address**: As a portal administrator, you can now define a list of IP addresses that are allowed to access your portal. When a request to the portal is generated from any user, their IP address is evaluated against the allow list. If the IP address is not on the list, the portal displays a webpage with an HTTP 403 status code. More information: [Restrict portal access by IP address](../admin/ip-address-restrict.md)

- **Manage SharePoint documents**: Dynamics 365 Portals now supports uploading and displaying documents to and from SharePoint directly on a basic form or advanced form in a portal. This allows portal users to view, download, add, and delete documents from a portal. Portal users can also create folders to organize their documents. More information: [Manage SharePoint documents](../manage-sharepoint-documents.md)

- **New portal content editor (preview)**: In this preview, a new and simplified portal editor is available for customizers of Dynamics 365 Portals to reduce the learning curve on customization and increase their productivity.

- **Enable voting for status reasons**: By default, an idea is enabled for voting only when the Status Reason is set to New. You can now enable the voting on an idea for different status reasons. To enable voting for different status reasons, you must create the Ideas/EnableVotingForStatusReasons site setting and set its value to the required status reason values. 

## Dynamics 365 Portals version 9.0.6 for customer engagement apps

Dynamics 365 Portals version 9.0.6 for customer engagement apps brought the following updates and features:

- **Dynamics 365 Portals app**: The Dynamics 365 Portals app provides a new experience to configure and manage your online platform to communicate and collaborate with customers. When you install Dynamics 365 Portals version 9.0 and higher, the Dynamics 365 Portals app, built on the Unified Interface framework, is created out-of-the-box.

- **Reset a portal**: You can now reset a portal if you plan to move to another geolocation or to another tenant, and don't want to use the portal anymore. When you reset a portal, the hosted resources of the portal are deleted, and the portal URL will not be accessible. More information: [Reset a portal](../admin/reset-portal.md)

- **Change the base URL of a portal**: You can now change the base URL of a portal after it's provisioned. For example, if you choose contosocommunity.microsoftcrmportals.com as the base URL while provisioning the portal, you can later change it to contosocommunityportal.microsoftcrmportals.com as per your requirement. More information: [Change base URL](../admin/change-base-url.md)

## Dynamics 365 Portals version 8.4.1 for customer engagement apps

Dynamics 365 Portals version 8.4.1 for customer engagement apps brought in a bunch of bug fixes and performance improvements, along with the following features:

- **Search within attachment content of knowledge articles and web files**: Attachment content of knowledge articles and web files are now searchable to increase the likelihood of relevant search results. More information: [Search within file attachment content](../configure/search-file-attachment.md)
- **Accessibility**: The out-of-the-box portals (Community portal, Partner portal, Customer portal, Employee self-service portal) are now accessible. However, a customizer should ensure that the portal remains accessible after any customization or changes.

## Dynamics 365 Portals version 8.4 for customer engagement apps

Dynamics 365 Portals version 8.4 for customer engagement apps brought in a bunch of bug fixes and performance improvements, along with the following features:

- **Access portal error logs**: As a portal developer, you can now access detailed error logs for any issues on your portal. This helps you to debug the issues while developing the portal. Once your portal is live, you can configure the portal to send all application errors to an Azure Blob storage account owned by you. This will help you to debug the issues reported by your customers. More information: [Access portal error logs](../admin/view-portal-error-log.md)
- **Renew portal authentication key**: A portal connects to the Dataverse environment using Azure Active Directory (Azure AD) application. To do this, it requires an authentication key connected to Azure AD. This key is added when you provision your portal and it must be renewed every two years. This version of portals brings in the capability for administrators to be notified about key expiration and renew this key from the Power Apps portals admin center. More information: [Renew portal authentication key](../admin/manage-auth-key.md)
- **Implement General Data Protection Regulation in portals**: As a portal administrator, you can now configure your portal to meet the GDPR requirements. You can also provide certain terms and conditions that must be agreed upon by a user in order to use a portal. You can also set up checks; for example, if a portal is accessed by a minor user, the user must have parental consent to access the portal. Implementing GDPR allows obtaining consent from portal users regarding use of their personal data, identifying minor users, and obtaining parental consent for minor users. More information: [Implement GDPR in portals](../configure/implement-gdpr.md)

## Dynamics 365 Portals version 8.3 for customer engagement apps

Dynamics 365 Portals version 8.3 for the customer engagement apps brought the following updates and features:

- **Ability to include attachments with knowledge articles**: You can display note attachments along with knowledge articles. To enable this feature, create the site setting KnowledgeManagement/DisplayNotes and set the value to **true**. Portal users can also search for these attachments. More information: Display attachments with knowledge articles

  > [!Note]
  > Search for attachments can only be performed on the note's description and file attachment name. The content of the attached file is not searchable.
  
- **Administrative wizard to add a table to the portal**: This feature introduces a new administrative wizard to easily expose data on the portal. The table created through the wizard takes the data from your organization and makes a subset of it available to your portal customers, based on the security and permission model you choose.

- **Import metadata translation**: Use this feature to import the metadata translation of newly activated languages after you install a portal. More information: [Import metadata translation](../admin/import-metadata-translation.md)

- **Source code availability for portals**: A one-time release of Dynamics 365 Portals code is released to the Microsoft Download Center under MIT license for developers to download. This feature enables portals to be deployed to Dynamics 365 on-premises or online environments, and allows developers to customize the code to suit their specific business needs.

  > [!NOTE]
  > Source code is offered as a working sample and on an as-needed basis. No direct support will be provided for any modifications to the code.

- **Single sign-on (SSO) configuration improvements and support for Azure Active Directory B2C (Azure AD B2C)**: For portals that require a consumer-based sign-in, this feature now supports the ability to:
  - Configure your portal authentication to use SSO 
  - Support Azure AD B2C for customer authentication
  - Manage your portal security in Azure

  More information: [Azure AD B2C provider settings for portals](../configure/azure-ad-b2c.md)

- **Support timezone-independent date formats in portals forms**: This feature adds support for **Date Only** and **Timezone Independent** behaviors for date/time fields. More information: [Behavior and format of the date and time field](../configure/behavior-format-date-time-field.md)

- **Allowing non-global administrators to provision a portal**: You can now provision a portal if you're assigned to the System Administrator role of the CRM organization selected for the portal. You can also manage an existing portal, if you have any of the following roles:
  - Dynamics 365 admin
  - System Administrator of the CRM organization selected for the portal

- **Store the custom domain name for a portal**: This feature stores the primary domain name of a portal on the website record. If the domain name is changed in the future, the latest primary domain name will be stored.

- **Tracking cookie for portals**: A persistent cookie, Dynamics365PortalAnalytics, will be set whenever a user goes to a portal. This cookie has an expiration of 90 days. This cookie does not store any of the user's personal data and is used by Microsoft to collect analytics about portal service. Please read the Microsoft online services privacy statement [here](https://go.microsoft.com/fwlink/p/?linkid=856855).

- **Performance improvement of header and footer on a portal**: Two new site settings—Header/OutputCache/Enabled and Footer/OutputCache/Enabled—are added to enable header and footer output caching when these settings are set to true. For new users, these site settings are set to true by default, thereby enabling header and footer output caching. For existing users who upgrade to a newer version of Dynamics 365 Portals, output caching is disabled by default. It means that the Header and Footer web templates are parsed and rendered on every page load. To enable output caching, they must update the appropriate web templates and create the required site settings. More information: [Enable header and footer output caching](../configure/enable-header-footer-output-caching.md)

## December 2016 updates

The December 2016 update brought many new features to Dynamics 365 Portals. These updates allowed for better interactions among companies, partners, and customers, and made the experience of navigating the portal faster and easier. Some of the major updates included:

- **Multiple-language support:** Support customers from multiple regions by using a single portal. More information: [Enable multiple-language support](../configure/enable-multiple-language-support.md)
- **East Asian language support:** Support for multiple-byte languages such as Japanese, Chinese, and Korean.
- **Faceted search:** New filters improve how quickly customers can find the content they're looking for while granting more control over the visibility of content. More information: [Faceted search](../configure/improve-portal-search-faceted-search.md)
- **Product filtering:** Portal users can trim access to knowledge articles related to their product ownership to avoid information overload.
- **Content access levels:** A new level of ownership associated with a portal contact, account, or web role can be used to control access to knowledge articles to help target the right article at the right audience and prevent irrelevant articles from surfacing. More information: [Content access levels](/dynamics365/portals/manage-knowledge-articles-content-levels)
- **Knowledge article reporting enhancement:** The portal tracks where a knowledge article was used in the portal.
- **Project Service Automation integration:** Provide access and visibility for active and closed projects across all stages of a project lifecycle to partners and customers. Team members, reviewers, and customers can view project status, quotes, order forums, and bookable resources on the portal with this solution. More information: [Integrate Project Service Automation](/dynamics365/portals/integrate-project-service-automation)
- **Field Service integration:** Expose information about active agreements, assets, work orders, invoices, and support cases to partners and customers on the portal with this solution. More information: [Integrate Field Service](/dynamics365/portals/integrate-field-service)
- **Partner onboarding:** Recruit new partners for better customer sales and service experiences. Potential partners can apply for partner status through the portal.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e)

