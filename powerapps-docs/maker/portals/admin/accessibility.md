---
title: Accessibility in Power Apps portals
description: Learn about making Power Apps portal accessible.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 06/0/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
    - carltoncolter
---
 
# Accessibility in Power Apps portals

Microsoft is committed to make products and services accessible to everyone. For more information about accessibility in general, go to the [Microsoft Accessibility](https://www.microsoft.com/accessibility) website.

> [!NOTE]
> Power Pages is also committed to accessibility for all. More information: [What is Power Pages](/power-pages/introduction).

## Accessibility standards

Power Apps portals conforms to global accessibility standards to help ensure accessibility. The following accessibility standards and conformance reports provide more details about accessibility with portals.

For more details about each of the follow accessibility standards, go to [Microsoft Accessibility Conformance Reports](https://cloudblogs.microsoft.com/industry-blog/government/2018/09/11/accessibility-conformance-reports/). In the **Search by Online Services** box, enter **power apps portals**, and then download the corresponding reports.

:::image type="content" source="media/accessibility/conformance-reports.png" alt-text="Search by Power Apps portals to download conformance reports.":::

### WCAG 2.1

[Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/) cover a wide range of recommendations for making web content more accessible. Following the guidelines will make content more accessible to a wider range of users, including accommodations for people with visual impairments, hearing loss, limited mobility, inability to speak, blindness and low vision, deafness and hearing loss, limited movement, photo sensitivity, and cognitive or developmental disabilities. These guidelines address the accessibility of web content on desktops, laptops, tablets, and mobile devices. In addition, following these guidelines can make web content more easily accessible to users in general.

Power Apps portals conforms to the WCAG 2.1 accessibility standard. For more details, download *W3C Web Content Accessibility Guidelines (WCAG) 2.1 Conformance Statement for Power Apps portals* from the [Microsoft Accessibility Conformance Reports](#accessibility-standards) website.

### US Section 508

The US General Services Administration (GSA) Office of Government-wide Policy (OGP) is tasked under [Section 508](https://www.section508.gov/) of the Rehabilitation Act to provide technical assistance to help Federal agencies comply with these requirements, and ensure that covered information and communication technology (ICT) is accessible to, and usable by, individuals with disabilities.

Power Apps portals conforms to the Section 508 guidelines defined by the US GSA. For more details, download *Section 508 report for portals* from the [Microsoft Accessibility Conformance Reports](#accessibility-standards) website.

### EN 301 549

[EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/02.01.02_60/en_301549v020102p.pdf) from the European Telecommunications Standards Institute (ETSI) provides an open, inclusive, and collaborative environment. This environment supports the timely development, ratification, and testing of globally applicable standards for ICT-enabled systems, applications, and services.

Power Apps portals conforms to ETSI EN 301 549. For more details, download *EN 301 549 Accessibility Declaration of Conformance for portals* from the [Microsoft Accessibility Conformance reports](#accessibility-standards).

## Creating an accessible portal

For a portal to be accessible, follow the [WAI-ARIA Authoring Practices 1.1](https://www.w3.org/TR/wai-aria-practices/) authoring practices.

### Customizing your portal and accessibility

When you customize your portal, you're responsible for meeting accessibility standards.

### Basic forms

A basic form (formerly known as an *entity form*) uses a model-driven Power Apps form to display a form on a webpage. Basic forms typically don't require a developer to design and configure; however, it might be helpful to involve a developer to extend some of the form features.

More information: [About basic forms](../configure/entity-forms.md)

### Basic form options

The controls included in a basic form are built to follow WCAG 2.1. The following options help make forms more accessible.

| **Name**                        | **Description**    |
|---------------------------------|----------|
| ToolTips Enabled                | The tooltip is set by using the description of the attribute on the target table. This setting adds the title attribute, providing screen readers with more information. The default value is false. |
| Enable Validation Summary Links | A Boolean value of true or false that indicates whether anchor links should be rendered in the validation summary to scroll to the field containing an error. The default value is true.          |

:::image type="content" source="media/accessibility/form-options.png" alt-text="Form Options menu.":::

More information: [Form options](../configure/entity-forms.md#form-options)

### Liquid templates and content snippets

When custom HTML and [Liquid](../liquid/liquid-overview.md) content are added to the portal, accessibility must be taken into consideration. The person making the changes to the Liquid templates and [content snippets](../configure/customize-content-snippets.md) is responsible for ensuring that the content they add is accessible. It's important to make sure that customizations adhere to the required policies, whether it be WCAG 2.1, US Section 508, or ETSI EN 301 549.

The [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/) provides a list of the WCAG requirements, with links to the full descriptions.

### Quick tips for accessible content

- Make sure a non-sighted or visually impaired person can do everything a sighted user can do.

- Test your portal by zooming in to 200 percent. Make sure the text is readable, and pages and controls function as expected. For more information, go to [WCAG 1.4.4](https://www.w3.org/WAI/WCAG21/Understanding/resize-text.html).

- Color contrast matters. Use a color contrast tool to help you see the contrast ratio. For more information, go to [WCAG 1.4.3](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html).

- Color shouldn't be the only visual way of conveying an action or information. If changing the color to highlight text, make sure the color or descriptive information is also available in the text. For more information, go to [WCAG 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html).

- Use the alt attribute for every image (IMG tag). Use an empty alt attribute to hide the image from screen readers. Ideally, you can use CSS to define decorative images hidden from screen readers. For more information, go to [WCAG C9](https://www.w3.org/WAI/WCAG21/Techniques/css/C9.html).

- Use the Microsoft [Accessibility Insights](https://accessibilityinsights.io/) tool to perform two types of scans:

    - [FastPass](https://accessibilityinsights.io/docs/web/getstarted/fastpass/): automatically checks for compliance with dozens of accessibility requirements.

    - [Assessment](https://accessibilityinsights.io/docs/web/getstarted/assessment/): measures compliance with WCAG 2.1 Level AA success criteria.

- Follow [WAI-ARIA Authoring Practices](https://www.w3.org/TR/wai-aria-practices/) while creating page layout and adding widgets.

- To go a step further, test your site by using the same accessibility tools as your users:

    - Use a screen reader, such as [Windows Narrator](https://support.microsoft.com/windows/chapter-1-introducing-narrator-7fe8fd72-541f-4536-7658-bfc37ddaf9c6#WindowsVersion=Windows_11).

    - Use [Immersive Reader](https://education.microsoft.com/resource/9b010288) in Microsoft Edge to make sure your portal is rendered and readable, making adjustments to the portal as needed.

## Microsoft accessibility features

Microsoft accessibility features help various agencies address accessibility requirements and conform to the standards laid out. More information: [Accessibility features of Microsoft products](https://sway.office.com/vAdiAMXOJEQGVbqX)

### See also

[Accessibility in Dynamics 365](/dynamics365/get-started/accessibility/)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
