---
title: "Azure AD B2C provider settings for portals | MicrosoftDocs"
description: "Instructions to enable Azure AD B2C provider settings for portals."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: shjais
ms.reviewer:
---

# Azure AD B2C provider settings for portals

[!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory (Azure AD) powers Office 365 and Dynamics 365 services for employee or internal authentication. [!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory B2C is an extension to that authentication model that enables external customer sign-ins through local credentials and federation with various common social identity providers.

A portal owner can configure the portal to accept [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C as an identity provider. [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C supports Open ID Connect for federation.

In the process of configuring [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C as an identity provider for your portal, multiple values are generated that you will use later while you configure the portal. You can note these values in the following table. While configuring the portal, replace the variable name with the values you note here.

| Variable Name     | Value | Description                                                           |
|-------------------|-------|-----------------------------------------------------------------------|
| Application-Name  |       | Name of the application that represents the portal as a relying party |
| Application-ID    |       | The Application ID associated with the application created in Azure Active Directory B2C.  |
| Policy-Signin-URL |       | The Issuer (iss) URL defined in the metadata endpoint.                |
| Federation-Name   |       | A unique name to identify the type of federation provider such as 'B2C'. This will be used in Site Setting names to group configuration settings for this specific provider.                                                                      |
| | | |

### Use Azure AD B2C as an identity provider for your portal

1. Sign in to your [Azure portal](https://portal.azure.com/).
2. [Create an Azure AD B2C tenant](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-get-started).
3. Select **[!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C** on the leftmost navigation bar.
4. [Create Azure application](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-app-registration#register-a-web-application).

   > [!Note]
   > You must choose **Yes** for the **Allow implicit flow** field and specify your portal URL in the **Reply URL** field. The value in the **Reply URL** field should be in the format [portal domain]/signin-[Federation-Name]. For example, `https://contosocommunity.microsoftcrmportals.com/signin-B2C`.

5. Copy the application name, and enter it as the value of Application-Name in the preceding table.
6. Copy the application ID, and enter it as the value of Application-ID in the preceding table.
7. [Create a sign-up or sign-in policy](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-reference-policies#create-a-sign-up-or-sign-in-policy).
8. Select the policy, and then select **Edit**.
9. Select **Token, session & SSO config**.
10. From the **Issuer (iss) claim** list, select the URL that has **/tfp** in its path.
11. Save the policy.
12. Select the URL in the **Metadata endpoint for this policy** field.
13. Copy the value of the issuer field and enter it as the value of Policy-Signin-URL in the preceding table. 

## Portal configuration

After creating and configuring the B2C tenant in [!include[Azure](../../../includes/pn-azure-shortest.md)], you must configure your portal to federate with [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C by using the Open ID Connect protocol. You must create a unique name for your federation to [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C&mdash;for example, B2C&mdash;and store it as the value of the *Federation-Name* variable in the above table.

### Configure your portal
1. Open the Portal Management app.
2. Go to **Portals** > **Websites**.
3. Select the website record for which [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C needs to be enabled.
4. Go to **Site Settings**.
5. Create the following site settings:
   -   **Name**: Authentication/OpenIdConnect/[Federation-Name]/Authority

       **Value**: [Policy-Signin-URL]
   -   **Name**: Authentication/OpenIdConnect/[Federation-Name]/ClientId

       **Value**: [Application-ID]
   -   **Name**: Authentication/OpenIdConnect/[Federation-Name]/RedirectUri

       **Value**: [portal domain]/signin-[Federation-Name]

       For example, `https://mysite.com/signin-b2c` 
6. To support a federated sign-out, create the following site setting:
   - **Name**: Authentication/OpenIdConnect/[Federation-Name]/ExternalLogoutEnabled

     **Value**: true
7. To hardcode your portal to a single identity provider, create the following site setting:
   - **Name**: Authentication/Registration/LoginButtonAuthenticationType

     **Value**: [Policy-Signin-URL]

8. To support password reset, create the required site settings described [here](#password-reset).
9. To support claims mapping, create the required site settings described [here](#claims-mapping).

For a complete list of related site settings, see [here](#related-site-settings).

### Password reset

The following site settings are required if you want to support password reset with [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C local accounts:

| Site Setting                                                        | Description                                                                                                          |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Authentication/OpenIdConnect/[Federation-Name/PasswordResetPolicyId | ID of the password reset policy.                                                                                     |
| Authentication/OpenIdConnect/[Federation-Name]/ValidIssuers         | A comma-delimited list of issuers that includes the [Policy-Signin-URL] and the issuer of the password reset policy. |
|Authentication/OpenIdConnect/[Federation-Name]/DefaultPolicyId | ID of the sign-in or sign-up policy.|
|||

### Related site settings

You can create or configure the following site settings in portals to support [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C as an identity provider:


| Site Setting                                                         | Description                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authentication/Registration/ProfileRedirectEnabled                   | Specifies whether the portal can redirect users to the profile page after successful sign-in. By default, it is set to true.                                                                                                                                            |
| Authentication/Registration/EmailConfirmationEnabled                 | Specifies whether email validation is required. By default, it is set to true.                                                                                     |
| Authentication/Registration/LocalLoginEnabled                        | Specifies whether local sign-in is required. By default, it is set to true.                                                                        |
| Authentication/Registration/ExternalLoginEnabled                     | Enables or disables external authentication.       |
| Authentication/Registration/AzureADLoginEnabled                      | Enables or disables [!include[Azure](../../../includes/pn-azure-shortest.md)] AD as an external identity provider. By default, it is set to true.                                                                                                                                                                      |
| Authentication/OpenIdConnect/[Federation-Name]/ExternalLogoutEnabled | Enables or disables federated sign-out. When set to true, users are redirected to the federated sign-out user experience when they sign out from the portal. When set to false, users are signed out from the portal only. By default, it is set to false.               |
| Authentication/LoginTrackingEnabled                                  | Enables or disables tracking the user's last sign-in. When set to true, the date and time are displayed in the **Last Successful Sign-in** field on the contact record. By default, this is set to false.                                                            |
| Authentication/OpenIdConnect/[Federation-Name]/RegistrationEnabled   | Enables or disables the registration requirement for the existing identity provider. When set to true, registration is enabled for the existing provider only if the site setting Authentication/Registration/Enabled is also set to true. By default, it is set to true. |
|Authentication/OpenIdConnect/[Federation-Name]/PostLogoutRedirectUri |Specifies the URL within the portal to redirect to after a user signs out. |
| | |

### Related content snippet

If registration is disabled for a user after the user has redeemed an invitation, display a message by using the following content snippet:

**Name**: Account/Register/RegistrationDisabledMessage

**Value**: Registration has been disabled.

## Customize the [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C user interface

[!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C supports user interface customization. You can customize the user experience for sign-up and sign-in scenarios.

### Step 1: Create a web template
Create a web template by using the following values:

**Name**: [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C Custom Page

**Source**: Use the following sample web template source HTML.

```html
<!DOCTYPE html>
<html lang=en-US>
  <head>
    <meta charset=utf-8>
    <meta name=viewport content=width=device-width, initial-scale=1.0>
    <meta http-equiv=X-UA-Compatible content=IE=edge>
    <title>
      {{ page.title | h }}
    </title>
                        <link href={{ request.url | base }}/bootstrap.min.css rel=stylesheet>
                        <link href={{ request.url | base }}/theme.css rel=stylesheet>
                        <style>
                          .page-heading {
            padding-top: 20px;
      }
      .page-copy {
            margin-bottom: 40px;
      }
      .highlightError {
        border: 1px solid #cb2027!important;
        background-color: #fce8e8!important;
      }
      .attrEntry .error.itemLevel {
        display: none;
        color: #cb2027;
        font-size: .9em;
      }
      .error {
        color: #cb2027;
      }
      .entry {
        padding-top: 8px;
        padding-bottom: 0!important;
      }
      .entry-item {
        margin-bottom: 20px;
      }
      .intro {
        display: inline;
        margin-bottom: 5px;
      }
      .pageLevel {
          width: 293px;
          text-align: center;
          margin-top: 5px;
          padding: 5px;
          font-size: 1.1em;
          height: auto;
      }
      #panel, .pageLevel, .panel li, label {
          display: block;
      }
      #forgotPassword {
          font-size: .75em;
          padding-left: 5px;
      }
      #createAccount {
          margin-left: 5px;
      }
      .working {
          display: none;
          background: url(data:image/gif;base64,R0lGODlhbgAKAPMAALy6vNze3PTy9MTCxOTm5Pz6/Ly+vNTS1Pz+/�N0Jp6BUJ9EBIISAQAh+QQJCQAKACxRAAIABgAGAAAEE1ClYU4RIIMTdCaegVCfRASCEgEAOw==) no-repeat;
          height: 10px;
          width: auto;
      }
      .divider {
        margin-top: 20px;
        margin-bottom: 10px;
      }
      .divider h2 {
        display: table;
        white-space: nowrap;
        font-size: 1em;
        font-weight: 700;
      }
      .buttons {
        margin-top: 10px;
      }
      button {
            width:auto;
            min-width:50px;
            height:32px;
            margin-top:2px;
            -moz-border-radius:0;
            -webkit-border-radius:0;
            border-radius:0;
            background:#2672E6;
            border:1px solid #FFF;
            color:#fff;
            transition:background 1s ease 0s;
            font-size:100%;
            padding:0 2px
      }

      button:hover {
            background:#0F3E83;
            border:1px solid #3079ed;
            -moz-box-shadow:0 0 0;
            -webkit-box-shadow:0 0 0;
            box-shadow:0 0 0
      }
      .password-label label {
        display: inline-block;
        vertical-align: baseline;
      }
      img {
            border:0
      }
      .divider {
            margin-top:20px;
            margin-bottom:10px
      }
      .divider h2 {
            display:table;
            white-space:nowrap;
            font-size:1em;
            font-weight:700
      }
      .divider h2:after,.divider h2:before {
            border-top:1px solid #B8B8B8;
            content:'';
            display:table-cell;
            position:relative;
            top:.7em;
            width:50%
      }
      .divider h2:before {
            right:1.8%
      }
      .divider h2:after {
            left:1.8%
      }
      .verificationErrorText {
            color:#D63301
      }
      .options div {
            display:inline-block;
            vertical-align:top;
            margin-top:7px
      }
      .accountButton,.accountButton:hover {
            background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAh1BMVEX///9QUFBOTk5LS0tERERCQkI/Pz9ISEg6OjpGRkZNTU08PDyAgID09PSlpaWWlpZxcXFgYGBZWVlUVFT6+vrx8fHt7e3s7Ozo6Oji4uLJycnGxsa4uLiqqqqgoKCNjY2JiYmGhoZra2tmZmb7+/vu7u7d3d3U1NTNzc2+vr67u7usrKx7e3vprNQnAAAA8klEQVQ4y63Q127DMAxAUZpDwyMeSdqsNqu7/f/va6zahgGJKAr0vgk6DyQh+6V/BiTOOeNRA9zuAWBdM6WBlPDTvaUUoAuMrT0mgNvA1IJjQB3MKjACvp6DK0WAH+agtH8H9jQHLUUgz7Uhx8xOXzNESxirLCYA2mw8tacI5FyIYXq8A9ge2Qs6oTnw2e2ruho2rjBcXJ4ADh3jBOQLQnVhRFx2gNDZ4ACogbHXj/ft9Dj5AcgbJFu5AThQWuYBIGmgtAFQo4EFB+CPGthJAPypgY3BHsheA5UNwLyAvsYNoDyroKUe4EoFTQ/yDtTONvsGUJ8KTUYyH+UAAAAASUVORK5CYII=);
            background-repeat:no-repeat
      }
      .accountButton {
            border:1px solid #FFF;
            color:#FFF;
            margin-left:0;
            margin-right:2px;
            transition:background-color 1s ease 0s;
            -moz-border-radius:0;
            -webkit-border-radius:0;
            border-radius:0;
            text-align:center;
            word-wrap:break-word;
            height:34px;
            width:158px;
            padding-left:30px;
            background-color:#505050;
      }
      .accountButton:hover {
            background-color:#B9B9B9;
            border:1px solid #FFF;
            -moz-box-shadow:0 0 0;
            -webkit-box-shadow:0 0 0;
            box-shadow:0 0 0
      }
      .accountButton:focus {
            outline:gold solid 1px
      }
      #MicrosoftAccountExchange {
            background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAPFBMVEU1pe/////t+v4uoe5btvNixPVVwfUsoe9tyfXU7/y95vu24vrd9f5NtfLH6/ys3/o/sPE6qfD2/f+f2vnAysuQAAAAaElEQVQ4y93SORKAIAwFUEGCsoT1/nd1JkkDFhY24qt+8VMkk20lu6DAaVBOBsVKsuO8aYo08IqlYyxoRTQExfyKheRIgu5Yl4KoVhSUgNOhoiYRsmb5g2u+LtzXDNOhjKgoAZ9/8k8uZWsGqcIav5wAAAAASUVORK5CYII=);
            background-color:#33A7F2
      }
      #MicrosoftAccountExchange:hover {
            background-color:#ADDBF9
      }
      #GoogleExchange {
            background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEXcTkH////cTD/bSj3ZQDLYOyzaRDbeV0vbSDrZPS/66Obyv7rsnpfpkorjcWfgZlvXOCr++Pj5393haFz88/L88fD67Or319T1zsv1zsrxuLPuqaLuqKLoi4LlfXTgYlbWMyTWMiPwtrHwta/fXVH/sCIIAAAAmElEQVQ4y+2RyQ7DIBBDMcwAIXvovqXb/39jRaX0AEmr5px3tSV7PGLhX6TVRFpN61l9zPNS6kn9gDcXO67zDnCnO2BCiNIyMtgKKJgyY2zQ68JEDtqju0nFTcOsxPUMw1GDDUqt+tY51/YNVlhvacTgEfCDIY0Q/lkBSg4RaUmmDo4/JdMzHy1Q2ejMeCj6PrXQP5+1MI8X0Y4HL4c826EAAAAASUVORK5CYII=);
            background-color:#DC4E41
      }
      #GoogleExchange:hover {
            background-color:#F1B8B3
      }
      #TwitterExchange {
            background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAdVBMVEVgqd3///9Ypdtdp9xaptxSotpQodlNn9lWo9pUo9rX6Pa+2vGTw+iLvuZlqt79/P7K4PO62O+y0+6hyutysuD2+fzi7vne6/fT5PTE3fKs0O2lzeuZx+l7tuJqrd71+Pzz9vzn8PnQ4/SCueSAueNsrt9InNh7sQwBAAAAwklEQVQ4y92PRw6EMAwAXeIkdBbY3uv/n7gSAoLDD5hbPCPZgZVihEgYgNSUpmfS7bfbtHS2nReyL2Qoc+yp8ZRAwCEWjgGAPQ7sssKoAGsWBrrgyMZCwD77Uel+59E3Tt14xZ7qlY7BRf1CDgeMKMw8sBXGlKxWtLGvHCgkQ80m0YHpjjq4sQ74pn1mISLJVSAMiwJO98l/TWSNF1eGKzqKfZ7Vj0mnHHwodpP+WIYlZP373DTtVWxYr2FD3pOBdfIHhOAHYHQI9VgAAAAASUVORK5CYII=);
            background-color:#60A9DD
      }
      #TwitterExchange:hover {
            background-color:#BFDCF1
      }
      #FacebookExchange {
            background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAaVBMVEU7W5z///85Wps3WJsiRo8xU5fw8vYyUpY0VZiAj70pS5OBkb0vUpb7+fwsTpTR1ud6irllerBPaqX09fnx8vfs7fSQoMZxg7VsgLNGY6FCX58ZP4v++/7r7vTZ3OupstGIlsFWcalDYaCK3qwDAAAAnklEQVQ4y+XQyw7CIBAFUBgc5VUoWGtb3/7/RyoYkyZAiSsXvdt7kstA/hRg/B0GpZ6byQ3Dw0NBaH+lMYRle3T0kwayACRdBrr/gnN+QtpQWv8cR4DswiUAjozlz4RdF8AmlnmwjaDQImoZwQkRedoToUS7D+ColGoTwQidx8oEQDMHN1MBva5MOL70SCHuE1TOhOpHrRt0FWAOP4IX8PsG2qEOR30AAAAASUVORK5CYII=);
            background-color:#3B5B9C
      }
      #FacebookExchange:hover {
            background-color:#B0BDD7
      }
      #LinkedInExchange {
            background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEUAe7b///8AdrMklscAc7EAeLUAcbB5ttifzeMqmckAdLIAaqz7+/6PxeAShr0CgLkAba4nmMctksTv9Puw1eij0OWGvNtfrNJNo80YjMAeib/D4vGt3Oy82+yfzOOCvtyJvdx3tddirtI/ncoxmMj9KsrQAAAAw0lEQVQ4y9WSVw7DIAxAG8CkjJDVzO5x/zMWk0RNJaB/kfo+sGUeCMvstgI4J7F9aS5NxSLnTWLpZVDgexTqIiycUNBhgTxRyCKPYJ3dl7sITCkO+FyLXaWU310DscASOesf3ahWChGJ5cb4ASO5Joiu2EegWEmZa1c3yUwOHmHNuQgJup4CgF8YlKpcMhKvkNmb1REz6hdetsyziIBldv8lpH8ouGm28zQFCu2SOSAXlJYGYCgpFThEMFPm/zCryja8Acy7CRfMrcKPAAAAAElFTkSuQmCC);
            background-color:#0077B5
      }
      #LinkedInExchange:hover {
            background-color:#99CAE1
      }
      #AmazonExchange {
            background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png);
            background-color:#FFF;
            color:transparent
      }

      #next {
            -moz-user-select:none;
            user-select:none;
            cursor:pointer;
            width:auto;
            padding-left:10px;
            padding-right:10px;
            height:30.5px;
            -moz-border-radius:0;
           -webkit-border-radius:0;
            border-radius:0;
            background:#2672E6;
            border:1px solid #FFF;
            color:#fff;
            transition:background 1s ease 0s;
            font-size:100%
      }
      #next:hover {
            background:#0F3E83;
            border:1px solid #FFF;
            box-shadow:0 0 0
      }
      #next:hover,.accountButton:hover {
            -moz-box-shadow:0 0 0;
            -webkit-box-shadow:0 0 0;
            box-shadow:0 0 0;
      }
                        </style>
  </head>
  <body>
    <div class=navbar navbar-inverse navbar-static-top role=navigation>
      <div class=container>
        <div class=navbar-header>
          <div class=visible-xs-block>
            {{ snippets[Mobile Header] }}
          </div>
          <div class=visible-sm-block visible-md-block visible-lg-block navbar-brand>
            {{ snippets[Navbar Left] }}
          </div>
        </div>
      </div>
    </div>
    <div class=container>
      <div class=page-heading>
        <ul class=breadcrumb>
          <li>
            <a href={{ request.url | base }} title=Home>Home</a>
          </li>
          <li class=active>{{ page.title | h}}</li>
        </ul>
        {% include 'Page Header' %}
     </div>
     <div class=row>
      <div class=col-md-12>
        {% include 'Page Copy' %}
        <div id=api></div>
      </div>
     </div>
    </div>
    <footer role=contentinfo>
      <div class=footer-top hidden-print>
        <div class=container>
          <div class=row>
            <div class=col-md-6 col-sm-12 col-xs-12 text-left>
               {{ snippets[About Footer] }}
            </div>
            <div class=col-md-6 col-sm-12 col-xs-12 text-right>
              <ul class=list-social-links>
                <li><a href=#><span class=sprite sprite-facebook_icon></span></a></li>
                <li><a href=#><span class=sprite sprite-twitter_icon></span></a></li>
                <li><a href=#><span class=sprite sprite-email_icon></span></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class=footer-bottom hidden-print>
        <div class=container>
          <div class=row>
            <div class=col-md-4 col-sm-12 col-xs-12 text-left>
               {{ snippets[Footer] | liquid }}
            </div>
            <div class=col-md-8 col-sm-12 col-xs-12 text-left >
            </div>   
          </div>
        </div>
      </div>
    </footer>
  </body>
</html>
```
### Step 2: Create a page template

Create the following page template:
- **Name**: [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C Custom Page
- **Type**: Web Template
- **Web Template**: [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C Custom Page
- **Use Website Header and Footer**: Clear this check box

### Step 3: Create a webpage

Create the following webpage:
- **Name**: Sign-in
- **Parent** Page: Home
- **Partial Url**: azure-ad-b2c-sign-in
- **Page Template**: [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C Custom Page
- **Publishing State**: Published

### Step 4: Create site settings

Site settings are required to configure cross-origin resource sharing (CORS) to allow [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C to request the custom page and inject the sign-in or sign-up user interface. Create the following site settings.

| Name                              | Value                             |
|-----------------------------------|-----------------------------------|
| HTTP/Access-Control-Allow-Methods | GET, OPTIONS                      |
| HTTP/Access-Control-Allow-Origin  | `https://login.microsoftonline.com` |
| | |

For a complete list of other CORS settings, see [CORS protocol support](../add-web-resource.md#cors-protocol-support).

### Step 5: [!include[Azure](../../../includes/pn-azure-shortest.md)] configuration

1. Sign in to your [!include[Azure portal](../includes/pn-azure-portal.md)].
2. Navigate to the **[!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C Tenant Management** blade.
3. Navigate to **Settings** > **Sign-up or sign-in policies**. A list of available policies is displayed.
4. Select the policy you want to edit.
5. Select **Edit**.
6. Select **Edit policy** > **Page UI customization** > **Unified sign-up or sign-in page**
7. Set **Use custom page** to **Yes**.
8. Set **Custom page URI** to the URL of the [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C Custom Page webpage created in step 3 of this procedure. For example, `https://mydomain.com/azure-ad-b2c-sign-in`.
9. Select **OK**.

## Claims mapping

When users sign in, either for the first time or subsequently, the federated identity provider provides claims based on its database regarding the users' signing in. These claims are configurable in the identity provider.

### [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C email claims

[!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C sends the email claim as a collection. The portal accepts the first email provided in the collection as the primary email address of the contact.

### Claims to support sign-up scenarios

When a new customer who does not exist in Common Data Service is provisioned, the inbound claims can be used to seed the new contact record that the portal will create. Common claims can include first and last name, email address, and phone number, but they are configurable. The following site setting is required:

**Name**: Authentication/OpenIdConnect/[Federation-Name]/RegistrationClaimsMapping

**Description**: List of logical name/claim pairs to be used to map claim values to attributes in the contact record created during registration.

**Format**: attribute1=claim1,attribute2=claim2,attribute3=claim3

For example:  firstname=<http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname,lastname=http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname,jobtitle=jobTitle>

> [!NOTE]
> Ensure that you map the email address to the primary email (emailaddress1) of the contact. If you have added secondary email (emailaddress2) or alternate email (emailaddress3) to the contact record and mapped it to the email, identity information will not be added to the contact and a new one will be created with the email address used for registration set in the primary email (emailaddress1).

### Claims to support sign-in scenarios

The data in Common Data Service and in the identity provider are not directly linked, so the data might get out of sync. The portal should have a list of claims that you want to accept from any sign-in event to update in Common Data Service. These claims can be a subset of, or equal to, the claims coming in from a sign-in scenario. This must be configured separately from sign-in claims mapping, because you might not want to overwrite some key portal attributes. The following site setting is required:

**Name**: Authentication/OpenIdConnect/[Federation-Name]/LoginClaimsMapping

**Description**: List of logical name/claim pairs to be used to map claim values to attributes in the contact record created after sign-in.

**Format**: attribute1=claim1, attribute2=claim2, attribute3=claim3

For example: firstname=<http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname,lastname=http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname,jobtitle=jobTitle> 

The claim name is the CLAIM TYPE field listed next to the attribute in the sign-in policies Application claims.

### Allow auto-association to a contact record based on email 

Customers who have contact records with emails associated then launch a website where their external users will sign in with [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C through an email validation mechanism. The new sign-in should be associated with the existing contact record instead of creating a duplicate record. This functionality only successfully maps a contact that does not have an active identity, and the email address must be unique (not related to multiple contact records). The following site setting is required:

**Name**: Authentication/[Protocol]/[Provider]/AllowContactMappingWithEmail

**Description**: Specifies whether contacts are mapped to a corresponding email. When set to true, this setting associates a unique contact record with a matching email address, and then automatically assigns the external identity provider to the contact after the user has successfully signed in. By default, it is set to false.
