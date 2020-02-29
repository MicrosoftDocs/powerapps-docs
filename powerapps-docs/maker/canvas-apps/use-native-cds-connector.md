---
title: Use native Common Data Service connector | Microsoft Docs
description: 
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 02/27/2020
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Common Data Service and the Improved data source experience

If you created a canvas app with a Common Data Service connector prior to November 2019, then you may not have the benefit of the most current version of the Common Data Service.  The **Improved** experience switch unlocks significant speed gains, increased reliability, and features such as access to Common Data Service Views and File and Image field attributes. 
The “Improve data source experience and Common Data Service views” feature option appears in the Advanced settings section.   The “Relational data, option sets, and other new features for Common Data Service” now appears in the Deprecated features section.
## How do I upgrade my canvas app?
Upgrade your app by inspecting the settings of the options and then following the directions below.
### A.	“Improve data source experience and Common Data Service views” is already “On”
If the “Improve data source experience and Common Data Service views” feature is “On” then you have previously converted your canvas app to use this new feature or you started an app when the default setting for this feature was “On.”  You are already there.  If it isn’t already, you may want to turn on the “Explicit Column Selection” feature “On” as well.
Note that as this feature is not supported on Windows Player, authors working with Power Apps Windows Player will need to turn the “Improve data source … “ feature “Off.”
### B.	“Relational data, option sets and other new features for CDS” feature is “Off”
Check in the Deprecated features section for this setting.  If the “Relational data, option sets and other new features for CDS” in your app is “Off” then use the steps below as a first step in the conversion.  If you can’t see this option or if it’s already “On”, continue to the next section.
#### First, turn “Use display names” ON
1.	Turn on “Use display names” (if it is not already on.)
2.	Wait for the health monitor to finish analyzing your app.
3.	Save, close, and re-open your app.
4.	Resolve all formula errors.
5.	Save, close, and re-open your app.

##### Possible errors at this step
It’s possible that some of the newly shown display names conflict with the display names for other entities, fields, or controls.  For instance, you might have a control name “image” and a field name “image.”  
1.	For control name clashes, change the name of the control to be different and unique.  This is usually the simplest fix. 
2.	For field and entity display name conflicts you may see a formula that is expecting an entity but is resolving to a more locally scoped field name. Use the square bracket with a “@” symbol to indicate a global scope so it resolves to the entity (e.g., [@entityName].)
#### Second, turn ON both “Relational data, option sets and other new features for CDS” and “Use GUID data types instead of strings”
1.	Turn on “Relational data, option sets and other new features for CDS”.
2.	Turn on “Use GUID data types instead of strings”.
3.	Wait for the health monitor to finish analyzing your app.
4.	Resolve all formula errors.
5.	Save, close, and re-open your app.  

##### Possible errors and suggestions at this step
It’s possible to have errors at this stage if you were using an option set field or hard coded GUID text values.  
1.	Option Set values.  If you were using an option set field with a text identifier for the option set value, you should instead use the dot notation to reference the option set value. For instance:  Change Patch (Accounts, OptionSet1 = “12345”) to Change Patch (Accounts, OptionSet.Item1) where Item1 corresponds to the “12345” value.  See the detailed example on converting Option sets below.
2.	GUIDs.  If you were using a static GUID string such as “015e45e1044e49f388115be07f2ee116”, convert it to function that returns a GUID object (e.g, GUID(“015e45e1044e49f388115be07f2ee116”)) 
3.	Lookups.  If you were using Lookup functions to get first level lookup values such as: Lookup (Lookup (Contacts, ‘contactID’ = ThisItem.ContactID”) consider using ThisItem.PrimaryContacts (where PrimaryContacts is the name of the entity) instead.  
   
### C.	“Improve data source experience and Common Data Service views“ is “Off”

This setting is at the top of the Setting page.  If the “Improve data source experience and Common Data Service views” in your app is “Off” then use the steps below to finish the conversion.
#### Turning on Improve data source experience and Common Data Service views” 
1.	Remove your existing Common Data Service data source connections. 
2.	Turn ON the “Improve data source experience and Common Data Service views” 
3.	Re-add your connections to your data sources to the Common Data Service using the new data source selection experience. 
4.	Save your application. 
Note:  If your application is extremely large, adding your data source connections back may take a while.  Please do not close the application during this process.

# Converting canvas apps with the Dynamics 365 connector
To convert your app that currently uses the Dynamics 365 connector you will need to drop and re-add your connections to your data sources.  Use the steps below to convert your connections to your data sources.
1.	Ensure that the “Improve data source experience and Common Data Service views” feature is turned “On.”
2.	Remove your existing Dynamics 365 data source connections.
3.	Re-add your connections to your data sources to the Common Data Service using the new data source selection experience.
4.	Save your application.


## Possible errors and suggestions at this step
It’s possible to have errors as you convert if you were not using Display Names, if you were using GUID strings, or if you were using an option set fields. 
1.	For control name clashes, change the name of the control to be different and unique.  This is usually the simplest fix. 
2.	For field and entity display name conflicts you may see a formula that is expecting an entity but is resolving to a more locally scoped field name. Use the square bracket with a “@” symbol to indicate a global scope so it resolves to the entity (e.g., [@entityName].)
3.	Option Set values.  If you were using an option set field with a text identifier for the option set value, you should instead use the dot notation to reference the option set value. For instance:  Change Patch (Accounts, OptionSet1 = “12345”) to Change Patch (Accounts, OptionSet.Item1) where Item1 corresponds to the “12345” value.
4.	GUIDs.  If you were using a static GUID string such as “015e45e1044e49f388115be07f2ee116”, convert it to function that returns a GUID object (e.g, GUID(“015e45e1044e49f388115be07f2ee116”)) 
5.	Lookups.  If you were using Lookup functions to get first level lookup values such as: Lookup (Lookup (Contacts, ‘contactID’ = ThisItem.ContactID”) consider using ThisItem.PrimaryContacts (where PrimaryContacts is the name of the entity) instead.  

# Detailed Examples

# Option Sets

Converting your app to use the new Power Apps Option sets and Two option data types along with the controls that support them can be one of the biggest sources of change when upgrading your app to use the new Improved data source experience.      

Previously there were separate *_myfield* and *_myfield_label fields* used for an Option set, and now there is just a single *myfield* that can be used both for locale independent comparisons and to obtain the locale specific label. 

## Remove data cards bound to Option sets and re-add
It's best to remove existing data cards and re-add them to work with your Option set.  For example, if you are working with the Account entity and the Category Option set, you'll see that the DataField property of the data card was set to *_accountcategory_label*. In the field list you can see that the data card has a type of String.





