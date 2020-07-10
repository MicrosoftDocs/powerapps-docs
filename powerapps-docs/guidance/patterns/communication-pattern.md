---
title: "Pattern: Communication / Announcement"
---


# Pattern: Communication

![Collage of communication app screenshots](media/communication-collage.png "Collage of communication app screenshots")

Want to quickly share news, event announcements, and the latest up-to-date info
with your employees no matter where they are? A common use of Power Platform is
to provide highly tailored and visually compelling communications via an app.
For example, Telstra sends all communications to its field engineers directly
within the Field Technician app. This document provides several examples of
real-world use cases that showcase organizations using Power Platform to
communicate information to employees.

## How to recognize the Communication/Announcement pattern

![Illustration of the communication pattern with compose, publish, and consume steps](media/communication-illustration.png)

In a typical communication scenario:

1. A communication team creates information to be published to the
    organization.

    - For example, an HR department might share news across the organization.

    - Or a field services team could create field technician bulletins.

1. Information is published to employees.

    - This could be on a regular basis like daily news or weekly newsletters,
        occasional announcements of events such as training, or urgent
        communication with important news during an emergency.

    - An app can use a push or pull model to get the latest information from
        the cloud.

1. Employees consume the communication.

    - The communications app keeps all relevant information in one place.

    - The communications app can also enable employees to take action, such as
        signing up for a training or event directly from an announcement.

    - The organization can run analytics on how many employees opened and read
        a communication, to learn what works best for their team.

## Template: Microsoft Crisis Communication app

The Crisis Communication app is a template that connects users with information
during a crisis. You can quickly get updates on internal company news, answers
to frequently asked questions, and access to important information like links
and emergency contacts.

The solution combines capabilities of Power Apps, Power Automate, Teams, and
SharePoint. It can be used on the web, mobile or in Teams.

Key features include:

- Employees can get information, report their work status (e.g., working from
    home), and make requests. This helps managers coordinate across their teams
    and helps central response teams track status across an organization.

- Admins can use the app to push news, updates, and content specific to their
    organization, and can provide emergency contacts specific to different
    locations.

- The app includes the ability to add RSS feeds of up-to-date information from
    reputable sources such as WHO, CDC, or a local authority.

The Crisis Communication Admin app enables the admin to compose news and
information as well as configure the features of the employee app.

![A screenshot of the Microsoft Crisis Communication admin app](media/crisis-communication-admin-app.png "A screenshot of the Microsoft Crisis Communication admin app")

The employee app, which can be embedded in Teams, enables users to consume news
and information, as well as reach out for assistance.

![A screenshot of the Microsoft Crisis Communication employee app](media/crisis-communication-employee-app.jpg "A screenshot of the Microsoft Crisis Communication employee app")

[Watch a video demo of the Crisis Communication
solution](https://youtu.be/23SypLXiOTw) and [Set up and learn about the Crisis
Communication sample
template](https://docs.microsoft.com/powerapps/maker/canvas-apps/sample-crisis-communication-app)

## How customers are using the Communication pattern

### Schlumberger Coronavirus Stay SAFE app

[Read the whole story](https://powerapps.microsoft.com/blog/schlumberger/)

For Schlumberger, the health and safety of their employees and contractors is
its first priority. Schlumberger’s Health, Safety and Environment (HSE) function
came together at the very early stages of the COVID-19 virus outbreak to raise
awareness and educate employees on preventative measures.

Schlumberger developed a Power Apps solution called “Coronavirus Stay SAFE” to
provide timely updates to their highly mobile workforce. The app enabled rapid
dissemination of important and relevant information from official health
organizations like the WHO and the CDC, as well as company-specific information.
The app is a single source of truth and a reference for preventive measures to
minimize exposure.

![Some screenshots of the Schlumberger Stay SAFE app](media/schlumberger-stay-safe-app-1.png "Some screenshots of the Schlumberger Stay SAFE app")

![Some screenshots of the Schlumberger Stay SAFE app](media/schlumberger-stay-safe-app-2.png "Some screenshots of the Schlumberger Stay SAFE app")

### Telstra Technician Plus app

[Read the whole
story](https://customers.microsoft.com/story/765534-telstra-telecommunications-teams)

Telstra, a leading Australian telecommunications company, was using a number of
resources over the years, such as online spreadsheets, paper documents, emails,
and websites to support the needs of field technicians to properly server their
customers. The company realized they needed a modern, mobile source of knowledge
and communication for the field employees.

Using Power Platform, the Field Digitization Team at Telstra built the
Technician Plus app for their field technicians, with role-specific applications
that aid in many of the tasks vital to field work and field management. The
solution also includes a news feed, a Telstra product catalogue that enables
upselling opportunities in the field, and instructional video and podcast hubs.
The solution is used by leaders to efficiently send communications out to the
field.

See the solution in this video:
<!--TO EDITOR: The author would like the thumbnail to be a hyperlink to the video but we don't know how to achieve that. -->
![A thumbnail of the Telstra video](media/telstra-video-thumbnail.png)(https://mymbas.microsoft.com/sessions/a00b1455-2989-4eb6-b17d-e182a27183a1?source=sessions)

### Hexion app to manage company-wide communications

[Read the whole story](https://customers.microsoft.com/story/810656-hexion-manufacturing-power-platform)

At global chemical company Hexion, managers and the communications department
were sending email widely throughout the company. They needed to target
predefined groups of people and require approval of communications before
distributing them. In this case, Power Platform is used to compose and publish
communications that are consumed in email and Teams.

The IT team in Hexion used Power Apps to build a new Broadcaster app with richer
capabilities than its previous legacy tool and a lower support cost. The app is
now used by the communications lead to broadcast company-wide messages in email
and Teams, and they plan to roll out to all major project team leaders. The
app’s key capabilities and benefits include:

- Authoring of emails with dynamic previews of the formatted versions.

- Authoring focuses on the content while the tool manages branding and layout.

- Ability to send a test email before sending the final communication.

- Targeting of predefined groups of users.

- Picking the author on whose behalf the email is sent and having their
    signature automatically populate.

![Some screenshots of the Hexion Broadcast app](media/hexion-broadcaster-app.png "Some screenshots of the Hexion Broadcast app")
