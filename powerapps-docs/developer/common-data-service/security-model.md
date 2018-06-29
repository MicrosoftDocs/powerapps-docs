# Security Model

<!-- Since much of the security information is being moved to the admin guide, this should be just the key parts that developers need to understand

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/security-dev/security-model 
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/security-dev/how-role-based-security-control-access-entities
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/security-dev/use-record-based-security-control-access-records
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/security-dev/use-field-security-control-access-field-values
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/security-dev/hierarchical-security-control-access-entities

For developers, the story is that their queries run in the context of a user.
The queries will only return records that the user is entitled to read.
Users will only be able to perform operations based on the user's privileges.
 - They can either check whether the user can perform the operation first, commonly by using a ribbon command to enable or disable
     - We should highlight the use of RetrievePrincipalAccessRequest to determine what actions that a user can perform
     - Or use RetrieveUserPrivilegesRequest to check what privileges the user has
         - See https://www.crmanswers.net/2014/09/check-if-user-has-specific-privilege.html
 - Or they can catch an error after it occurs
 - They can also use methods to Grant, Modify, and Revoke access.
 - They need to understand that fields may be secured and what to expect.

-->