---
title: "Set authentication identity for a portal  | MicrosoftDocs"
description: "Instructions to set authentication identity for a portal."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: shjais
ms.reviewer:
---

# Set authentication identity for a portal

Portals provides authentication functionality built on the [ASP.NET Identity](https://www.asp.net/identity) API. ASP.NET Identity is in turn built on the [OWIN](https://www.asp.net/aspnet/overview/owin-and-katana) framework, which is also an important component of the authentication system. The services provided include:

- Local (username/password) user sign-in
- External (social provider) user sign-in through third-party identity providers
- Two-factor authentication with email
- Email address confirmation
- Password recovery
- Invitation code sign-up for registering pregenerated contact records

> [!NOTE]
> The **Mobile Phone Confirmed** field on the Portal Contact form of the Contact entity currently serves no purpose. This field must be used only when upgrading from Adxstudio Portals.

## Requirements

Portals requires:

- Portals Base
- [!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)] Identity
- [!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)] Identity Workflows solution packages

## Authentication overview

Returning portal visitors can authenticate by using local user credentials or external identity provider accounts. A new visitor can register for a new user account either by providing a username and password or by signing in through an external provider. Visitors who are sent an invitation code (by the portal administrator) have the option to redeem the code in the process of signing up for a new user account.

**Related site settings:**

- `Authentication/Registration/Enabled`
- `Authentication/Registration/LocalLoginEnabled`
- `Authentication/Registration/ExternalLoginEnabled`
- `Authentication/Registration/OpenRegistrationEnabled`
- `Authentication/Registration/InvitationEnabled`
- `Authentication/Registration/RememberMeEnabled`
- `Authentication/Registration/ResetPasswordEnabled`

### Sign in by using a local identity or external identity

![Sign in by using a local account](../media/sign-in-local-account.png "Sign in by using a local account")  

### Sign up by using a local identity or external identity

![Register for a new local account](../media/register-new-local-account.png "Register for a new local account")  

### Redeem an invitation code manually

![Sign up by using an invitation code](../media/sign-up-invitation-code.png "Sign up by using an invitation code")  

## Forgot password or password reset 

Returning visitors who require a password reset (and have previously specified an email address on their user profile) can request a password reset token to be sent to their email account. A reset token allows its owner to choose a new password. Alternatively, the token can be abandoned, leaving the user’s original password unmodified.

**Related site settings:**

- `Authentication/Registration/ResetPasswordEnabled`
- `Authentication/Registration/ResetPasswordRequiresConfirmedEmail`

**Related process:** Send a password reset to a contact

1.  Customize the email in the workflow as necessary.
2.  Submit the email to invoke the process.
3.  The visitor is prompted to check email.
4.  The visitor receives the password reset email with instructions.
5.  The visitor returns to the reset form.
6.  The password reset is complete.

## Redeem an invitation

Redeeming an invitation code allows a registering visitor to be associated with an existing contact record that was prepared in advance specifically for that visitor. Typically, the invitation codes are sent out by email, but you can use a general code submission form to send codes though other channels. After a valid invitation code is submitted, the normal user registration (sign-up) process takes place to set up the new user account.

**Related site settings:**

`Authentication/Registration/InvitationEnabled`

**Related process:** Send invitation

The email sent by this workflow must be customized by using the URL to the redeem invitation page on the portal: https://portal.contoso.com/register/?returnurl=%2f&invitation={Invitation Code(Invitation)}

1. Create an invitation for a new contact.

    ![Create an invitation for a new contact](../media/create-invitation.png "Create an invitation for a new contact")  

2. Customize and save the new invitation.

    ![Customize a new invitation](../media/customize-new-invitation.png "Customize a new invitation")  

3. Process: Send invitation
4. Customize the invitation email.
5. The invitation email opens the redemption page.
6. The user signs up by using the submitted invitation code.

    ![Sign-up with a invitation code](../media/sign-up-invitation-code.png "Sign up by using an invitation code")  

## Manage user accounts through profile pages

Authenticated users manage their user accounts through the **Security** navigation bar of the profile page. Users are not limited to the single local account or single external account they chose at user registration time. Users who have an external account can choose to create a local account by applying a username and password. Users who started with a local account can choose to associate multiple external identities to their account. The profile page is also where the user is reminded to confirm their email address by requesting a confirmation email to be sent to their email account.

