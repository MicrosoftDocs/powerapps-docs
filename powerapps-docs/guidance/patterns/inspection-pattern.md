---
title: "Power Apps pattern: Inspection"
description: Discover how Power Apps enables efficient and actionable inspections for industries like aviation, education, and healthcare.
#customer intent: As a Power Apps maker, I want to learn how to use Power Apps to create inspection solutions so that I can streamline inspection processes in my organization.
author: kathyos
ms.topic: concept-article
ms.custom: guidance
ms.date: 02/20/2026
ms.subservice: guidance
ms.author: kathyos
ms.reviewer: kathyos
---

# Pattern: Inspection

Organizations need to perform inspections for many reasons. Microsoft Apps provides a no-code or low-code solution for enabling inspection, analysis, and action. In this pattern, an app user fills out a structured assessment, which is then uploaded to a centralized location for analysis, reporting, and potential action. You might call this process an audit, an inspection, quality control, taking inventory, a checkup, a checklist, or something similar.  

This article provides real-world examples of how customers use Microsoft Apps to create timely, efficient, and actionable inspections, from aircraft maintenance to elementary schools.

## How to recognize the inspection pattern

:::image type="content" source="media/inspection-illustration.png" alt-text="Screenshot of the inspection pattern illustration showing record, aggregate, and decide/act/report steps.":::

In a typical inspection scenario:

1. Someone (for example, an employee or a customer) fills out a standardized checklist or form, and submits it. This step might happen on a recurring basis, such as a daily quality check, a monthly inventory, or a scheduled checkup. You can collect data from the public, such as crowd-sourced vandalism reporting.

1. Then, typically in a centralized function, all the answers are aggregated for review or reporting.

    For example, you might report on how many vehicles require maintenance, or the history of a vehicle's status over the last year.

1. Often, an inspection results in needing to take action.

    For example, you might see that a vehicle fails its inspection and decide to take it out of service. Or the centralized report might show that daily maintenance standards need to be improved in a particular location.

## Template: Inspection solution for Microsoft Teams

The Inspection solution for Microsoft Teams is a general inspection app that can be used to inspect anything from a location (such as a retail store or manufacturing plant) to assets and equipment (such as vehicles and machines). The solution includes an app for performing inspections and an app for configuring and managing inspections.

:::image type="content" source="media/review-inspection.png" alt-text="Screenshot of the Inspection app for Microsoft Teams.":::

