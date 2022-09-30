---
title: List calendar view
description: Learn how to enable your list to render as a calendar view on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# List Calendar view

On the **Calendar View** tab, you can enable the list to render as a calendar view, with each individual record configured to act as a single event.

The following field mappings can be configured to display list records as dated events on the calendar. The records need to include at minimum a date field.

> [!Tip]
> See [date and time](behavior-format-date-time-field.md#date-and-time) field behaviors for information on formatting date and time fields on portals.

| Entity Field Mappings | Details |
| - | - |
| Start Date Field Name | A datetime column representing the start date of a calendar event. |
| End Date Field Name | A datetime column representing the end date of a calendar event. |
| Summary Field Name | A text column that will show the summary of a calendar event. |
| Description Field Name | A text column that will display a description of the calendar event. |
| Organizer Field Name | A text or lookup column that will display the organizer of the calendar event. |
| Location Field Name | A text column describing the location of the calendar event.|
| Is All Day Field Name | A yes/no column indicating if the calendar event is all day. |

| Setting | Details |
| - | - |
| Initial View | Initial view of the calendar; year, month, week, or day. Default value is month. |
| Initial Date | The initial start date when the calendar is rendered. Default (blank) will be the current date. |
| Time Zone Display Mode | The time zone the calendar will be displayed in. No option selected will display the events based on how the date column was configured in Dataverse. The *User Local Time Zone* will display events in the calendar using the time zone of the user viewing the portal. *Specific Time Zone* will display the calendar events with a specified time zone. |
| Display Time Zone | If the **Time Zone Display Mode** is set to *Specific Time Zone* this value will determine the time zone the calendar events are displayed. |
| Style | The setting displays the calendar in either a *Full Calendar* format or as an *Event List* |

Once the specific fields are configured, a list calendar view will appear on the portal page.

:::image type="content" source="media/lists/calendar-list.png" alt-text="List displayed as a calendar on a web page.":::

### See also

- [Work with lists](entity-lists.md)
- [Display multiple Dataverse records using lists](/training/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