**Related site settings:**

- `Authentication/Registration/LocalLoginEnabled`
- `Authentication/Registration/ExternalLoginEnabled`
- `Authentication/Registration/TwoFactorEnabled`

## Set or change a password

A user who has an existing local account can apply a new password by providing the original password. A user who does not have a local account can choose a username and password to set up a new local account. The username cannot be changed after it is set.

**Related site settings:**

`Authentication/Registration/LocalLoginEnabled`

**Related process:**
- Create a username and password.
- Change an existing password.

## Confirm an email address

Changing an email address (or setting it for the first time) puts it into an unconfirmed state. The user can request a confirmation email to be sent to their new email address, and the email will include instructions to the user for completing the email confirmation process.

**Related process:** Send an email confirmation to a contact

1. Customize the email in the workflow as necessary. 
2. The user submits a new email, which is in an unconfirmed state.
3. The user checks email for confirmation.
4. Process: Send email confirmation to contact
5. Customize the confirmation email.
6. The user clicks the confirmation link to complete the confirmation process.

> [!NOTE]
> Ensure that the primary email is specified for the contact because the confirmation email is sent only to the primary email (emailaddress1) of the contact. The confirmation email is not sent to the secondary email (emailaddress2) or alternate email (emailaddress3) of the contact record.

## Enable two-factor authentication

The two-factor authentication feature increases user account security by requiring proof of ownership of a confirmed email in addition to the standard local or external account sign-in. A user trying to sign in to an account that has two-factor authentication enabled is sent a security code to the confirmed email associated with their account. The security code must be submitted to complete the sign-in process. A user can choose to remember the browser that successfully passed the verification, so that the security code will not be required for subsequent sign-ins from the same browser. Each user account enables this feature individually and requires a confirmed email.

> [!WARNING]
> If you create and enable the **Authentication/Registration/MobilePhoneEnabled** site setting to enable the legacy functionality, an error will occur. This site setting is not provided out of the box and not supported by portals.

**Related site settings:**

- `Authentication/Registration/TwoFactorEnabled`
- `Authentication/Registration/RememberBrowserEnabled`

**Related Process:** Send email two-factor code to a contact

1. Enable two-factor authentication.
2. Choose to receive the security code by email.
3. Wait for the email that contains the security code.
4. Process: Send Email Two Factor Code To Contact.
5. Two-factor authentication can be disabled.

## Manage external accounts

An authenticated user may connect (register) multiple external identities to their user account, one from each configured identity provider. After the identities are connected, the user may choose to sign in by using any of the connected identities. Existing identities can also be disconnected, as long as a single external or local identity remains.

**Related Site Settings:**

- `Authentication/Registration/ExternalLoginEnabled`

**External Identity Provider Site Settings**

1.  Select a provider to connect to your user account.

    ![Manage external accounts](../media/manage-external-accounts.png "Manage external accounts")  

2.  Sign in by using the provider you want to connect.

The provider is now connected. The provider can also be disconnected.

## Enable ASP.NET identity authentication

The following describes the settings for enabling and disabling various authentication features and behaviors:


