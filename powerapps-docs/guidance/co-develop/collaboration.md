---
title: "Establishing a collaboration model | Microsoft Docs"
description: "Learn more about how to establish a well-defined and structured collaboration model for fusion app development."
author: luis-camino-ms
ms.topic: best-practice
ms.custom: Focus-center
ms.date: 07/22/2022
ms.subservice: guidance
ms.author: lucamino
ms.reviewer: tapanm

---

# Establishing a collaboration model

A well-defined and structured collaboration model is central to the efficient operation of a fusion team. This section considers the factors that can contribute to this success, such as well-defined roles and responsibilities, a structured business rhythm, reliable communication channels, and an accessible documentation portal. 


## Define roles and responsibilities
To create an efficient fusion team, you must first establish clear roles and responsibilities. The key approach is to start small and only introduce more roles and personnel when necessary. Use smaller targets to build on success and demonstrate the value of the fusion team model before attempting more ambitious projects. 

At a minimum, your team should include the following personnel and roles:
- **The product owner** – typically, this is the person tasked with ensuring the projects’ success. He or she'll also define the clear and compelling purpose or may co-develop that vision with the remainder of the team.
- **The domain expert** – this is the business-savvy member of the team who understands and can articulate both the challenge and the solution. With the simplicity of the Power Apps low-code approach, he or she should be able to get most of the way to creating that solution.
- **The professional developer** – the ‘Pro Dev’ takes the solution from the domain expert and gives it enough coding support to enable it to deliver its intended functionality (and nothing more) if necessary.
- **The administrator** – this team member facilitates integration and support scenarios, while performing back-end administrative services.
Any further support in terms of time and expertise that the core team requires can be brought in on a flexible basis, rather than as a permanent member of the group. This approach ensures efficient operation of the fusion team while providing access to the more resources that the product owner needs for the team to achieve its goals. 

## Establish a rhythm of business model
Synchronizing operational rhythms related to app development in fusion team can improve team effectiveness by aligning to the following structure:

- **Define a repeating calendar event for team synchronization.** For most teams, weekly or fortnightly status update meetings are fine. However, don’t schedule meetings for the sake of having meetings and try to avoid increasing the frequency of meetings close to deadlines, as that approach can be counterproductive. 
- **Keep to agreed working hours.** Ideally, your team will be collocated, although fusion teams can also work effectively across geographies and time zones. Whatever the working arrangements, ensure that everyone understands the purpose and duration of working hours and respects those boundaries. 
- **Create a weekly rhythm.** The team’s weekly rhythm should include solo work, collaborative interactions, and, when necessary, effective meetings. These meetings should have a specific purpose, such as:
  - Scope reviews – to bring teams together on new initiatives.
  - User experience reviews – to go over app design and mockups.
Meetings to plan other meetings, meetings instead of emails or instant messages, or meetings without a clearly defined purpose are productivity killers.
- **Work efficiently.** The team needs to align internally to create the most usable solution. This alignment should include the ability to reuse components that others have built.
- **Maintain consistent progress towards the goal.** To ensure the team meets its goals, it's essential that everyone works together to achieve that outcome. For fusion teams working with Power Apps, maintaining this progress means capturing and understanding user feedback, prioritizing the backlog, and establishing and maintaining a holistic roadmap of the whole project. 
- **Generate a support matrix.** A support matrix provides a structured approach for obtaining the necessary support to progress towards the team’s overall goals. An inevitable challenge with business technologists directly building apps is when they reach the limits of their knowledge and abilities. At this point, who do they reach out to and how do they do that? How do they deal with a user bug report? This matrix should set out how they can raise a support ticket to engage the right team in troubleshooting and resolving the issue, based on the issue’s severity. For each support scenario, this matrix explains the escalation and troubleshooting path. 

