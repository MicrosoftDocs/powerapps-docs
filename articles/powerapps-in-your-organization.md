<properties
    pageTitle="PowerApps sing up Q&A in your organization | Microsoft PowerApps"
    description="Common questions and answers about licenses and users signing up for PowerApps in your Office 365 tenant"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="MandiOhlinger"
    manager="erikre"
    editor=""
    tags=""
 />
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="05/18/2016"
    ms.author="mandia"/>

# Power Apps in your organization Q&A
This topic describes how users in your organization can use Power Apps, and how you can control the PowerApps service. 


## What are PowerApps?

Microsoft PowerApps enables users to create applications for Windows, iOS, and Android mobile devices. Using these apps, you can create connections to common SaaS services, including Twitter, Office 365, Dropbox, Excel, and more.
 
PowerApps is currently in public preview. 

## How do users sign up for PowerApps?

Individual users in your organization can sign up for PowerApps through the [PowerApps web site](http://powerapps.microsoft.com). When a user in your organization signs up for PowerApps, that user is assigned a PowerApps license automatically.
 
[Sign up for PowerApps](signup-for-powerapps.md) includes more details.


## How do individual users in my organization sign up?

There are three scenarios that might apply to users in your organization:

#### Scenario 1: Your organization already has an existing Office 365 environment and the user signing up for PowerApps already has an Office 365 account. 

In this scenario, if a user already has a work or school account in the tenant (for example, contoso.com) but does not yet have PowerApps, Microsoft activates the plan for that account, and the user is automatically notified of how to use PowerApps.


#### Scenario 2: Your organization has an existing Office 365 environment and the user signing up for PowerApps doesn’t have an Office 365 account. 

In this scenario, the user has an email address in your organization’s domain (for example, contoso.com) but does not yet have an Office 365 account. In this case, the user can sign up for PowerApps and is automatically given an account. This lets the user access PowerApps. For example, if an employee named Nancy uses her work email address (for example, Nancy@contoso.com) to sign up, Microsoft automatically adds Nancy as a user in Contoso’s Office 365 environment and activates PowerApps for that account.


#### Scenario 3: Your organization does not have an Office 365 environment connected to your email domain. 

There are no administrative actions your organization needs to take to take advantage of PowerApps.

**IMPORTANT**: If your organization has multiple email domains and you prefer all email address extensions to be in the same tenant, before any users create your primary tenant, add all email address domains to that tenant before any users create your primary tenant. There is no automated mechanism to move users across tenants after they have been created. For more information on this process, see [If I have multiple domains](powerapps-in-your-organization.md#if-i-have-multiple-domains,-can-i-control-the-office-365-tenant-that-users-are-added-to?) later in this article and [Add your domain to Office 365](https://support.office.com/article/Add-your-domain-to-Office-365-ffdb2216-330d-4d73-832b-3e31bcb5b2a7) online.
 

## How will this change the way I manage identities for users in my organization today?

If your organization already has an existing Office 365 environment and all users in your organization have Office 365 accounts, identity management will not change.

If your organization already has an existing Office 365 environment but not all users in your organization have Office 365 accounts, we will create a user in the tenant and assign licenses based on the user’s work or school email address. This means that the number of users you are managing at any particular time will grow as users in your organization sign up for the service.

If your organization does not have an Office 365 environment connected to your email domain, there will be no change in how you manage identity. Users will be added to a new, cloud-only user directory, and you will have the option to elect to take over as the tenant admin and manage them.
 

## What is the process to manage a tenant created by Microsoft for my users?

If a tenant was created by Microsoft, you can claim and manage that tenant by following these steps:

1. Join the tenant by signing up for PowerApps using an email address domain that matches the tenant domain you want to manage. For example, if Microsoft created the contoso.com tenant, you will need to join the tenant with an email address ending with @contoso.com.

2. Claim admin control by verifying domain ownership: once you are in the tenant, you can promote yourself to the admin role by verifying domain ownership. To do so, follow these steps:  

	1. Go to [https://portal.office.com](https://portal.office.com).

	2. Select the app launcher icon in the upper-left and choose Admin.
	Admin tile used to become an admin 

		**INSERT SCREEN SHOT**

	3. Read the instructions on the **Become the admin** page and then choose **Yes, I want to be the admin**.  
	
		**NOTE**: If this option doesn’t appear, there is already an Office 365 administrator in place.

 
## If I have multiple domains, can I control the Office 365 tenant that users are added to?

If you do nothing, a tenant will be created for each user email domain and subdomain.

If you want all users to be in the same tenant regardless of their email address extensions: 

- Create a target tenant ahead of time or use an existing tenant, and add all the existing domains and subdomains that you want consolidated within that tenant. Then all the users with email addresses ending in those domains and subdomains will automatically join the target tenant when they sign up.


**IMPORTANT**: There is no supported automated mechanism to move users across tenants once they have been created. To learn about adding domains to a single Office 365 tenant, see [Add your users and domain to Office 365](https://support.office.com/article/Add-your-users-and-domain-to-Office-365-ffdb2216-330d-4d73-832b-3e31bcb5b2a7).


## How can I prevent users from signing up for PowerApps?

There are steps you can take as an admin to prevent users from signing up for PowerApps. If you do block this, users’ attempts to sign in will fail and they will be directed to contact their organization’s admin. You do not need to repeat this process if you have already disabled automatic license distribution before (e.g. Office 365 for Education for Students, Faculty, and Staff).

These steps require the use of Windows PowerShell. To get started with Windows PowerShell, see the [PowerShell getting started guide](http://go.microsoft.com/fwlink/p/?LinkID=286814).

To perform the following steps, you must install the latest 64-bit version of the [Azure Active Directory Module for Windows PowerShell](http://go.microsoft.com/fwlink/p/?LinkID=236297).

After you click the link, select **Run** to install the package.

**Disable automatic tenant join** : Use this Windows PowerShell command to prevent new users from joining a managed tenant:

To disable automatic tenant join for new users:  
`Set-MsolCompanySettings -AllowEmailVerifiedUsers $false`

To enable automatic tenant join for new users:  
`Set-MsolCompanySettings -AllowEmailVerifiedUsers $true`


 
## How do I remove PowerApps for users that already signed up?

**Need to rewrite/add specific details that apply to PowerApps. The following steps are from Power BI**

If a user signed up for PowerApps but you no longer want them to have access to PowerApps, you can remove the PowerApps license for that user.

1. Go to the [Office 365 Admin Portal](https://portal.microsoftonline.com/).

2. In the left navigation bar, select **Users then Active Users**.

3. Find the user you want to remove the license for, then select their name.

4. On the user details page, select **Licenses** in the left navigation bar.

5. Uncheck **Microsoft PowerApps**.

6. Select **Save**.


## How can I allow users to join my existing Office 365 tenant?

To allow users to join your tenant, run the opposite command as described in the question above:  
`Set-MsolCompanySettings -AllowEmailVerifiedUsers $true`
 

## How do I verify if I have the block on in the tenant?

Use the following PowerShell script:  
`Get-MsolCompanyInformation | fl allow*`
 

## How can I prevent my existing users from starting to use PowerApps?

**Disable automatic license distribution** : Use this Windows PowerShell script to disable automatic license distributions for existing users. You do not need to repeat this process if you have already disabled automatic license distribution before (e.g. Office 365 for Education for Students, Faculty, and Staff).

To disable automatic license distribution for existing users:  
`Set-MsolCompanySettings -AllowAdHocSubscriptions $false`

To enable automatic license distribution for existing users:  
`Set-MsolCompanySettings -AllowAdHocSubscriptions $true`

**NOTE**: The AllowAdHocSubscriptions flag is used to control several user capabilities in your organization, including the ability for users to sign up for the Azure Rights Management Service. Changing this flag will affect all of these capabilities.
 
**NOTE**: This blocking prevents new users in your organization from signing up for PowerApps. Users that sign up for PowerApps prior to disabling new signups for your organization will still retain their licenses. See the [How do I remove PowerApps for users that already signed up?](topic-name.md#how-do-i-remove-powerapps-for-users-that-already-signed-up?) section for instructions on how you can remove access to PowerApps for users that had previously signed up for the service.


## How can I allow my existing users to sign up for PowerApps?

To allow your existing users to sign up for PowerApps, run the opposite command as described in the previous question:  
`Set-MsolCompanySettings -AllowAdHocSubscriptions $true`
 

## How do I know when new users have joined my tenant?

Users who have joined your tenant as part of this program are assigned a unique license that you can filter on within your active user pane in the admin dashboard.

To create this new view, in the Office 365 admin center, go to **Users** > **Active Users**, and on the **Select a View** menu, select **New View**. Name your new view, and under **Assigned license**, select **Microsoft PowerApps**. Once the new view has been created, you can see all the users in your tenant who have enrolled in this program.
 

## Are there any additional things I should be prepared for?

You might experience an increase in password reset requests. For information about this process, see [Reset a user's password](https://support.office.com/article/Reset-a-users-password-7a5d073b-7fae-4aa5-8f96-9ecd041aba9c).

You can remove a user from your tenant via the standard process in the Office 365 admin center. However, if the user still has an active email address from your organization, they will be able to rejoin unless you block all users from joining.
 

## Why did 10,0000 licenses for Microsoft PowerApps show up in my Office 365 tenant?

As a qualifying organization, users in your organization are eligible to use Microsoft PowerApps and these licenses represent the available capacity for new PowerApps users in your tenant. There is no charge for these licenses. If you’ve chosen to allow users to sign up for PowerApps themselves, they will be assigned one of these available free licenses when they complete the sign up process. You can also choose to assign these licenses to users yourself through the Office 365 admin portal.
 

## Is this free? Will I be charged for these licenses?

These licenses are for the public preview of PowerApps, which is currently free. 
 

