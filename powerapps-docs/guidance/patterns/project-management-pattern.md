---
title: "Power Apps pattern: Project Management | Microsoft Docs"
description: Learn how project management apps help you manage projects to ensure teams achieve their goals and meet success criteria as planned.
author: Vasavib
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 12/10/2020
ms.author: vabhavir
ms.reviewer: kathyos
---

# Pattern: Project management

![Collage of project management app screenshots](media/project-management-collage.jpg "Collage of project management app screenshots")

Organizations need a central place to manage multiple projects as they ensure
various teams achieve their goals and meet success criteria as planned.

A few common use cases for Project Management include managing new product
ideas, project plans and milestones, team performance management and so on.

Power Platform provides a no-code, low-code solution for organizations to create
easy-to-use solutions to manage the lifecycle of projects. This article provides
several real-world examples of how customers have used Power Platform to create
efficient project management applications and workflows.

## How to recognize the project management pattern

![Illustration of the project management pattern with plan, track, and review steps](media/project-management-illustration.png "Illustration of the project management pattern with plan, track, and review steps")

Business groups within organizations see the need for a tool to manage projects,
track progress, and monitor outcomes.

In a typical scenario:

1. Plan your work to manage ideas, project plans, tasks, and milestones.

2. Track progress against the plan, notify, and escalate if needed.

3. Review progress, monitor outcomes and visualize key aspects of the progress.

## How customers are using the project management pattern

### Custom Air Products & Services, Inc., Traveler App