|                        Site Setting Name                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          Authentication/Registration/LocalLoginEnabled          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Enables or disables local account sign-in based on a username (or email) and password. Default: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|          Authentication/Registration/LocalLoginByEmail          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Enables or disables local account sign-in using an email address field instead of a username field. Default: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|        Authentication/Registration/ExternalLoginEnabled         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Enables or disables external account sign-in and registration. Default: true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          Authentication/Registration/RememberMeEnabled          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Selects or clears a Remember me? check box on local sign-in to allow authenticated sessions to persist even when the web browser is closed. Default: true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|          Authentication/Registration/TwoFactorEnabled           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Enables or disables the option for users to enable two-factor authentication. Users with a confirmed email address can opt into the added security of two-factor authentication. Default: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|       Authentication/Registration/RememberBrowserEnabled        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Selects or clears a Remember browser? check box on second-factor validation (email code) to persist the second-factor validation for the current browser. The user will not be required to pass the second-factor validation for subsequent sign-ins as long as the same browser is being used. Default: true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|        Authentication/Registration/ResetPasswordEnabled         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Enables or disables the password reset feature. Default: true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Authentication/Registration/ResetPasswordRequiresConfirmedEmail |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Enables or disables password reset for confirmed email addresses only. If enabled, unconfirmed email addresses cannot be used to send password reset instructions. Default: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|   Authentication/Registration/TriggerLockoutOnFailedPassword    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Enables or disables recording of failed password attempts. If disabled, user accounts will not be locked out. Default: true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|             Authentication/Registration/IsDemoMode              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Enables or disables a demo mode flag to be used in development or demonstration environments only. Do not enable this setting on production environments. Demo mode also requires the web browser to be running locally to the web application server. When demo mode is enabled, the password reset code and second-factor code are displayed to the user for quick access. Default: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|    Authentication/Registration/LoginButtonAuthenticationType    | If a portal only requires a single external identity provider (to handle all authentication), this allows the **Sign-In** button of the header nav bar to link directly to the sign-in page of that external identity provider (instead linking to the intermediate local sign-in form and identity provider selection page). Only a single identity provider can be selected for this action. Specify the [AuthenticationType](https://msdn.microsoft.com/library/microsoft.owin.security.authenticationoptions.authenticationtype.aspx) value of the provider.<br>For a single sign-on configuration using OpenIdConnect, such as using Azure Active Directory B2C, the user needs to provide the Authority.<br>For OAuth2 based providers the accepted values are: `Facebook, Google, Yahoo, [!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)], LinkedIn, Yammer,` or `Twitter`<br>For WS-Federation based providers, use the value specified for the `Authentication/WsFederation/ADFS/AuthenticationType` and `Authentication/WsFederation/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]/\[provider\]/AuthenticationType` site settings. Examples: https://adfs.contoso.com/adfs/services/trust, Facebook-0123456789, Google, Yahoo!, uri:[!INCLUDE[pn-ms-windows-short](../../../includes/pn-ms-windows-short.md)]LiveID. |
|                                                                 |                                                                                                                                                                                                                                                                                                  |

## Enable or disable user registration

The following describes the settings for enabling and disabling user registration (sign-up) options:

| Site Setting Name                                   | Description                                                                                                                                                                             |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authentication/Registration/Enabled                 | Enables or disables all forms of user registration. Registration must be enabled for the other settings in this section to take effect. Default: true                                   |
| Authentication/Registration/OpenRegistrationEnabled | Enables or disables the sign-up registration form for creating new local users. The sign-up form allows any anonymous visitor to the portal to create a new user account. Default: true |
| Authentication/Registration/InvitationEnabled       | Enables or disables the invitation code redemption form for registering users who possess invitation codes. Default: true                                                               |
|Authentication/Registration/CaptchaEnabled|Enables or disables captcha on the user registration page. Default: false<br>**Note**: This site setting might not be available by default. To enable captcha, you must create the site setting and set its value to true. |
||

> [!NOTE]
> Ensure that the primary email is specified for the user because registration is done by using the primary email (emailaddress1) of the user. The user cannot be registered by using the secondary email (emailaddress2) or alternate email (emailaddress3) of the contact record.

## User credential validation

The following describes the settings for adjusting username and password validation parameters. Validation occurs when users sign up for a new local account or change a password.

| Site Setting Name                                                       | Description                                                                                                                                                                                         |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authentication/UserManager/PasswordValidator/EnforcePasswordPolicy      | Whether the password contains characters from three of the following categories:<br><ul><li>Uppercase letters of European languages (A through Z, with diacritic marks, Greek and Cyrillic characters)</li><li>Lowercase letters of European languages (a through z, sharp-s, with diacritic marks, Greek and Cyrillic characters)</li><li>Base 10 digits (0 through 9)</li><li>Nonalphanumeric characters (special characters) (for example, !, $, \#, %)</li></ul>Default: true. For more information: [Password policy](https://technet.microsoft.com/library/hh994562(v=ws.10).aspx).                                                                                                           |  
| Authentication/UserManager/UserValidator/AllowOnlyAlphanumericUserNames | Whether to allow only alphanumeric characters for the username. Default: false. For more information: [UserValidator<TUser, TKey>.AllowOnlyAlphanumericUserNames](https://msdn.microsoft.com/library/dn613211.aspx).                                                          |  
| Authentication/UserManager/UserValidator/RequireUniqueEmail             | Whether a unique email address is needed for validating the user. Default: true. For more information: [UserValidator<TUser, TKey>.RequireUniqueEmail](https://msdn.microsoft.com/library/dn613213.aspx).                                                                   |  
| Authentication/UserManager/PasswordValidator/RequiredLength             | The minimum required password length. Default: 8. For more information: [PasswordValidator.RequiredLength](https://msdn.microsoft.com/library/microsoft.aspnet.identity.passwordvalidator.requiredlength.aspx).                                       |  
| Authentication/UserManager/PasswordValidator/RequireNonLetterOrDigit    | Whether the password requires a non-letter or digit character. Default: false. For more information: [PasswordValidator.RequireNonLetterOrDigit](https://msdn.microsoft.com/library/microsoft.aspnet.identity.passwordvalidator.requirenonletterordigit.aspx). |  
| Authentication/UserManager/PasswordValidator/RequireDigit               | Whether the password requires a numeric digit (from 0 through 9). Default: false. For more information: [PasswordValidator.RequireDigit](https://msdn.microsoft.com/library/microsoft.aspnet.identity.passwordvalidator.requiredigit.aspx).                |  
| Authentication/UserManager/PasswordValidator/RequireLowercase           | Whether the password requires a lowercase letter (from a through z). Default: false. For more information: [PasswordValidator.RequireLowercase](https://msdn.microsoft.com/library/microsoft.aspnet.identity.passwordvalidator.requirelowercase.aspx).        |  
| Authentication/UserManager/PasswordValidator/RequireUppercase           | Whether the password requires an uppercase letter (from A through Z). Default: false. For more information: [PasswordValidator.RequireUppercase](https://msdn.microsoft.com/library/microsoft.aspnet.identity.passwordvalidator.requireuppercase.aspx).       | 
|| 

## User account lockout settings

The following describes the settings that define how and when an account becomes locked from authentication. When a certain number of failed password attempts are detected in a short period of time, the user account is locked for a period of time. The use can try again after the lockout period elapses.

| Site Setting Name                                               | Description                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authentication/UserManager/UserLockoutEnabledByDefault          | Indicates whether the user lockout is enabled when users are created. Default: true. For more information: [UserManager<TUser, TKey>.UserLockoutEnabledByDefault](https://msdn.microsoft.com/library/dn613214.aspx).                                                                                                  |  
| Authentication/UserManager/DefaultAccountLockoutTimeSpan        | The default amount of time that a user is locked out for after Authentication/UserManager/MaxFailedAccessAttemptsBeforeLockout is reached. Default: 24:00:00 (1 day). For more information: [UserManager<TUser, TKey>.DefaultAccountLockoutTimeSpan](https://msdn.microsoft.com/library/dn613201.aspx).                 |  
| Authentication/UserManager/MaxFailedAccessAttemptsBeforeLockout | The maximum number of access attempts allowed before a user is locked out (if lockout is enabled). Default: 5. For more information: [UserManager<TUser, TKey>.MaxFailedAccessAttemptsBeforeLockout](https://msdn.microsoft.com/library/dn613202.aspx).                                                                        |  
| Authentication/ApplicationCookie/ExpireTimeSpan                 | The default amount of time cookie authentication sessions are valid for. Default: 24:00:00 (1 day). For more information: [CookieAuthenticationOptions.ExpireTimeSpan](https://msdn.microsoft.com/library/microsoft.owin.security.cookies.cookieauthenticationoptions.expiretimespan(v=vs.113).aspx). |
||  

## Cookie authentication site settings

Settings for modifying the default authentication cookie behavior. Defined by the [CookieAuthenticationOptions](https://msdn.microsoft.com/library/microsoft.owin.security.cookies.cookieauthenticationoptions.aspx) class.

| Site Setting Name   | Description       |
|----------------------|------------------------------------------------|
| Authentication/ApplicationCookie/AuthenticationType                      | The type of the application authentication cookie. Default: ApplicationCookie. For more information: [AuthenticationOptions::AuthenticationType](https://msdn.microsoft.com/library/dn300391.aspx).  |
| Authentication/ApplicationCookie/CookieName                              | Determines the cookie name used to persist the identity. Default: .AspNet.Cookies. For more information: [CookieAuthenticationOptions::CookieName](https://msdn.microsoft.com/library/dn385537.aspx).  |
| Authentication/ApplicationCookie/CookieDomain                            | Determines the domain used to create the cookie. For more information: [CookieAuthenticationOptions::CookieDomain](https://msdn.microsoft.com/library/dn385536.aspx).  |
| Authentication/ApplicationCookie/CookiePath                              | Determines the path used to create the cookie. Default: /. For more information: [CookieAuthenticationOptions::CookiePath](https://msdn.microsoft.com/library/dn385539.aspx). |
| Authentication/ApplicationCookie/CookieHttpOnly                          | Determines if the browser should allow the cookie to be accessed by client-side javascript. Default: true. For more information: [CookieAuthenticationOptions::CookieHttpOnly](https://msdn.microsoft.com/library/dn385540.aspx).                     |
| Authentication/ApplicationCookie/CookieSecure                            | Determines if the cookie should only be transmitted on HTTPS request. Default: SameAsRequest. For more information: [CookieAuthenticationOptions::CookieSecure](https://msdn.microsoft.com/library/dn385538.aspx).  |
| Authentication/ApplicationCookie/ExpireTimeSpan                          | Controls how much time the application cookie will remain valid from the point it is created. Default: 14 days. For more information: [CookieAuthenticationOptions::ExpireTimeSpan](https://msdn.microsoft.com/library/microsoft.owin.security.cookies.cookieauthenticationoptions.expiretimespan(v=vs.113).aspx).  |
| Authentication/ApplicationCookie/SlidingExpiration                       | The SlidingExpiration is set to true to instruct the middleware to re-issue a new cookie with a new expiration time any time it processes a request which is more than halfway through the expiration window. Default: true. For more information: [CookieAuthenticationOptions::SlidingExpiration](https://msdn.microsoft.com/library/dn385548.aspx). |
| Authentication/ApplicationCookie/LoginPath                               | The LoginPath property informs the middleware that it should change an outgoing 401 Unauthorized status code into a 302 redirection onto the given login path. Default: ~/signin. For more information: [CookieAuthenticationOptions::LoginPath](https://msdn.microsoft.com/library/dn385541.aspx).                                            |
| Authentication/ApplicationCookie/LogoutPath                              | If the LogoutPath is provided the middleware then a request to that path will redirect based on the ReturnUrlParameter. For more information: [CookieAuthenticationOptions::LogoutPath](https://msdn.microsoft.com/library/dn385545.aspx).               |
| Authentication/ApplicationCookie/ReturnUrlParameter                      | The ReturnUrlParameter determines the name of the query string parameter which is appended by the middleware when a 401 Unauthorized status code is changed to a 302 redirect onto the login path. For more information: [CookieAuthenticationOptions::ReturnUrlParameter](https://msdn.microsoft.com/library/dn385546.aspx).                           |
| Authentication/ApplicationCookie/SecurityStampValidator/ValidateInterval | The period of time between security stamp validations. Default: 30 mins. For more information: [SecurityStampValidator::OnValidateIdentity](https://msdn.microsoft.com/library/microsoft.aspnet.identity.owin.securitystampvalidator.onvalidateidentity.aspx).                    |
| Authentication/TwoFactorCookie/AuthenticationType                        | The type of the two-factor authentication cookie. Default: TwoFactorCookie. For more information: [AuthenticationOptions::AuthenticationType](https://msdn.microsoft.com/library/dn300391.aspx).            |
| Authentication/TwoFactorCookie/ExpireTimeSpan                            | Controls how much time the two-factor cookie will remain valid from the point it is created. Default: 5 mins. For more information: [CookieAuthenticationOptions::ExpireTimeSpan](https://msdn.microsoft.com/library/dn385543.aspx).     |
|||

### See also

[Configure portal authentication](configure-portal-authentication.md)  
[OAuth2 provider settings for portals](configure-oauth2-settings.md)  
[Open ID Connect provider settings for portals](configure-openid-settings.md)  
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
[SAML 2.0 provider settings for portals](configure-saml2-settings.md)  