## Define how the team communicates
Standardizing team communications is another essential component in maintaining an efficient operation. All team members must know how the team connects, particularly in asynchronous modes across time zones. Your communications strategy should consider the following areas:
- **Channels.** What channels will the team use for primary and secondary communications? What are the advantages and disadvantages of each? In a world of choice, simply adopting email may not be best solution and options such as Microsoft Teams may provide better clarity, improved traceability, and higher response rates. 
- **Notification types.** How are you going to notify your team of updates or events that they need to action? 
- **Message frequency and volume.** How often do you inform your team? A daily communication can provide a useful summary of what’s happened that day, but some messages may need earlier action. Most knowledge workers are overloaded with emails. Ensure that you achieve a balance between frequency and volume to avoid team members being swamped with project-related messages. 
- **Automation.** How can you automate the communication process? Standardized email templates, bots, and event alerts can all help, but need to be used responsibly if they aren't to overload team members’ ability to respond. 
- **Good communication skills.** Not everyone in a team will have the same level of communication skills, but anyone can get better. Simple approaches like choosing a good subject for an email make a dramatic difference in how well the team responds to that message. Encourage simple and effective writing in all communications; where there are actions that team members need to take, be specific and call out those actions in the subject line. 

An example of how to employ effective communication skills might be where you need to change a table definition in Dataverse, such as adding multiple fields. When you send out a notification of this intended change, the team must understand that if they don't respond within a reasonable time, then this lack of response indicates their agreement. Standardized and logical communication processes help improve efficiency and deliver expected outcomes. 

## Publish a documentation portal
Documentation isn't just an optional part of any project – it's essential for communication, collaboration, support, and ongoing operations. Commented code is good code and creating comprehensive explanatory and training documentation is an essential part of the deployment and learning phases of any fusion project. 

- **Application catalog.** The application catalog is a matrix or table that summarizes and coordinates all applications within a particular team’s responsibility. The catalog includes all the respective owners from the roles and responsibilities section. A key function is to ensure that the team knows exactly who owns what, thereby simplifying the process of contacting the right team member for specific answers. 
- **Technical questions.** Your team should maintain a repository of frequently asked (or even not-so-frequently-asked) technical questions about the operation of the app. These questions need to be reasonable, with the answers well-written and accessible. 
- **How-to guides.** How-to guides are instantly digestible sets of procedures that provide simple answers to common setup and operating questions. Typically, they would answer a specific question, such as “How do I get started creating a new app?”
- **Onboarding.** Onboarding instructions are internal-only documents designed to help new team members. This documentation would include information such as access requests, joining email distribution lists, setting up and subscribing to alerts, and so on. 

## Best practices
The following best practices should help in defining boundaries and approaches for efficient work within fusion teams.

### Accountability
While maker-led development and fusion teams enable rapid application development and deployment, it's vital to ensure that this effort is overt and conducted in partnership with the IT department. Makers must be accountable to IT to help prevent issues in relation to the growth of shadow IT systems. 

In consequence, IT must be alerted whenever a maker starts building an app. This notification in turn facilitates the development process, as IT can provide suitable support to the maker and the fusion team, helping them create well-architected apps that are properly secured and managed.

### Automation

A well-implemented automation can provide a huge boost to productivity. An example of how to increase solution deployment success is by automating any required checks in multi-solution deployments. These automated checks can include:

- Solution version verification, where each deployment uses an updated version number, thus avoiding issues when troubleshooting.
- Duplicate connection references.
- Missing connection references.
- Duplicate components.

The [PR Checker solution](community-solutions-tools.md) includes an example of how to incorporate this automation effectively. 

### Reporting

Fusion teams and maker-developed apps must align to a data-first approach, which means building apps where it's possible to monitor success directly. Achieving this outcome requires good instrumentation that provides the ability to discover what the team is doing well, along with analysis of this feedback to generate accurate appraisals of the effectiveness of a particular app. To achieve this outcome, you should:

- **Monitor and assess applications.** Just because one person thinks something is useful or a good idea, doesn’t automatically mean everyone will find value in it. Teams need to monitor app usability and assess their functionality to ensure that any new developments are useful and functioning appropriately. 
- **Encourage good judgment.** In other words, don’t build apps just because you can – only build them to address a specific business need. 


> [!div class="nextstepaction"]
> [Next step: Establishing co-development governance](governance.md)
