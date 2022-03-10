---
title: Accessibility in Power Apps portals
description: Learn about making Power Apps portal accessible.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 03/10/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
---
 
# Accessibility in Power Apps portals

Microsoft is committed to make products and services accessible to everyone. For more information about accessibility in general, go to [Accessibility](https://www.microsoft.com/accessibility).

## Accessibility standards

Power Apps portals conforms to global accessibility standards to ensure the accessibility to everyone. The following accessibility standards and conformance reports provide more details about accessibility with portals.

For more details on each of the follow accessibility standards, you can download the related documents from [Microsoft Accessibility Conformance Reports](https://cloudblogs.microsoft.com/industry-blog/government/2018/09/11/accessibility-conformance-reports/).

Enter *power apps portals* in the **Search by Online Services** and then download the corresponding reports.

:::image type="content" source="media/accessibility/conformance-reports.png" alt-text="Searching by Power Apps portals and being able to download conformance reports.":::

### WCAG 2.1

[Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/) covers a wide range of recommendations for making web content more accessible. Following the guidelines will make content more accessible to a wider range of people with disabilities, including accommodations for blindness and low vision, deafness and hearing loss, limited movement, speech disabilities, photo sensitivity, and combinations of disabilities, and some accommodation for learning disabilities and cognitive limitations; but won't address every user need for people with these disabilities. These guidelines address accessibility of web content on desktops, laptops, tablets, and mobile devices. Following these guidelines will also often make Web content more usable to users in general.

Power Apps portals conforms to the WCAG 2.1 accessibility standard. For more details, download the **W3C Web Content Accessibility Guidelines (WCAG) 2.1 Conformance Statement for Power Apps portals** from the [Microsoft Accessibility Conformance reports](#accessibility-standards).

### US Section 508

The U.S. General Services Administration (GSA) Office of Government-wide Policy (OGP) is tasked under [Section 508](https://www.section508.gov/) of the Rehabilitation Act to provide technical assistance to help Federal agencies comply with these requirements, and ensure that covered ICT is accessible to, and usable by, individuals with disabilities.

Power Apps portals conforms to the Section 508 guidelines defined by the U.S. GSA. For more details, download the **Section 508 report for portals** from the [Microsoft Accessibility Conformance reports](#accessibility-standards).

### EN 301 549

[EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/02.01.02_60/en_301549v020102p.pdf) from ETSI provides an open, inclusive and collaborative environment. This environment supports the timely development, ratification and testing of globally applicable standards for ICT-enabled systems, applications and services.

Power Apps portals conforms to the ETSI. For more details, download the **EN 301 549 Accessibility Declaration of Conformance for portals** from the [Microsoft Accessibility Conformance reports](#accessibility-standards).

## Creating an accessible portal

For a portal to be accessible, use the [WAI-ARIA Authoring Practices 1.1](https://www.w3.org/TR/wai-aria-practices/) authoring practices.

### Customizing your portal and accessibility

When you customize your portal, you're responsible for meeting accessibility standards.

### Basic forms (entity forms)

A basic form allows a model-driven Power Apps form to be used on the Power Portal. Basic forms typically don't require a developer to design, but depending on portal's form requirements, a developer may be helpful.

More Information: [About Basic Forms](../configure/entity-forms.md)

### Basic form options

The included Basic Form controls are built to follow [WCAG 2.1](https://www.w3.org/TR/WCAG21/). There are options that help make forms more accessible:

| **Name**                        | **Description**                                                                                                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ToolTips Enabled                | The tooltip is set using the description of the attribute on the target table. This setting adds the title attribute, providing screen readers with more information. Default value is false. |
| Enable Validation Summary Links | A boolean value of true or false that indicates whether anchor links should be rendered in the validation summary to scroll to the field containing an error. Default value is true.          |

:::image type="content" source="media/accessibility/form-options.png" alt-text="form options menu":::

More Information: [Form Options](../configure/entity-forms.md#form-options)

### Liquid Templates and Content Snippets

When custom html and liquid content are added to the portal, accessibility must be taken into consideration. The person making the changes to the liquid template and content snippets is responsible for ensuring the content they add is accessible. It's important to make sure the customizations adhere to the required policies, whether it be [WCAG 2.1](#wcag-21), [US Section 508](#us-section-508), and/or [ETSI EN 301 549](#en-301-549).

The [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/) provides a list of the WCAG requirements, with links to the full descriptions.

### Quick Tips for Accessible Content

1. Make sure a non-sighted or visually impaired person can do everything a sighted user can do.

1. Test your portal by zooming in to 200%, make sure the text is readable, the pages function and work, etc. For more information, see: [WCAG 1.4.4](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG21%2FUnderstanding%2Fresize-text.html&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591078718%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=7dwyo3J%2F7tC5ykGjHWYo%2FUb7mTSi7AFQ10ypb80wgFU%3D&reserved=0)

1. Color contrast matters.  Use a color contrast tool to help you see the contrast ratio. For more information, see: [WCAG 1.4.3](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG21%2FUnderstanding%2Fcontrast-minimum.html&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591078718%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=%2BYu2bmqn991ZMrtVBsquQ2TW1cazwBvSToKf8iyjwds%3D&reserved=0)

1. Color shouldn't be the only visual way of conveying an action or information. If changing the color to highlight text, make sure the color or descriptive information is also available in the text. For more information, see: [WCAG 1.4.1](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG21%2FUnderstanding%2Fuse-of-color.html&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591078718%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=wITEX%2BDM%2Bp4A6umK%2BCF4RjRAQu%2FMN4FAWnKFtlVh2wk%3D&reserved=0)

1. Use the alt attribute for every image (img tag). Use an empty alt attribute to hide the image from screen readers. Ideally, use CSS to define decorative images hidden from screen readers. For more information, see: [WCAG C9](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG21%2FTechniques%2Fcss%2FC9.html&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591078718%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=NdvmiSQDPg0AoniEyKo2xTxdlSyP8pNaM0NLfBRJTmQ%3D&reserved=0)

1. Use the Microsoft Tool, [Accessibility Insights](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Faccessibilityinsights.io%2F&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591078718%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=%2F3DRWtlql3YNpTRP%2BBh%2FRrQbnvcqphp0TpJ2bI6oGZI%3D&reserved=0) to perform two types of scans:

    - [FastPass](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Faccessibilityinsights.io%2Fdocs%2Fen%2Fweb%2Fgetstarted%2Ffastpass%2F&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591078718%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=v9Ni30%2FGosSEe5Tmcf35FVrnBrrKrLn24ecRowPR%2FQo%3D&reserved=0): automatically checks for compliance with dozens of accessibility requirements.

    - [Assessment](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Faccessibilityinsights.io%2Fdocs%2Fen%2Fweb%2Fgetstarted%2Fassessment%2F&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591128708%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=iuCLSsz1XhTEjqzrZIZkSIvWjzpKaWOGQJbM0JX2PGY%3D&reserved=0): measures compliance with WCAG 2.1 Level AA success criteria.

1. Follow [WAI-ARIA Authoring Practices](https://www.w3.org/TR/wai-aria-practices/) while creating page layout and adding widgets.

1. To go a step further, test your site using the same accessibility tools as your users:

    - Use a screen-reader, such as [Windows Narrator](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.microsoft.com%2Fen-us%2Fwindows%2Fchapter-1-introducing-narrator-7fe8fd72-541f-4536-7658-bfc37ddaf9c6%23WindowsVersion%3DWindows_11&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591128708%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=84IQXrWI9NiMj79ESaayvhsVobSv%2BNOPNzhTIZWDaOg%3D&reserved=0).

    - Test using the [Immersive Reader](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Feducation.microsoft.com%2Fen-us%2Fresource%2F9b010288&data=04%7C01%7CNeeraj.Nandwana%40microsoft.com%7Cdf0b316568b14277b61808d9e1a0ecc8%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637788903591128708%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=aLsTp6MsE6qLNpY3FYC7vPmSuYeov%2F7n9nzCSalE2tE%3D&reserved=0) in Edge to make sure your portal renders and is readable, making adjustments to your portal as needed.

## Microsoft accessibility features

Microsoft accessibility features help various agencies address accessibility requirements and conform to the standards laid out. More information: [Accessibility features of Microsoft products](https://sway.office.com/vAdiAMXOJEQGVbqX)

### See also

[Accessibility in Dynamics 365](/dynamics365/get-started/accessibility/)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]