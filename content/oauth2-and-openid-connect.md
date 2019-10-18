Title: OAuth 2.0 and OpenID Connect Primer
Date: 2019-10-17 17:30
Category: Authentication and Authorization
Tags: code, web, auth, oauth, openid
Authors: Mark Mikofski
Summary: Authentication and authorization with OAuth 2.0 and OpenID Connect.

# Authentication and Authorization

Web applications may contain both public and private data. Private data may
be further restricted to only certain authorized users. Therefore the web
application must first authenticate a user, and then determine what private
data they are authorized to access. The OAuth 2.0 specification implements an
alternative workflow which alows users to authorize another web application to
access resources on their behalf. The specification states that
[OAuth 2.0 is not an authentication protocol](https://oauth.net/articles/authentication/).
However, [OpenID Connect](https://openid.net/connect/) does use OAuth 2.0 to
implement a standard for authentication. GitHub is an example of the OpenID 
Connect standard, see [Basics of Authentication](https://developer.github.com/v3/guides/basics-of-authentication/).

## Terms

The following definitions are from from the linked reference by Alex Bilbie.

- **Resource (API) server**: The server hosting the protected resources,
capable of accepting and responding to protected resource requests using access
tokens.
- **Authorization server**: The server issuing access tokens to the client
after successfully authenticating the resource owner and obtaining
authorization.
- **Resource owner (the User)**: An entity capable of granting access to a
protected resource. When the resource owner is a person, it is referred to as
an end-user.
- **Client**: An application making protected resource requests on behalf of
the resource owner and with its authorization. The term client does not imply
any particular implementation characteristics (e.g. whether the application
executes on a server, a desktop, or other devices).

## Authorizing Users & Clients

There are four workflows supported by OAuth 2.0 that allow users to authorize
an applications to obtain a `Bearer` token to gain access to resources in lieu
of user credentials or client tokens.

1. [Authorization Code](#authorization-code)
2. [Resource Owner Password Credentials](#resource-owner-password-credentials)
3. [Client Credentials](#client-credentials)
4. Implicit (not covered in this post)

### Authorization Code

This is the most secure workflow and is the preferred workflow for applications
running on remote web servers that can store credentials confidentially. The
process is documented in the [OAuth 2.0 specification](https://oauth.net/2/)
and in the [References](#references). The authorization code workflow
consists of the following steps:

1. Ask an administrator to create a client application with the desired grant
type. You should be given a `client_id` and a `client_secret`. These must be
treated as secrets, _e.g._ never transmit them over HTTP, only HTTPS, and don't
commit them to repositories. The client type for the authorization code
workflow should always be **Confidential**. A _confidential_ client can keep a
secret, while a _public_ client can't. An example of a confidential client
would be a server, while a public client would be single-page JavaScript
application, because anyone could view the page source. Authorization code
should only be used with confidential clients that can keep secrets. The client
registration must include a list of redirect URI to consume the authorization
code from the authorization service.
2. Then a registered client can use an authorization URL to redirect users to
login with the identity provider and get an authorization code which can be
exchanged by the client for an access token. For this post, we'll use this
fictitious authorization URL:

        https://identity-provider/authorize/

    * The authorization URL is very picky. It must include a the following query
    string parameters:

            "client_id": <client-id>,
            "state": <optional>,
            "response_type": "code",
            "redirect_uri": <redirect_uri>,
            "scope": "read write email name"


    * The authorization can also include the desired scopes including any
    additional claims about the user such as: `email`, `name`, `given_name`,
    `family_name`, `openid`, _etc._ that can be retrieved in the ID token from the
    `/identity-provider/userinfo/` endpoint.
    * Optionally, the authorization request should also contain a unique `state`
    code, a string of any length, used to prevent cross site forgery request. It's
    up to the client to save the state sent in the request, to validate it with the
    state returned in the response from the authorization server.
    * Optionally there may be an `approval_prompt` parameter that can be provided
    and set to either `force` or `auto`. If not set, and there is a "skip
    authorization" checkbox in the app registration form which is disabled, then
    the default may be `force` which may ask users to authenticate everytime. To
    only ask users to authenticate the first time, try `auto`.
    * The identity provider will ask the user for their credentials if not
    already cached in the user's browser.
    * Depending on the `approval_prompt` parameter or the "skip authorization"
    checkbox, the user may be prompted to authorize the token, with a list of the
    claims and scopes that the token is requesting.
    * The authorization service returns a code and the state submitted by the
    client. The code can then be exchanged for an access token.

3. The redirect URI on the client side has 10 minutes, and one attempt to
exchange the authorization code for an access token. This request is sent as a
`POST`:

        https://identity-provider/token/

    * The token URL is very picky. It must include the client's id and secret
    either as a basic authentication header or as payload data. Additionally the
    following data must also be in the payload of the `POST`:

            "grant_type": "authorization_code",
            "code": <code>,
            "redirect_uri": <redirect_uri>

    * The response is a JSON string with the `access_token`, `expires_in`,
    `token_type` (always `Bearer`), `scopes` and a `refresh_token`.


### Resource Owner Password Credentials

This can be used by trusted clients by passing users credentials directly to
the authorization server, in return for a token. See the
[References](#references) for more info and examples.

### Client Credentials

This can be used by trusted clients to use the API directly on their own behalf
with any user. See the [References](#references) for more info and examples.

### Refresh Token

This can be used by any client to extend a token before it expires by
exchanging a _refresh token_ for a new token without requiring the user to
reenter their credentials. See the [References](#references) for more info and
examples.

## Getting User Info

This part of the OpenID Connect specification allows a client to use the access
token to obtain the token owners identity and other claims such as `email`,
`name`, `given_name` and `family_name`. These claims must be submitted as
scopes when the authorization code is requested. Then the client can send a
`GET` request:

    https://identity-provider/userinfo/

* The `GET` must have an authorization header containing the bearer token:

        Authorization: "Bearer <token>"

* The content of the response is JSON web token (JWT), a base-64 encoded string
signed by hashing the JWT using the client secret as the key. See
[jwt.io](https://jwt.io/) for more information and available bindings.
* The response status code should `200 OK` and the content type is
`application/jwt`. The status code will be `405 METHOD NOT ALLOWED` if the
request does not use `GET` and `403 FORBIDDEN` if the bearer token is missing
or invalid.
* The JWT contains the user name as the subject `sub` claim as well as any
additional claims requested as scopes.
* Use the `groups` scope to get a list of the xyz-app groups that a user
belongs to including the _administrator_ group.
* It is up to the client to validate that the JWT is signed correctly. The hash
algorithm is in the JWT as `alg`.
* The JWT also has an issuer claim, `iss` that should be set to the name of the
identity provider.
* The JWT audience claim, `aud` is the the client id.
* It's up to the client to check the time frame of the JWT using issued at
`iat`, expires in `exp` and not before `nbf` claims.
* The client can also confirm that the correct token was used by examining the
access token hash claim, `at_hash`. Please see the the
[OpenID Connect Core](http://openid.net/specs/openid-connect-core-1_0.html)
specification for more info.

## Permissions

Access to resources can be limited in two ways:

* permissions (not covered in this post)
* token scopes

### Token Scopes

If a user or an application is authenticated using an OAuth 2.0 token, then
that token must have the scopes required for the desired action, _regardless_
of the owner's permissions or group membership! For example if an application
has been authorized by a member of the _administrator_ group, then that token
can only be used to edit data if it has the `write` scope.

### Scopes and Claims

Scopes can also used as claims to identify a token owner. The following scopes
and claims may be available.

|Name        |Description                  |
|------------|-----------------------------|
|read        |Read scope                   |
|write       |Write scope                  |
|groups      |Access to your groups        |
|name        |JWT claim for user full name |
|email       |JWT claim for user email     |
|given_name  |JWT claim for first name     |
|family_name |JWT claim for last name      |

The `groups` scope can also be used as a claim to get the groups that the token
owner belongs to from the identity provider.

## References

* [A Guide To Oauth 2.0 Grants by Alex Bilbie](https://alexbilbie.com/guide-to-oauth-2-grants/)
* [An Introduction to OAuth 2 by Digital Ocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)
* [OAuth 2 Simplified by Aaron Parecki](https://aaronparecki.com/oauth-2-simplified/)
