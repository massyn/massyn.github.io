---
layout: post
title:  PHP Security Guide
author: "Phil Massyn"
categories: security
tags: ["security"]
image: php.jpg
---

According to [W3techs.com](https://w3techs.com/technologies/details/pl-php), at least *77.6%* of websites run on [PHP](https://www.php.net/).  PHP, like any programming language, if implemented incorrectly, can cause you a lot of headaches.

I've enjoyed coding over many years and I have developed a number of websites in [Perl](https://www.perl.org/) and PHP.  Being a security specialist, I've also seen how websites can be implemented terribly, resulting in data breaches, and website defacements.

I started by CGI programming journey in Perl, many years ago, and the writings of [Ovid](http://ovid-cgi-course.perl-begin.org/cgi-course/lesson_3.html) have been in my mind over many years.  This guide will be based on some of Ovid's _teachings_, as well as my observations.

* Some of the points raised will not be PHP specific, and would apply to any website.
* Web server examples are based on [Apache](https://httpd.apache.org/), however, the issue listed could also be relevant on other platforms like [nginx](https://nginx.org/en/) or even IIS.

Let's get started.

## Overview on web applications risks

|**Layer**|**Possible Risks**|
|--|--|
|User layer|- The user does something wrong (like delete a record accidentally)<br>- The user does not protect their credentials, and allows an attacker to use the application with their access credentials.|
|Application|- Coding errors in the application could allow an attacker to exfiltrate data or misuse the application.|
|Middleware|- Components like Apache or PHP need to be maintained to ensure the software is not compromised.|
|Operating system|- Vulnerabilities in the OS may cause an outage, or data leakage<br>- Misconfiguration may allow an attacker to compromise the server.<br>- Malware could cause the server to be compromised.<br>- Improper access controls could allow an attacker to brute-force their way onto the system with weak credentials.|
|Hardware|- Server may crash causing an outage or data loss|

## Web Server Configuration

### Do not reveal the Web server version

Sites like [OpenCVE](https://www.opencve.io/cve?vendor=apache) list all known system vulnerabilities.  By revealing your web server version, it becomes an easy task for an attacker to exploit your server.

**Detecting the issue**

The server headers can reveal a lot of useful information about your environment.  Using `curl -I` you can quickly check the headers being returned.

Run the command on your platform, and review the `Server` tag being returned.

```bash
$ curl -Is https://www.massyn.net | grep -i '^Server'
server: AmazonS3
```

In this example, you can see my website is hosted on Amazon S3.  If the response actually included a version number, you will need to take steps to switch that off.

**Remediation**

**NOTE** - this only prevents the leaking of the server version information.  It does not actually make the server any more difficult to crack.

#### PHP

* Edit the `php.ini` file.

```
$ vi /usr/local/etc/php/php.ini
```

(If you can't find the `php.ini` file, use `sudo find / -name php.ini`)

* Add the following line to your config

```
expose_php=off
```

#### Apache

* Edit the apache configuration file `security.conf`

```
$ vi /etc/apache2/conf-available/security.conf
```

* Add the following lines (if they don't exist), or edit the ones that may already be there to look like this.

```
ServerTokens Prod
ServerSignature Off
```

* Restart Apache for the settings to take effect.

```
$ sudo service apache2 restart
```

### Keep the Web server up to date

Any kind of software will have bugs.  Bugs are caused by human error, where the programmer may not have understood the requirements correctly, or they simply made a mistake during the implementation of a particular process.  Other more serious bugs are where the programmer actually did nothing wrong, yet the bug was introduced due to a design issue, where a designed feature is being able to be abused by an attacker for a purpose different to what the designers anticipated.

This is a problem because bugs like these can allow an attacker to compromise your system, and get it to do things you don't want it to, like allowing an attacker to use your resources for his own purposes (while you are paying for it), stealing your information, or simply bringing your site down.

**Detecting the issue**

Unless you run a vulnerability scanner on your system, you probably won't know that Apache may need to be updated.  This is not as much of an issue in larger enterprises that do run scanners on a regular basis, but it does become an issue with smaller companies that may not be able to afford such scanners.

**Remediation**

Keep your web server patched.  Depending on the system you're running, you should be able to update the web server with ease.

```
$ apt-get update apache2 php -y
```

**Warning**

While keeping the system patched is a best practice, so is having good backups, and a good testing practice.  Make sure your system still works fine after these updates, and initiate any sort of roll-back activity should the update cause you an operational outage.

### Use TLS/SSL - always!

Any network communications could potentially be intercepted by an unknown third-party, reading the data, or able to inject their own data into the traffic without you realising it.  This has the increased risk that your client cannot trust that the server they are connecting to does in fact belong to you, since they have no way of confirming your server identity.

Keep in mind that a TLS/SSL certificate is not just about encryption - it is also about confirming that you (the server) are who you claim to be.  When dealing with sensitive data, like banking transactions, your client wants that validation that they are in fact talking to your server, instead of someone pretending to be you.

**Detecting the issue**

Using a tool like [SSLLabs](https://www.ssllabs.com/ssltest/) you will be able to confirm that your web server's SSL certificate is as robust as it can be.  Any site that is serving pages over HTTP instead of HTTPS is a clear indicator that they're not using encryption for their network traffic.

For more information, refer to [whynohttps.com}(https://whynohttps.com/).

**Remediation**

[DigitalOcean](https://www.digitalocean.com) has written a very nice [article](https://www.digitalocean.com/community/tutorial_collections/how-to-secure-apache-with-let-s-encrypt) explaining how to install [Let's Encrypt](https://letsencrypt.org/) on your web server.  Simply follow the steps to implement the free certificate.

**Caveats**

I like Let's Encrypt, and I will encourage you to use it.  Do keep in mind that an attacker can also use Let's Encrypt to get their own domains.  So while using this service is a huge benefit, it may not be suited to all use cases.  If you are running sensitive workloads, like banking or medical data, consider getting a proper certificate from a reputable certificate provider, who can validate the authenticity of your certificate.  I am quite weary of eCommerce sites that operate on a Let's Encrypt certificate, as I have no way of knowing if that site is legit.

### Harden your web server headers

To improve security, web servers will provide additional information to the browser via their server headers to tell the browser what can be allowed, what certain configuration is, etc.  These headers are also used to tell the browser which sites can be allowed for cross-site access, for example, which sites can be used to query APIs.  This is quite important 

**Detecting the issue**

Using a tool like [securityheaders.com](https://securityheaders.com/), you will be able to identify if you have any gaps in your security header configuration.  Anything less than an **A** should be of concern.

**Remediation**

* Edit the `security.conf` file

```
$ vi /etc/apache2/conf-enabled/security.conf
```

* Add the following lines to it

```
Header always append X-Frame-Options SAMEORIGIN
Header set X-Content-Type-Options nosniff
Header set X-XSS-Protection "1; mode=block"
Header set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
Header set Content-Security-Policy "default-src https: 'unsafe-inline' 'unsafe-eval'"
```

**NOTE** - some of these settings might break your application.  Test it properly!

## PHP Configuration

### Turn off error reporting

There are two main issues with error messages.  

The first, is it reveals information about the configuration of the application that should not be known.  Looking at an example of a SQL database connection failure...

    Fatal error: Uncaught PDOException: SQLSTATE[HY000] [2002] Connection refused in /var/www/html/mysql.php:6 Stack trace: #0 /var/www/html/mysql.php(6): PDO->__construct('mysql:host=some...', 'username', 'secret123') #1 {main} thrown in /var/www/html/mysql.php on line 6

On face value, you may not think much of it, but for an attacker it just revealed some information, like

* You're using **mySQL** (not that this is an issue per se - you're using PHP so chances are your backend DB is mySQL)
* Your website is hosted in `/var/www/html/` -- this is good to know if the attacker were to try a file-based attack.
* The username and password for the database was hardcoded in the mySQL connect string (`username` / `secret123`)
* A partial database hostname was also visible (`some...`)

If you have a development server that is isolated from the internet then having the error messages is valuable during the development process, however, once the application moves to production, the error reporting should be turned off.

**Remediation**

* Edit the `php.ini` file.

```
$ vi /usr/local/etc/php/php.ini
```

(If you can't find the `php.ini` file, use `sudo find / -name php.ini`)

* Add the following line to your `php.ini` file

```
error_reporting=0
display_errors=off
```

* Restart Apache for the settings to take effect.

```
$ sudo service apache2 restart
```

**More Information**

* [ini.error-reporting](https://www.php.net/manual/en/errorfunc.configuration.php#ini.error-reporting)
* [ini.display-errors](https://www.php.net/manual/en/errorfunc.configuration.php#ini.display-errors)

### Harden the PHP session cookie

If you're using [session_start()](https://www.php.net/manual/en/function.session-start.php) in your code, your application is using the `PHPSESSID` cookie.  This cookie is a great mechanism to manage state for your application.  By default, this cookie is not very secure.  You need to evaluate the security requirements of your application, and adapt the various settings accordingly.

**Remediation**

* Edit the `php.ini` file.

```
$ vi /usr/local/etc/php/php.ini
```

(If you can't find the `php.ini` file, use `sudo find / -name php.ini`)

* Add the following line to your `php.ini` file, and adjust per your requirements.

```
session.cookie_httponly=1       # Refuse access to the cookie from JavaScript
session.use_strict_mode=On      # only accepts valid session IDs
session.cookie_secure=On        # use only over TLS/SSL connections
session.gc_maxlifetime=86400    # delete cookies older than 1 day (86400 seconds)
session.sid_length="48"         # Use a length of 48 - make this longer if you can
session.hash_function="sha512"  # Use a strong hashing algorithm
```

* Restart Apache for the settings to take effect.

```
$ sudo service apache2 restart
```

**More Information**

* [session.security.ini](https://www.php.net/manual/en/session.security.ini.php)

## Application development

### Using the $_SESSION array

The `$_SESSION` global variable is a great way to manage state across an application.  Any data stored in this variable will be available as a text file on the server.

    Do not store any sensitive information (like passwords) in this variable. Use this only to track state.

**Remediation**

You may decide to change the path where the temporary files are stored.  This is defined through the `session.save_path` setting in the `php.ini` file.

* Create the path where you want to store the session files.  In this example, I'm using `/some/secure/folder`

```
$ mkdir /some/secure/folder/
```

* Edit the `php.ini` file.

```
$ vi /usr/local/etc/php/php.ini
```

(If you can't find the `php.ini` file, use `sudo find / -name php.ini`)

* Add the following line to your `php.ini` file, and adjust per your requirements.

```
session.save_path=/some/secure/folder   # path where the session files are to be stored
```

* Change the permissions of the folder

```
$ chown -R www-data:www-data /some/secure/folder
$ chmod -R 600 /some/secure/folder
```

**WARNING** DO NOT set the permissions to anything like *777*, as this will make the folder executable, and allow an attacker to inject their own code into a cookie for execution.

* Restart Apache for the settings to take effect.

```
$ sudo service apache2 restart
```

**More Information**

* [reserved.variables.session](https://www.php.net/manual/en/reserved.variables.session.php)

### Sanitise input (and headers!)

Whenever you use the `$_POST` or `$_GET` variables, data is being read from the browser.  This is quite normal - your application needs to receive data from the browser to do what it needs to do.  The problem however is you have no way to confirm that the user is using the application in the way it was intended.  One scenario, is where you may require the user to insert a number, however the user is entering data other than a number.

There are a number of security concerns too.

* SQL Injection attacks can occur with malformed inputs.  
* XSS (Cross-site scripting) vulnerabilities can occur when scripted code (for example JavaScript) is injected into an application.

Let me demonstrate a simple SQL injection vulnerability.  Consider the following piece of (very badly written) code...

```php
...
$conn = new mysqli($servername, $username, $password, $dbname);

$sql = "SELECT * FROM users WHERE username = '" . $POST['username'] . "' AND password = '" . $POST['password'] . "'";
$result = $conn->query($sql);
...
```

Assuming a user logs on with a username and password, the SQL query passed to the database would be somethig like 

```sql
SELECT * FROM users WHERE username = 'admininstrator' AND password = 'secret'
```

So far so good... but... what if the attacker uses the username `administrator'--` and password `12345` ?  The resulting SQL query would be:

```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = '12345'`
```

Noticed that?  The query changed -- it is simply honouring the `username` piece, not the `password` part, since the `'--` that was passed during the `username` field caused the SQL query to be altered, and causing the application to authenticate the user without a password.

For that reason, it is imperitive that input be sanitised.  One way to get around this problem, is to use the [`filter_input`](https://www.php.net/manual/en/function.filter-input.php) function.

```php
$sql = "SELECT * FROM users WHERE username = '" . filter_input(INPUT_POST, 'username', FILTER_SANITIZE_SPECIAL_CHARS) . "' AND password = '" . filter_input(INPUT_POST, 'password', FILTER_SANITIZE_SPECIAL_CHARS) . "'";
```
(Please note - while this code is _slightly_ better, you should still not use it.)

**More Information**

* [function.filter-input](https://www.php.net/manual/en/function.filter-input.php)

### Escape all output

For an application to be effective, it has to be able to pass data back to the browser.  When we get a variable from any source, be it a database, or any other source for that matter, if this data contains some arbitrary code, for example, some rogue JavaScript, it has the risk of executing that JavaScript.

Take the following example.  Assume that `$variable` contains data provided from a database, which might contain some JavaScript, that is simply displayed on the screen.

```php
<?php
$variable = '<script>alert("This is not supposed to work!!");</script>';

print "<html><h1>$variable</h1></html>";
?>
```

When users have the ability to post data uncontrolled, and the same data is returned unfiltered, there is a risk your users will receive some JavaScript that is not intended for them, resulting in their workstations getting compromised.

**Remediation**

Using the [`htmlentities`](https://www.php.net/manual/en/function.htmlentities.php) function, pass all data being sent to the browser through this function.

```php
<?php
$variable = '<script>alert("This is not supposed to work!!");</script>';

print "<html><h1>" . htmlentities($variable, ENT_QUOTES | ENT_HTML5, 'UTF-8') . "</h1></html>";
?>
```

**More Information**

* [function.htmlentities](https://www.php.net/manual/en/function.htmlentities.php)

### Do not let the user near the shell

Consider the following code.

```php
<?php
$x = $_POST['file'];
$output = exec("ls /tmp/$x*");
print "<html><h1>$output</h1></html>";
?>
```

A user posts a variable into `file`, and the code executes the `ls` command, and returns the result.. No issue there.. What if the user injects `'ses* && hostname #'`.  The command passed to the server would be

```bash
ls /tmp/ses* && hostname #*
```

This is bad.  The user now has the ability to execute any command to the server.  Any code that touches the shell should be closely scrutinised.  Avoid it at all cost.

### Do not store user passwords

Remember our earlier example where I demonstrated a SQL injection example with a basic username and password stored in a database?  Don't do that.  

**Do not EVER store a password in clear text in a database, EVER!**

**Remediation**

Don't create your own authentication system.  If you don't know what you're doing, you could cause unauthorised access issues, or even worse, leak user passwords.  Use a service like [AWS Cognito with PHP](https://www.awssecurity.info/technical/using-cognito-in-php.html), or some other oath2 service to do the user authentication for you.

If you have to store your own passwords, use a function like [`password_hash`](https://www.php.net/manual/en/function.password-hash.php) to create a secure, non-reversable hash of the password.

**More Information**

* [AWS Cognito with PHP](https://www.awssecurity.info/technical/using-cognito-in-php.html)
* [function.password-hash](https://www.php.net/manual/en/function.password-hash.php)

### Store database credentials securely

With your application connecting do a database, chances are you have some sort of clear text file on your server that contains the database credentials.  Typically you may have a `config.php` file that contains something like :

```php
<?php
$dbServer = 'localhost';
$dbUser = 'root';
$dbPassword = 'secret123';
$dbDatabase = 'myApplication';
?>
```

Your application needs these credentials - it has to be able to connect to the database to run your desired queries, but at the same time, you also need to protect the credentials.

* Move the `config.php` to a different folder that is not served by your web server.  If your server uses `/var/www/html/`, you could store the config file in `/var/www`
* Adjust the permissions, and only allow your web service from accessing the file.

```bash
$ chown www-data:www-data /var/www/config.php
$ chmod 600 /var/www/config.php
```

**More Information**
If your application is hosted on the cloud (for example [AWS](https://aws.amazon.com)), you could always use [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) to store your credentials securely.

* [GetSecretValue.php](https://docs.aws.amazon.com/code-samples/latest/catalog/php-secretsmanager-GetSecretValue.php.html)

### Disable sensitive functions

In an earlier example, we demonstrated how a user can inject custom commands to the shell.  There is a way to simply prevent this from running in the first place.  There are several PHP functions that can be very handy, but also very dangerous.  It is a good practice to disable sensitive functions.

Do note that some applications may fail if you simply disable all the functions.  Some application redevelopment may be required.

**Remediation**

* Edit the `php.ini` file.

```
$ vi /usr/local/etc/php/php.ini
```

(If you can't find the `php.ini` file, use `sudo find / -name php.ini`)

* Look for the `disable_functions` line in your `php.ini` file.  If it does not exist, add it.

```
disable_functions =exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,show_source
```

* Restart Apache for the settings to take effect.

```
$ sudo service apache2 restart
```

**More Information**

* [ini.disable_functions](https://www.php.net/manual/en/ini.core.php#ini.disable-functions)

### Disable remote url access

This option enables the URL-aware `fopen` wrappers that enable accessing URL object-like files.  An attacker might be able to run arbitrary PHP commands using this function to query a remote source, and inject rogue code into your application.

**Remediation**

* Edit the `php.ini` file.

```
$ vi /usr/local/etc/php/php.ini
```

(If you can't find the `php.ini` file, use `sudo find / -name php.ini`)

* Look for the `allow_url_fopen` line in your `php.ini` file.  If it does not exist, add it.

```
allow_url_fopen=Off
```

* Restart Apache for the settings to take effect.

```
$ sudo service apache2 restart
```

**More Information**

* [ini.allow-url-fopen](https://www.php.net/manual/en/filesystem.configuration.php#ini.allow-url-fopen)