Learn more about the solution: [Video](https://aka.ms/TeamsInspectionVideo) |  [Sample app template](https://github.com/microsoft/teams-powerapps-app-templates/tree/main/Inspection)

## Template: Hospital Emergency Response sample solution

The Hospital Emergency Response sample solution provides a set of capabilities for healthcare organizations to collect data for situational awareness of available beds and supplies, COVID-19–related patients, staffing, and pending discharges. This solution implements the inspection pattern by collecting an inventory of available hospital beds and supplies. It also uses dashboards to summarize key data and insights for users to make informed decisions, resulting in efficient deployment and usage of resources.

:::image type="content" source="media/hospital-emergency-response-app.png" alt-text="Screenshot of the Hospital Emergency Response app.":::

The main components of the Hospital Emergency Response solution are:

- **Mobile app for frontline staff**: Frontline staff, such as nurses and medical practitioners, can use the mobile app to quickly view and enter information as required.

- **Web app for hospital admins**: Hospital admins can use this app to add and manage system data required for the solution to work.

- **Dashboards for healthcare decision makers**: Decision makers can use dashboards to quickly view important data and metrics to help make decisions efficiently.

Learn more about the solution: [Video](https://youtu.be/Dg-i3F9G01I) |  [Blog post](https://www.microsoft.com/power-platform/blog/power-apps/emergency-response-solution-a-microsoft-power-platform-solution-for-healthcare-emergency-response-2)

## How customers are using the inspection pattern

Customers across industries are using the inspection pattern to streamline processes, ensure safety, and make informed decisions.

### Virgin Atlantic safety and compliance app

Virgin Atlantic uses Power Apps to do a safety and compliance audit for their aircraft. Aircraft engineers use a simple Power Apps canvas app on their mobile devices, with preloaded checklists to perform ad-hoc and scheduled inspections.

[Read the whole story.](https://www.microsoft.com/power-platform/blog/power-apps/virgin-atlantic-drives-agile-wins-for-mobile-workforce-with-the-power-platform)

Aircraft engineers use a canvas app on their corporate iPads to perform ad-hoc and scheduled inspections. They can view what audits are scheduled for them and review audit questions. After an inspection is completed, expected answers are highlighted in green to provide a visual aid. Unexpected answers are highlighted in red and followed up with a prompt, which the engineer can use to record a finding
and assign a follow-up task to a manager.

:::image type="content" source="media/virgin-atlantic-aircraft-inspection.png" alt-text="Screenshot of the Virgin Atlantic safety and compliance audit app.":::

Engineering compliance managers use a Power Apps canvas app integrated within a SharePoint list to review completed inspections and view all inspection findings. They can also generate HTML and PDF inspection summaries from the app if an inspector or executive requires further information.

:::image type="content" source="media/virgin-atlantic-audit-summary.jpg" alt-text="Screenshot of the engineering compliance manager view showing Power Apps running embedded in SharePoint.":::

### Standard Bank ATM inspection app

The Cash Tribe team in Retail Banking South Africa was responsible for 8,000 ATMs. They needed to perform manual inspections of these ATMs regularly to identify problems&mdash;such as vandalism, broken screens, and dirty surroundings&mdash;that weren't flagged through automated alerts. The inspections were done on a clipboard and the team was buried in reams of paperwork.

[Read the whole story.](https://www.microsoft.com/power-platform/blog/power-apps/standard-bank-south-africa-creates-a-center-of-excellence-for-the-power-platform)

With Microsoft Power Platform, Standard Bank was able to build a mobile app for inspecting ATMs. Over 300 inspectors use the Power Apps canvas app to generate over 5,000 inspection reports each month. The app uses the device GPS capabilities to find nearby ATMs and the device camera to take pictures when issues need to be reported.

:::image type="content" source="media/standard-bank-atm-app-blurred.png" alt-text="Screenshot of the Standard Bank ATM inspection app.":::

[Watch a demo of the ATM inspection.](https://youtu.be/-JRUIA8ItWE?t=1469)

An important part of the inspection pattern is the ability to review the collected data. For this app, the data is stored in SharePoint Online lists, which is their central data repository to enable business intelligence to aid in future improvements. Power BI dashboards and reports are used to visualize the aggregate data.

:::image type="content" source="media/standard-bank-atm-audit.jpg" alt-text="Screenshot of the Standard Bank ATM inspection app dashboards and reports.":::

### Tacoma Public schools reading assessment

[Read the whole story.](https://www.microsoft.com/power-platform/blog/power-apps/assistant-principal-builds-power-platform-solution-to-improve-reading-assessments)

[Watch a video.](https://www.youtube.com/watch?v=v5xWpOT1V78)

Schools in Tacoma, Washington, use the Developmental Reading Assessment, 2nd Edition (DRA2), in which teachers read with students to assess their reading level and abilities. Teachers systematically observe, record, and evaluate how a student's reading performance changes over time. They use this data to set reading goals for the student.

Rather than filling out paper forms as before, teachers now access this app from their mobile device or Surface tablets provided by the school. Teachers use the app to enter detailed information from each student's reading assessment, such as oral reading goals and comprehension goals.

:::image type="content" source="media/tacoma-schools-dra-app.png" alt-text="Screenshot of the Tacoma Public Schools DRA2 app.":::

### More stories

- [Pinnacle Group – Helpdesk employee leads transition from paper to digital](https://www.microsoft.com/power-platform/blog/power-apps/pinnacle-group/)
- [Kelly Roofing uses Power Apps to capture photos at work sites](https://www.microsoft.com/power-platform/blog/power-apps/kellyroofing/)
- [G & J Pepsi – G&J Pepsi pours in-house expertise into perfect apps with low-code Power Apps driven by Power Automate](https://www.microsoft.com/customers/story/821738-gj-pepsi-cola-bottlers-consumer-goods-microsoft-power-platform)