[Read the whole
story.](https://powerapps.microsoft.com/blog/custom-air-products-services-manages-hvac-manufacturing-process-using-the-power-platform/)

Custom Air Products & Services, Inc. (CAPS) is a Houston-based provider of
heating, air conditioning, and ventilation (HVAC) solutions that specializes in
the design, construction, installation, modification, and servicing of air
conditioning equipment in both the industrial and commercial segments of the
HVAC industry.

The CAPS Project Management (PM) team needed a customized solution to track the
entire lifecycle of HVAC units as they passed through the manufacturing process,
with a focus on quality construction. The solution needed to be customized to
meet the needs of each department and to track quality checks and allow for
respective owners to sign off on each stage in the process. Moreover, they
wanted to empower anyone in the organization to report on issues via their
mobile devices. One of the key problems they were facing was the “traveler”
document - a paper document used to track quality checks - getting lost.

The following diagram represents the process that needed to be digitized and
automated:

![Flowchart of the sign-off process](media/CAPS-flowchart.png "Flowchart of the sign-off process")

Rebecca Sackett, a Data Analyst Assistant, who found Power Apps in her Office
365 subscription and began experimenting with creating apps against SharePoint
lists to replace manual processes, built the Power Apps solution to digitize the
“traveler” document. The app was called “CAPS Traveler.” The main Traveler
management app allows PMs and stakeholders to view all active projects, view a
set of key statistics, and manage the testing and shipping calendars.

![Screenshot of CAPS Traveller app calendar view](media/CAPS-traveller-calendar.png "Screenshot of CAPS Traveller app calendar view")

PMs initiate projects and add details for each required step, such as – Fab,
Paint, Electrical, Testing, etc. Personnel from each department then use a
companion mobile app that is custom built with specific questions for their
department. Later, the central team collates the data and uses the reports to
identify common reasons why a particular step wasn’t done.

![Screenshot of CAPS customized Sign-Off app](media/CAPS-signoff-app.png "Screenshot of CAPS customized Sign-Off app")

 *Customized sign-off app for the Electrical team, one of ten such
customized companion apps*

There are ten such sign-off apps in addition to the main management app that all
read and write data to the same set of SharePoint lists. Once all the steps are
completed, someone in the Quality Control (QC) team performs a final sign-off. A
Flow is then automatically triggered to generate a PDF report (see Flow section
below).

![Screenshot of flows used to create the final report, and the report itself](media/CAPS-pdf-report.png "Screenshot of flows used to create the final report, and the report itself")

### Environment Canterbury INZONE App

[Read the whole story.](https://powerapps.microsoft.com/blog/environment-canterbury-speeds-up-outcome-tracking-with-the-power-platform/)

Environment Canterbury (ECan) works in partnership with the communities of
Canterbury on long term environmental outcome programs that consist of multiple
milestones and related projects and they needed an affordable solution that
would provide greater consistency across projects, higher levels of visibility,
and quicker access to data.

Using an app, Zone Managers and project participants view their projects’
status. All projects are tagged with the zone and specific milestones, and all
milestones are tagged with the long-term outcomes. The app provides a customized
color scheme, which makes it easy to differentiate and navigate between
projects, milestones, and outcomes. All screens for projects are green,
milestones are blue, and outcomes are orange.

![Screenshot of InZone app](media/environment-canterbury-inzone-app.png "Screenshot of InZone app")

Notifications are sent to prompt data updates and provide escalations if
projects are not updated at the required time. The flows are also used to call
specific views and generate HTML table-based digest emails listing all items
relating to a specific person in a single email.

![Screenshot of the flows that generate various emails](media/environment-canterbury-email-flows.png "Screenshot of the flows that generate various emails")

### Partners In Health Gift Review App

[Read the whole story.](https://customers.microsoft.com/story/775258-partners-in-health-nonprofit-power-apps)

Partners In Health (PIH) relies on its individual donors for about half of its
funding each year, while the other half comes mainly from government grants,
corporations, and foundations. The nonprofit has about 10 gift officers who are
responsible for stewarding its 1,000+ most generous individual donors. PIH
wanted to improve gift officers’ abilities to manage their portfolios by
showing them gifts as they arrive and by giving officers a 360-degree view of
their donor portfolios.

Bella Chih-Ning, Analytics and Applications Manager at PIH built a Gift Review
app and dashboard for gift officers to manage and visualize many aspects of
donations. With the Gift Review App, gift officers could view donations
immediately as they come in, add relevant notes, and ensure the donations are
assigned to the appropriate fund. This creates a To-Do List checklist where the
gift officer reviews the donation to ensure it is assigned to the appropriate
campaign, coded to the correct gift type, and assigned to the right fund. The
gift officer can email questions to the PIH DevOps team directly within the app.
Once everything is clear, the gift officers mark the checklist as “done,” which
becomes visible to their managers.

![Screenshot of Partners in Health gift review app](media/partners-in-health-gift-review-app.png "Screenshot of Partners in Health gift review app")

![Screenshot of Partners in Health gift editing screen](media/partners-in-health-edit-gift.png "Screenshot of Partners in Health gift editing screen")

*Gift Review App donor gift, To-Do List status, and overlay screen for updating
with actions completed*

*“The App in a Day training really opened my eyes to how easy it can be to build
tools that streamline processes and empower our colleagues to be better at their
jobs,” says Bella Chih-Ning*

### R3 Retail Project Management Solution

[Read the whole story.](https://customers.microsoft.com/story/809496-r3-retail-development)

The company R3 Retail Development provides deep expertise in project management
consulting to maximize profits for supermarket, grocery, food processing,
commercial, retail, and small industrial customers across the United States. R3
needed a highly customized approach for its end-to-end project management needs.

The Project Portfolio app was built within just 120 hours and now manages more
than 200 projects. R3 project managers and the regional store managers that they
serve now use the new Project Portfolio app. The app has a rich set of
capabilities that include:

- A dashboard that displays summary stats based on the signed-in user.

- Project tracking information including dates, tasks, issues, purchase
    orders, and people.

- IP address tracking for all installed devices, such as refrigerators.

- File-uploading capabilities for documents like architectural files for HVAC
    systems.

- Extensive custom business logic, such as automatically setting date values
    based on status entries.

![Screenshot of R3 project dashboard](media/r3-project-dashboard.png "Screenshot of R3 project dashboard")

*Project Details interface with milestones, statuses, due dates, tasks, issues,
and team members; for larger versions of all the figures in this story plus
additional Project Portfolio app screenshots, go to the Downloads section in the
left-hand sidebar*

Administrators can assign security clearances to specific app users according to
their roles. Administrators can also configure the list of task types and
the expected time for each task, which in turn is used to generate due dates
automatically.

![Screenshot of R3 role management screen and key stats dashboard](media/r3-role-management.png "Screenshot of R3 role management screen and key stats dashboard")

*Project Portfolio app's user management interface and key stats dashboard*

R3 uses [Power Automate](https://flow.microsoft.com/) to send automated
notifications and reminders. All data is stored in Microsoft Dataverse.

### Capitol Music Group Scheduling tools

[Read the whole story.](https://customers.microsoft.com/story/768079-capitol-records-media-entertainment-power-platform)

Capitol Music Group (CMG) saw an opportunity to modernize its marketing workflow
and scheduling tools, previously built using InfoPath. A business-critical app
managed schedules for new releases, and over time, evolved to capture data for
different types of releases and media. CMG wanted to automate routine processes,
broaden visibility and collaboration between partner labels, and adapt faster to
new marketing channels online. But its Capitol Scheduling app had become deeply
integrated into its process flows and consisted entirely of XML data that
required a lot of tribal knowledge to manage. Wanting a streamlined, low-code
approach to app development and management, CMG ultimately decided to migrate
its app from InfoPath to Microsoft Power Platform, including Power Apps and
Power Automate.

Capitol wanted their teams to use the new scheduling interface to easily
communicate, get approvals, and collaborate on marketing for different types of
releases—be it the physical, digital, or video side of things.

*“With Microsoft Power Platform, Capitol has an easy way to share marketing
information across the whole product life cycle. It even helps them facilitate
and streamline cross-label projects.” says Karen Reali, Senior Manager,
Universal Music Group*
